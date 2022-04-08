message = input("enter the message: ")
shift_key = int(input("enter key:(1 - 26):"))
secret_message=""
for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += shift_key
        if char.isupper():
            if char_code > ord("Z"):
                char_code -= 26
            elif char_code < ord("A"):
                char_code += 26
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26
        secret_message += chr(char_code)
    else:
        secret_message += char
print("encrypted message is : ", secret_message)

shift_key= -shift_key
original_message=""
for char in secret_message:
    if char.isalpha():
        char_code=ord(char)
        char_code += shift_key
        if char.isupper():
           if char_code > ord("Z"):
                char_code -= 26
           elif char_code < ord("A"):
                char_code += 26
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26
        original_message += chr(char_code)
    else:
        original_message += char
print("original message is : ", original_message)


