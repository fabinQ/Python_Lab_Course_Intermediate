import math
import numpy as np

argument_list = [round(a,1) for a in np.arange(0,10.1,0.1)]


user_value = input("Podaj zadnie matematyczne: ")

for x in argument_list:
    result = eval(user_value)
    print("{0:7.4f} - dla x {1:4.1f}".format(result, x))

