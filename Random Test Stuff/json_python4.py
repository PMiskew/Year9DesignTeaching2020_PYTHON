import json


data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('dataA.txt', 'w') as outfile:
    json.dump(data, outfile)


import json

data = []
data.append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data.append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data.append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('dataB.txt', 'w') as outfile:
    json.dump(data, outfile)