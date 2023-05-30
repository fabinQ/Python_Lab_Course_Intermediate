def double(x):
    return 2 * x

def square(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2

number = 8

transformation = [double, square, negative, div2]

tmp_return_value = number

# Mimo że wskazujemy na to samo miejsce w pamięci id() i potem w procesie zmieniamy wartość zmiennej to interpreter robi .copy() zmiennej i nie zmienia oryginału.
# Nie działa to w liście. XD

print(id(number), id(tmp_return_value))

for instruction in transformation:
    tmp_return_value = instruction(tmp_return_value)
    print("{}: tempolar resolut is {}.".format(instruction.__name__,tmp_return_value))
print(number,tmp_return_value)
print(id(number), id(tmp_return_value))

##########################################

print("="*50)

number = 8
transformation = [square, square, div2, double]

tmp_return_value = number

# Mimo że wskazujemy na to samo miejsce w pamięci id() i potem w procesie zmieniamy wartość zmiennej to interpreter robi .copy() zmiennej i nie zmienia oryginału.
# Nie działą to w liście. XD

print(id(number), id(tmp_return_value))

for instruction in transformation:
    tmp_return_value = instruction(tmp_return_value)
    print("{}: tempolar resolut is {}.".format(instruction.__name__,tmp_return_value))
print(number,tmp_return_value)
print(id(number), id(tmp_return_value))
