def wielomian_generator(n):
    return lambda x: sum([(-1)**i * x**(n-i)for i in range(n)])

w5 = wielomian_generator(5)
print(w5(5))
w10 = wielomian_generator(10)
print(w10(5))
