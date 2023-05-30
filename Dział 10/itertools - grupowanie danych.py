import itertools as it
import os

file_path = os.path.join(os.getcwd(), 'data.txt')
data =[]
with open(file_path,'r') as file:
    for line in file:
        element = line.rstrip('\n').split(': ')
        data.append({'type':element[0], 'action':element[1]})
for i in data:
    print(i)
# print(i for i in data)
# for i in data:
#     print(i)
# print(data[2]['type'])
print('***********************')

data = sorted(data, key= lambda x:x['type'])
for key, elementss in it.groupby(data, key= lambda x:x['type']):
    print('KEY {} GROUP {}, number of action {}'.format(key, list(elementss), len(list(elementss))))