age=int(input("enter the age:"))
if (age==5):
    print("go to kindergarten!")
elif(6 <= age) and (age <= 17):
    print("go to grade {}".format(age-5))
elif(age > 17):
    print("go to college")
else:
    print("stay at home")
