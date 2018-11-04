import json
import os

for i in os.listdir('.'):
    try:
        json_data = open(i, "r")
        f = list(eval("".join(list(json_data.read()))))
        a = f[0]
        b = f[1]
        c = min([a, b], key=lambda x: len(x))
        d = max([a, b], key=lambda x: len(x))
        e = {c : d}
        print(e)
        json_data.close()
        json_data = open(i, "w")
        json_data.write(str(e))
        json_data.close()
    except:
        print("h")
        pass
