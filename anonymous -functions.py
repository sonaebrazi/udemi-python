sum_1 = lambda x, y: x + y
print("Sum :", sum_1(3, 5))

can_vote = lambda age: " Yes , can vote" if age >= 18 else "No! can't vote"
print(can_vote(13))

pow_list = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
for func in pow_list:
    print(func(4))

attack = {'quick': (lambda: print("Quick Attack")), 'power': (lambda: print("Power Attack")),
          'miss': (lambda: print("Attack Missed"))}
attack['quick']()

import random
attack_key = random.choice(list(attack.keys()))
attack[attack_key]()
