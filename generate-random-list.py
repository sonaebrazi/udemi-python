import  random
rand_list=[]
for i in range(5):
    rand_list.append(random.randrange(1,9))
for i in rand_list:
    print("{} : {}".format(rand_list.index(i),i))
