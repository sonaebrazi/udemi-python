#calculator
num_1 , operator , num_2 = input("enter:").split()
num_1 = int(num_1)
num_2 = int(num_2)
if operator == "*":
    print("{} * {} = {}".format(num_1,num_2,(num_1 * num_2)))
elif operator == "/":
    print("{} / {} = {}".format(num_1, num_2, (num_1 / num_2)))
elif operator == "+":
    print("{} + {} = {}".format(num_1, num_2, (num_1 + num_2)))
elif operator == "-":
    print("{} - {} = {}".format(num_1, num_2, (num_1 - num_2)))
else:
    print("wrong!!!")

