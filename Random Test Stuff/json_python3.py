import json 

with open("questions.json", "r") as read_file:
	data = json.load(read_file)

print(data[0]["question"])