import json

file_path = "./test/test.json"

with open(file_path, 'r', encoding='UTF8') as file:
    data = json.load(file)
    print(type(data))
    print(data)
    print(data["Tyler"])