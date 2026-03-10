file = open('jecrc.txt', 'a+')

# file.write('JECRC is a university!')
file.writelines([
    'there is cse branch\n'
    'there is business branch\n'
    'there is design branch\n'
])
file.seek(0)
print(file.read())


file.close()