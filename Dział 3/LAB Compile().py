import math
import timeit
import matplotlib.pyplot as plt

def plot(argument_list, results_list):
    plt.plot(argument_list, results_list)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Graph of {}".format(i))
    plt.show()


# Ustawiamy czas, liste formuł, i liste argumentów
time_start = timeit.default_timer()
formulas_list = [
     "abs(x**3 - x**0.5)",
     "x**3 - x**0.5",
     "abs(math.sin(x) * x**2),"
     "math.sin(x) * x**2"
     ]

argument_list = []
for i in range (1000000):
    argument_list.append(i/10)

# Dla każdej wartosci w form oblicza z listy arg. jesli nie zrobimy pre-kompilacji to wykonanie
# tego zajmue ok. 58 sek., jesli przed obliczaniem wykonamy prekompilacje compile(i,'','eval/exec/simple')
# to zajamie nam to ok. 2 sek. bo nie musi dla miliona argumentów na nowo kompilować.
# ( results_list.append(eval(i / compile_arg)) )

for i in formulas_list:
    results_list = []
    print("Wyrażenie: {}".format(i))
    compile_arg = compile(i, 'błąd prekompilacji', 'eval')
    for x in argument_list:
        results_list.append(eval(compile_arg))
    print("Min: {}, Max {}".format(min(results_list),max(results_list)))
    # plot(argument_list, results_list)

time_stop = timeit.default_timer()
print("Czas wykonania: {}".format(time_stop-time_start))