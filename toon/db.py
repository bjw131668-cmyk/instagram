import re
FILES=["/home/claude/toon/나물려_대본DB_07-18.md","/home/claude/toon/나물려_대본DB_19-30.md"]
def load(n):
    """대본 DB에서 N화를 그대로 읽는다 -> dict(title, next_title, script[10], reel[6])"""
    for f in FILES:
        s=open(f).read()
        m=re.search(rf'\n## {n}화\. (.+?) \((?:.*?)다음 화 예고: (\d+)화 (.+?)(?: 편)?\)\n(.*?)(?=\n## |\Z)', s, re.S)
        if not m: continue
        body=m.group(4)
        lines=re.findall(r'^\s+\d+\. (.+)$', body, re.M)
        script=[tuple(x.strip().replace("|","\n") for x in l.split(" / ")) for l in lines]
        assert len(script)==10 and all(len(x)==4 for x in script), (len(script), [len(x) for x in script])
        reel=[int(x) for x in re.search(r'- 릴스: ([\d, ]+)', body).group(1).split(",")]
        tm=re.search(r"- 썸네일\(표지·릴스 커버 말풍선\): (.+?) / (.+)", body)
        thumb=tuple(x.strip().replace("|","\n") for x in tm.groups()) if tm else None
        return dict(thumb=thumb, title=m.group(1), next_n=int(m.group(2)), next_title=m.group(3), script=script, reel=reel, body=body)
    raise KeyError(n)
