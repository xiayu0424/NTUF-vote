import json
with open('data.json', 'r') as f:
    data = json.load(f)


def check(id):
    if id in data['data'].keys():
        return False
    else:
        return True
