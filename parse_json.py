from __future__ import unicode_literals
import json
import sys

args = sys.argv

file_data = open(args[1], "r")

keys = ["name", "lat", "lng", "compound_code", "global_code", "say"]
data_dict = {}
for k in keys:
    data_dict[k] = None

for f in file_data:
    strip_str = f.lstrip()
    for k in keys:
        key_len = len(k)
        temp_str = strip_str[1: key_len+1]
        if temp_str == k:
            if data_dict[k] == None:
                if k != "compound_code":
                    data_dict[k] = strip_str[key_len + 6:-3] #:と空白、,と改行コードを消す
                else:
                    temp_prefecture = strip_str[key_len + 6:-3].split("、")
                    data_dict[k] = temp_prefecture[-1]
                print(data_dict[k])
                print(strip_str,end="")

print("\n------Dict Data------")
print(data_dict)

print("\n------Json Data------")
json_data =  json.dumps(data_dict, ensure_ascii=False)
print(json_data)

with open("Data_" + args[1], "w") as fw:
    fw.write(json_data)

print("end")