from Lesson5.function import greet

greeting = "Hello"
name = "Renato"

def greet_2():
    global greeting
    greeting = "Goodbye"

    name = "Liron"

    message = f"{greeting}, {name}!"

    print(message)

    greet_2()

    print(greeting)

    print(name)