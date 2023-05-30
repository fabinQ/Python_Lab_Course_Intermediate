import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
i=1
for combintation in it.permutations(notes,4):
    print('{0:3.0f} {1}'.format(i, combintation))
    i+=1

v = math.factorial(len(notes))/math.factorial(len(notes)-4)
print (v)
input('press enter')
i=0
# for combintation in notes:
#     for combintation2 in notes:
#         for combintation3 in notes:
#             for combintation4 in notes:
#                 i+=1
#                 print(i,combintation,combintation2,combintation3,combintation4)

for combintation in it.product(notes, repeat = 4):
    i+=1
    print('{0:3.0f} {1}'.format(i, combintation))
# print(i)
v = math.pow(len(notes),4)
print (v)