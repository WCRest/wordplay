import parser, content, json

f = open('../lyrics/tiktok.lrc')
lines = f.readlines()
f.close()
pLines = parser.linesToArray(lines)
content.writeTo(pLines, "../index.html")

g = open('../index.json', "w")
g.write( json.dumps(pLines))
g.close()
