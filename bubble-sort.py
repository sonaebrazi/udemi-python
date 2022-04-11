import  random
#generating a random list of five values
rand_list=[]
for i in range(5):
    rand_list.append(random.randrange(1,9))
# printing the list of generated numbers
for i in rand_list:
    print(i,end="")
#bubble sort
i=len(rand_list) - 1
while i > 1:
    j=0
    while j < i :
        print("\nis {} > {}".format(rand_list[j],rand_list[j+1]))
        print()
        if rand_list[j] > rand_list[j+1]:
            print("switch")
            temp=rand_list[j]
            rand_list[j]=rand_list[j+1]
            rand_list[j+1]=temp
        else:
            print("don't switch")
        j += 1
        for k in rand_list:
            print(k,end="")
        print()
    print("end of round")
    i = i-1
    for k in rand_list:
        print(k, end="")
    print()
