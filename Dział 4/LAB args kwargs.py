# ZADANIE 1
import os

def calculate_paint(efficency_ltr_per_m2, *args):
    print("*args ", *args)
    print("args ", args)
    print("Suma: ", sum(args))
    litr_farby = efficency_ltr_per_m2 * sum(args)
    return litr_farby

list_of_rooms = [5.3, 6.5, 3]
print(calculate_paint(0.25,*list_of_rooms))

#ZADANIE 2
directory = os.getcwd()
directory = os.path.join(directory, "log_it.txt")

def log_it(directory, *args):
    with open(directory, "a") as f:
        for i in args:
            f.write(i+"\n")

with open(directory, "w") as f:
    f.write("")


log_it(directory,'Starting processing forecasting')
logi = "log1\nlog2\nlog3"
log_it(directory, logi)
log_it(directory, "Error","Not enough data","invoices","2020")
# log_it("log1", "log2", "log3")
print(".... LOG ERROR .....")