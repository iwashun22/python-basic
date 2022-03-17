person = {
   "name": "John Micheal",
   "job": "Programmer",
   "hobbies": ["Guitar", "Basketball", "Cooking"],
   "address": {
      "street": "some way",
      "city": "Lol Angle"
   }
}

print(person["name"]) # same
print(person.get("name")) # same

# method "get" can have a default value when the key doesn't match to any
print(person.get("email", "No register")) # No register <- there's no email in person

print(person["hobbies"][1])
print(person["address"]["street"])