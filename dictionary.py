person = {
  "name": "Rezwan",
  "expertise": "Python",
}


print(person.get('name'))
print(person['name'])

print(person.get('a', 'Nai nai nai')) # no error
print(person['a']) # error