class Dog:
    num_of_dogs = 0
    def __init__(self , name="unknown"):
        self.name = name
        Dog.num_of_dogs += 1

    @staticmethod
    def get_num_of_dogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():
    spot = Dog("spot")
    greg = Dog("greg")
    Dog.get_num_of_dogs()
    spot.get_num_of_dogs()

main()

