# dumps(): encryption
# loads(): decryption

'''
1.JSON,
2. pickle,

'''
import json

file = open('temp.txt','w+')   # use w+ to overwrite file

data = {
    'fullname': 'Rahul Gandhi',
    'userid': '887#',
    'password': '****'
}

# convert python dict to json string
enc_data = json.dumps(data)

file.write(enc_data)
file.seek(0)

enc_data = file.read()
print(type(enc_data))

# convert json string back to python dict
ori_data = json.loads(enc_data)

print(ori_data, type(ori_data))

file.close()
