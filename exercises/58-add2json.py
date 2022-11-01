#Please download the json file in the attachment and use Python to add a new employee to the file's content so that the file looks like in the expected output below.
import json
with open ("company2.json","r+") as file:
    d=json.load(file)
    #d=json.loads(file.read())
    print(type(d))
    d["employees"].append(dict(firstName="Albert",lastName="Bert"))
    file.seek(0)
    json.dump(d,file,indent=4)