import json
import os

for i in os.listdir('.'):
    print(i)
    try:
        json_data = open(i)
        d = json.load(json_data)
        a = []
        for j in d['results']:
            a.append(j['alternatives'][0]['transcript'])
        b = " ".join(" ".join(" ".join(a).split("%HESITATION")).split())
        print(b)
        json_data.close()
        f = open(i, "w")
        f.write(str({i.split(".")[0], b}))
        f.close()
    except:
        print("h")
        pass
