import os
import  functools
from datetime import datetime as dt

def path_to_log(name_file):
    if name_file[-4:]==".txt":
        path = os.path.join(os.getcwd(),name_file)
    else:
        path = os.path.join(os.getcwd(),name_file+".txt")
    print(path)
    return path


def CreateFunctionWithWrapper_toLogFile(func_name, LogFilePath):
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(LogFilePath, "a")
            file.write('Function "{}" started at {}.\n'.format(func_name,dt.now().isoformat()))
            file.write('Args function:\n')
            file.write(' '.join("{}".format(i) for i in args))
            file.write('\nKwargs function:')
            if len(kwargs) != 0 :
                file.write("\n")
                file.write(' '.join("{} = {}".format(x,y) for (x,y) in kwargs.items()))
                file.write("\n")
            else: file.write(" Empty\n")
            result = func(*args, **kwargs)
            file.write('Function returned "{}"\n'.format(result))
            file.write('*'*40)
            file.write('\n'*2)
            file.close()
            return result
        return func_with_wrapper
    return CreateFunctionWithWrapper

@CreateFunctionWithWrapper_toLogFile("ChangeSalary", path_to_log("ChangeSalary"))
def ChangeSalary(emp_name, new_salary, is_bonus=True):
    salary =("CHANGING SALARY FOR {} TO {} AS A BONUS {}.".format(emp_name, new_salary, is_bonus))
    # print(salary)
    return salary

@CreateFunctionWithWrapper_toLogFile("CahngePosition", path_to_log("CahngePosition"))
def CahngePosition(emp_name, new_position):
    position = ("CHANGING POSITON FOR {} TO {}.".format(emp_name, new_position))
    # print(position)
    return position


print(ChangeSalary('Johnson', 20000, is_bonus = True))
print(ChangeSalary('Jorge', 20000, True))
print(CahngePosition('Johnson', "Mid Dev"))
print(CahngePosition('Jorge', "Junior Dev"))


