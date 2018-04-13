import json

f = open('train-v1.1.json')
data = json.load(f)

print(data['data'])