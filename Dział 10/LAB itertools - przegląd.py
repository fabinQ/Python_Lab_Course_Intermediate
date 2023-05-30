import itertools


def get_factor(number):
    factor = []
    for i in range(1,round(number/2)+1):
        if number % i ==0:
            factor.append(i)
    return factor

def check_if_has_dividers(x):
    for i in range(2,x):
        if x%i==0:
            return True
    else:
        return False

candidate_list = list(range(1,500))
candidate_list= itertools.filterfalse(lambda x:x%2>0, candidate_list)
filtered_list = itertools.filterfalse(lambda x: x!= sum(get_factor(x)),candidate_list)
for i in filtered_list:
    print(i, get_factor(i))
# for i in candidate_list:
#     factor = get_factor(i)
#     # result = list(itertools.filterfalse(lambda x:not(sum(factor)==i),factor))
#     # if len(result)>0:
#     #     print(sum(result), ' a jej dzielniki to ', result)
#     if sum(factor)==i:
#         print(i, ' a jej dzielniki to ', factor)

prime_numbers = itertools.islice(itertools.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)),10)
print(list(prime_numbers))