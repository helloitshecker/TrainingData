import json
import os
import re

def getFiles(path=None):
    if path == None:
        return None


DATA_JSON = "data.json"

dirs = os.listdir()

data_json = open("data.json", "r")
data_json_content = data_json.read()
data_json.close()

dt = json.loads(data_json_content)

datasets = dt['datasets']

pattern = re.compile(r'\[(\d+)-(\d+)\]')

print("FILENAME \t\t\t SIZE")
for dataset in datasets:
    parent = ""
    for token in dataset.split('/'):
        if os.path.isdir(token):
            parent += token + "/"
            continue
        m = pattern.search(token)
        if m:
            start, end = map(int, m.groups())
            for i in range(start, end+1):
                filename = f"{parent}{token.split('[')[0]}{i}.{token.split('.')[-1]}"
                if not os.path.exists(filename):
                    print(f"{filename} does not exist!")
                else:
                    print(f"{filename} \t {os.path.getsize(filename)}B")
