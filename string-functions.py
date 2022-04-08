sample_string = "    hi my name is sona       "
sample_string=sample_string.lstrip()
sample_string=sample_string.rstrip()
print(sample_string)

print(sample_string.capitalize())
print(sample_string.upper())

a_list = ["sona","arghavan","ben"]
print("+".join(a_list))

b_list = sample_string.split()
for i in b_list:
    print(i)