import json
from collections import OrderedDict

file_data = []

with open('convert.json', 'w', encoding='UTF8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
    


file_path = "./lib/script/fredit-login.side"
with open(file_path, 'r', encoding='UTF8') as file:
  fullList = json.load(file)
  # print(type(data))
  # print(data)
  # print(len(jsonObject.get("tests")))
  # tests = dataList.get("tests")

  for idx1, depth1Item in enumerate(fullList, 1):
    if (depth1Item == "tests"):
      depth1List = fullList.get("tests")
      for idx2, depth2Item in enumerate(depth1List, 1):
        depth2List = depth2Item.get("commands")
        for idx3, depth3Item in enumerate(depth2List, 1):
          object_data = OrderedDict()
          object_data["command"] = depth3Item.get("command")
          if "click" in depth3Item.get("command"):
            dept3List = depth3Item.get("targets")
            for idx4, depth4Item in enumerate(dept3List, 1):
              # print(type(depth4Item))
              dept4List = depth4Item
              for idx5, depth5Item in enumerate(dept4List, 1):
                if "css" in depth5Item:
                  print(depth5Item)
                  object_data["targets"] = depth5Item
                  break
            object_data["duration"] = 5

            object_data["value"] = depth3Item.get("value")
            file_data.append(object_data)

with open('convert.json', 'w', encoding='UTF8') as make_file:
  json.dump(file_data, make_file, ensure_ascii=False, indent="\t")