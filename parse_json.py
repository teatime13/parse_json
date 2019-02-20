from __future__ import unicode_literals
import json

file_data = open("./raw_json", "r")

keys = ["name", "lat", "lng", "compound_code", "global_code", "say"]
data_dict = {}
for k in keys:
    data_dict[k] = None

for f in file_data:
    strip_str = f.lstrip()
    for k in keys:
        key_len = len(k)
        temp_str = strip_str[: key_len]
        if temp_str == k:
            if data_dict[k] == None:
                data_dict[k] = strip_str[key_len + 3:-2] #:と空白、,と改行コードを消す
                print(strip_str,end="")

print("\n------Dict Data------")
print(data_dict)

print("\n------Json Data------")
json_data =  json.dumps(data_dict, ensure_ascii=False)
print(json_data)

with open("jsonGPS", "w") as fw:
    fw.write(json_data)

print("end")