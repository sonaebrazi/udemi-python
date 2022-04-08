sample_string = input("enter string: ")
sample_string=sample_string.upper()
list_of_words = sample_string.split()

for elem in list_of_words:
     print(elem[0],end="")
