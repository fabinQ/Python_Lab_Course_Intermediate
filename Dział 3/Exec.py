var_x = 10

source = '''
var_y = 0
for i in range(var_x):
    print ("-"* i)
    var_y +=1
'''
# Funckja excec poddaje interpretacji wartość wyrażenie czyli wykonuje kod
exec(source)

# Jeśli stworzymy puste środowisko globals w zbiorze eval nie bedzie wiedzieć czym są var_x, var_y
globals = globals().copy()
# globals.clear()

source = input("Możesz sprawdzić var_x, var_y: ")
print(source)
print(eval(source, globals))
