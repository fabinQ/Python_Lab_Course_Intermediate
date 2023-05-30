import timeit
import functools
time_start = timeit.default_timer()

def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args,**kwargs):
        time_start = timeit.default_timer()
        result = func(*args,**kwargs)
        time_stop = timeit.default_timer()
        print("Wrapper time {}".format(time_stop-time_start))
        return result
    return func_with_wrapper


def double(x):
    return 2 * x

def square(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2

@CreateFunctionWithWrapper
def generate_values(how, x_table):
    list = ["KONIEC."]
    for x in x_table:
        for f in how:
            print("{} : {}".format(f.__name__, f(x)))
        print('-' * 10)
    return list

x_table = list(range(90001))
function = [double, square, negative, div2]
print(generate_values(function, x_table)[0])

time_stop = timeit.default_timer()
print("Czas wykonania :{}".format(time_stop-time_start))