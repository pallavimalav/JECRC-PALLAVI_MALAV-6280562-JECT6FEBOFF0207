# file = open('temp.txt', 'w')
# file.write('I am the first line.')



# file.close()

# file = open('temp1.txt', 'w')
file = open('temp1.txt', 'w+')
# file.write('I am the new data')
file.writelines([
    'first line\n',
    'sec line\n',
    'third line\n',
    'fourth line\n',
    'fifth line\n',
    'sixth line\n'

])
# to make the python interpreter to point at a specific index, we use seek(index).

file.seek(0)

print(file.read())


file.close()




