import random


def random_with_sum (number_of_values, asserted_sum):
    trial = 0
    while True:
        numbers = []
        trial +=1
        for i in range(0, number_of_values):
            numbers.append(random.randrange(1,101))
        if sum(numbers) == asserted_sum:
            yield (trial, numbers)
            trial = 0


for i in range(1,11):
    tbs = next(random_with_sum(3,100))
    print('Lp. {}. no. of tries {}, numebers whitch sum is 100 : {}, {}, {}.'.format(i, tbs[0], tbs[1][0], tbs[1][1], tbs[1][2]))