class Sum:
    @staticmethod
    def get_sum(*args):
        sum_1 = 0
        for i in args:
            sum_1 += i
        return sum_1
def main():
    print("sum:",Sum.get_sum(2,4,6,8,10))
main()