import os
import itertools as it

def scantree(path):
    # print(path)
    for entry in os.scandir(path):

        if entry.is_dir():
            # print('direction '.upper(), end = '')
            yield entry
            yield from scantree(entry.path)
        else:
            yield entry


print('$$$$$$$$$$$$$$$$$$$$$$')
listing =[]
path = os.path.join(os.getcwd(),'')


for i in scantree(path):
    listing.append(i)


for i in listing:
    print('DIR {}'.format(i.name) if i.is_dir() else 'FILE {}'.format(i.name))

print('*'*30)
data = sorted(listing, key= lambda x:x.is_dir())
for is_file, elementss in it.groupby(data, key= lambda x:x.is_file()):
    print('FILE {}'.format(len(list(elementss))) if is_file else 'DIR {}'.format(len(list(elementss))))