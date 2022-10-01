
# # Read in the file
# with open('helloworld.py', 'r') as file :
#   filedata = file.read()

# # Replace the target string
# filedata = filedata.replace('12345', 'abcde')

# # Write the file out again
# with open('helloworld.py', 'w') as file:
#   file.write(filedata)

#with open(file)

import fileinput

filename="helloworld.py"

# print("hallo")

for line in fileinput.input(filename, inplace=True):
    if "TOKEN=" in line:
      print("TOKEN=YOUR_TOKEN_HERE")
      #print("TOKEN=YOUR_TOKEN_HERE", line, end='')