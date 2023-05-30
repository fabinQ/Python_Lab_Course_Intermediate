import timeit
start_time = timeit.default_timer()

import os

def file_menager(file_to_process):
    with open(file_to_process, 'r') as file_to_process:
        file_to_process = file_to_process.read()
    return file_to_process

'''
Notka:
files_to_process = [
    r"os.getcwd().__add__('\math_sin_square.py'), # W metodzie eval działa, ale nie w funkcji - co jest dziwne.
    os.getcwd() + '\math_square_root.py'          # Takie cos działa i jest od razu rozumiane przez program - nie trzeba robić .join
    ]

Co ciekawe nie trzeba zmieniać \ na / żeby działało na macOS
'''

files_to_process = [
    os.getcwd() + '/math_sin_square.py',
    os.getcwd() + '/math_square_root.py'
    ]
for _ in files_to_process:
    x = file_menager(_)
    exec(x)

end_time = timeit.default_timer()
print("Czas wykonania: ", end_time - start_time, "sekund.")