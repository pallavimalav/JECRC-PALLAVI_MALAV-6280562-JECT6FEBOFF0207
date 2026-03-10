file = open('temp1.txt', 'r')

'''
1. read : display the file content as it is.
2. readline() : it will read the data line-by-line, single line at a time.
3. readlines()

'''
print(file.read())
file.seek(0)

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

print(file.readlines()) # epmty list

file.close()

# file = open('notes.txt', 'r')
# print(file.read())
# file.close()


