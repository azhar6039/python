#Store the dictionary in a json file.
import json
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
with open("company1.json","w") as file:
    #file.write(json.dumps(d,sort_keys=True, indent=4))
    json.dump(d,file,indent=4)