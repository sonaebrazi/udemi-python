one_to_ten = range (1 , 11)
def double_num(num):
    return num * 2
print(list(map(double_num , one_to_ten)))

print(list(map((lambda x: x*3) , one_to_ten)))

a_list = list(map((lambda x , y : x+y) ,  [1 ,2 , 3],[1 ,2 , 3]))
print(a_list)