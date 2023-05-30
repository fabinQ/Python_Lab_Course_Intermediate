import functools
import time

def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        print(f'Funkcja "{a_function.__name__}" wykonana w czasie {time_stop - time_start:.2f}')
        return v
    return a_wrapped_function

# @wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v

@wrapper_time
def suma(u):
    sum=0
    u = range(u)
    for i in u:
        sum += get_sequence(i)
    return sum
wrapper_get_sequence = wrapper_time(get_sequence)

print(wrapper_get_sequence(16))
print(suma(16))