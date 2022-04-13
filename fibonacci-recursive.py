def fibonacci(num):
    if num < 0:
        print("incorrect")
    elif num == 0 :
        return  0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)


number_of_fib_vals = int(input("how many fibonacci values :"))
i = 1
while i <= number_of_fib_vals:
    fib_value = fibonacci(i)
    print(fib_value)
    i += 1