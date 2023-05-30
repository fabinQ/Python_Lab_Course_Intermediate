import os

def scantree(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            yield entry
            yield from scantree(entry.path)
        else:
            yield entry

path = os.getcwd()
print('$$$$$$$$$$$$$$$$$$$$$$')
# print(scantree(path))
for i in scantree(path):
    print(i)