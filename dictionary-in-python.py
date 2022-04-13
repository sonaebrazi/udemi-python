customer=[]
while True:
    create_entry = input("Enter customer (Yes or No):")
    create_entry = create_entry[0].lower()
    if create_entry == "n":
        break
    else:
        f_name , l_name = input("enter customer:").split()
        customer.append({"f_name":f_name,"l_name":l_name})
for cust in customer:
    print(cust['f_name'] , cust['l_name'])