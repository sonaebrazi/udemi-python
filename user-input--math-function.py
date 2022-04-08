miles=int(input("enter miles:"))
klmeters=miles * 1.60934
print("it is: ",klmeters,"kilometers")
print("{} miles equals {} kilometers".format(miles,klmeters))

name = input("whats your name? \n")
print("hello", name)

num_1, num_2 = input("enter 2 numbers : ").split()
num_1 = int(num_1)
num_2 = int(num_2)
sum = num_1 + num_2
diff = num_1 - num_2
product = num_1 * num_2
quotient = num_1 / num_2
remainder = num_1 % num_2
print("{}+{}={}".format(num_1, num_2, sum))
print("{}-{}={}".format(num_1,num_2,diff))
print("{}*{}={}".format(num_1,num_2,product))
print("{}/{}={}".format(num_1,num_2,quotient))
print("{}%{}={}".format(num_1,num_2,remainder))
