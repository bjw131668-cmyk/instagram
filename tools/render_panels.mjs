#!/usr/bin/env node
// 컷 HTML -> 인스타 업로드용 JPEG (1080x1350)
// 사용법: node tools/render_panels.mjs episodes/001
//   episodes/001/panels/*.html 을 이름순으로 렌더링해 episodes/001/out/01.jpg ... 로 저장
import { createRequire } from "node:module";
const { chromium } = createRequire(import.meta.url)("playwright");
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const ep = path.resolve(process.argv[2] ?? "");
const panelDir = path.join(ep, "panels");
if (!process.argv[2] || !fs.existsSync(panelDir)) {
  console.error("사용법: node tools/render_panels.mjs episodes/<번호>");
  process.exit(1);
}
const panels = fs.readdirSync(panelDir).filter((f) => f.endsWith(".html")).sort();
if (!panels.length) { console.error(`컷 HTML이 없습니다: ${panelDir}`); process.exit(1); }
const out = path.join(ep, "out");
fs.mkdirSync(out, { recursive: true });
for (const f of fs.readdirSync(out)) if (/^\d+\.jpg$/.test(f)) fs.unlinkSync(path.join(out, f));

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
const failed = [];
page.on("requestfailed", (r) => failed.push(r.url()));
for (const [i, name] of panels.entries()) {
  await page.goto(pathToFileURL(path.join(panelDir, name)).href, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  const file = path.join(out, `${String(i + 1).padStart(2, "0")}.jpg`);
  await page.screenshot({ path: file, type: "jpeg", quality: 92, clip: { x: 0, y: 0, width: 1080, height: 1350 } });
  console.log(`${name} -> ${path.relative(process.cwd(), file)}`);
}
await browser.close();
if (failed.length) { console.error("불러오지 못한 리소스:\n" + failed.join("\n")); process.exit(2); }
