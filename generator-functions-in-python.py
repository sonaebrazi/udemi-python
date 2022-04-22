def is_prime(num):
    for i in range(2 , num):
        if num % i ==0:
            return False
        return True
def generate_primes(max_number):
    for num1 in range(2 , max_number):
        if is_prime(num1):
            yield num1

primes = generate_primes(50)
print("prime :" , next(primes))
print("prime :" , next(primes))
print("prime :" , next(primes))
print("prime :" , next(primes))
