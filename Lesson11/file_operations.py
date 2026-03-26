# file_path = "example.txt"
# file = open(file_path, "r")
#
# content = file.read()
# print(content)
#
# file.close()

import os

#Opening and closing files
file = open('example.txt' , 'r')
file.close()

# using with statement for automatic closing
with open('example.txt', 'r') as file:
    content = file.read()

# reading from files
with open('example.txt','r') as file:
    content = file.read() #read entire content
    line = file.readline() #read a single line
    lines = file.readlines() #read all lines into a list

#writing to files
with open('example.txt', 'w') as file:
    file.write('Hello World!')

lines = ['Hello World!\n', 'Welcome to Python\n']
with open('example.txt','w') as file:
    file.writelines(lines)

#moving the cursor
with open('example.txt', 'r') as file:
    file.seek(0)
    data = file.read()
    print(data)

#checking file existance
if os.path.exists('example.txt'):
    print('File exists')

#appending to file
with open('example.txt', 'a') as file:
    file.write("New data appended")

#reading and writing binary files
data = b'This is some binary data'
with open('example.bin', 'wb') as file:
    file.write(data)