while True:
    try:
         num=int(input("please enter a number :"))
         break
    except ValueError:
        print("yu didnt enter a number!")
    except:
        print("an unknown error occured!!")
print("thanks")