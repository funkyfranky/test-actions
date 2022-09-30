# Read in the file
with open('helloworld.py', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('12345', 'abcde')

# Write the file out again
with open('file.txt', 'w') as file:
  file.write(filedata)