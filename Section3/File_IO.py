# File I/O
# File functions
# For Windows the '\' is escaped using '\\'
# For MacOS the '\', use '/' instead
# Text in the file is "This is a test"

# open()
file = open('fileload.txt', mode='r')

# seek()
file.seek(2)

# read() / readlines()
print(file.read())
file.seek(0)
print(file.readlines())
file.close()

# with statement
with open('fileload.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)
