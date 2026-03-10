# achieve the desired output for the below given input :
# INPUT : LAvi@123Ab
# OUTPUT : laVI@123aB 

# you can't use any inbuilt functions 



s = "LAvi@123Ab"
result = ""

for ch in s:
    ascii_val = ord(ch)

    if 65 <= ascii_val <= 90:
        result += chr(ascii_val + 32)
    
    elif 97 <= ascii_val <= 122:
        result += chr(ascii_val - 32)  
    
    else:
        result += ch 

print(result)






