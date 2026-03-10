# wap to take a character from the user and convert it into lowercase if it is in uppercase or vice-versa. 

#  character = chr(input("Enter a character: "))

# do it by using ascii values, instead of isLower and isUpper


ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only ONE character.")
else:
    if ch.islower():
        print("Converted:", ch.upper())
    elif ch.isupper():
        print("Converted:", ch.lower())
    else:
        print(ch)


        # print("It is not an alphabet character.")

# A --> a
# a --> A
# 1 -->
# * --> *





       