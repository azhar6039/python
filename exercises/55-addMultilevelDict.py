#Adding to Multilevel Dictionaries
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
#d1={"firstName": "Albert", "lastName": "Bert"}
d["employees"].append(dict(firtsName="Albert",lastName="Bert"))
print(d)