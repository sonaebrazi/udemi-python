print(type("3"))
print(type('3'))
print(type('''3'''))


sample_str = "hi my name is sona"
print("length=",len(sample_str))
print(sample_str[-1])
print(sample_str[0:-1:7])
print(sample_str[::-1])
print("Green "+"Tree")
print("Go "*5)
print(str(4))


for char in sample_str[5:9]:
    print(char,"!")

#getting unicode of a character:
print("A =",ord("A"))

#getting character of a unicode:
print("65 =",chr(65))


