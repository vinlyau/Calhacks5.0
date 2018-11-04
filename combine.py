import json
import os

f = open("finished.json", "w")
d = dict()
for i in os.listdir('.'):
    try:
        g = open(i, "r").read()
        h = eval(g)
        d.update(h)
    except:
        pass
print(d)
f.write(str(d))
f.close()
