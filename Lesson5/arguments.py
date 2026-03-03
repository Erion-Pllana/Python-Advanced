

def person(name, greeting="Hello"):
    message= f"{greeting}, {name}"
    return message

default_greeting = person("Erion")
costum_greeting = person("Erion", 'Hi')

print(default_greeting)
print(costum_greeting)