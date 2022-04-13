import os
with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")
with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.read())

print(my_file.closed)
print(my_file.name)
print(my_file.mode)

with open("mydata.txt", encoding="utf-8") as my_file:
    line_num = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        print("Line", line_num)
        word_list = line.split()
        print("Number of Words :", len(word_list))

        char_count = 0
        for word in word_list:
            for char in word:
                char_count += 1
        avg_num_chars = char_count / len(word_list)

        print("Avg Word Length : {:.2f}".format(avg_num_chars))
        line_num += 1
