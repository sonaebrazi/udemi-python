money = float(input("money : "))
interest_rate = float(input("interest rate: ")) * 0.01
for i in range(10):
    money = money + (money * interest_rate)
print("investment after 10 years : ${:.2f}".format(money))
