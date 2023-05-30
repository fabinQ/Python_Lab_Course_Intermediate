def CreateFunction(kind = '+'):
    print(kind)
    sorce = '''
def f(arg = [],*args):
    result = 0
    args = [*arg, *args]
    print(args)
    for i in args:
        result {}= i
    return result'''.format(kind)
    exec(sorce,globals())
    return f
print(globals())
arg = list(range(1,11))
f_add = CreateFunction('+')
print(f_add(arg,11,12))
print(globals())

f_subs = CreateFunction('-')
print(f_subs([],11,12))
print(globals())
