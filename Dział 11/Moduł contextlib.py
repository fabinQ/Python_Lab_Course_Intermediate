from contextlib import contextmanager
class Door():

    def __init__(self,where):
        self.where = where

    def open(self):
        print('Open door to the {}'.format(self.where))

    def close(self):
        print('Close door to the {}'.format(self.where))

@contextmanager
def OpenClose(obj):
    # print(obj.where)
    obj.open()
    yield obj
    obj.close()

@contextmanager
def Close(obj):
    # print(obj.where)
    yield obj
    obj.close()

# door1 = Door('hell')
# door2 = Door('paradise')
#
# door1.open()
# time.sleep(1)
# door1.close()

# with OpenClose(Door('next room')) as door3:
#     print('the door to the {}'.format(door3.where))
#     a =2
#     b =3
#     print(a+b)


# with Close(Door('next room')) as door3:
#     door3.open()
#     print('the door to the {}'.format(door3.where))
#     a = 2
#     b = 3
#     print(a + b)

# from urllib.request import urlopen
# import requests
# from contextlib import closing
#
# with closing(requests.get('http://www.kursyonline24.eu')) as page:
#     for line in page:
#         print(line)

# import os
# from contextlib import suppress
# path = os.path.join(os.getcwd(),'data_to_delate.txt')
#
# with suppress(FileNotFoundError):
#         os.remove(path)

from contextlib import redirect_stdout
import os
file = os.path.join(os.getcwd(), 'log.txt')

with open(file, 'w') as file:
    with redirect_stdout(file):
        print("Dupa")
        door1 = Door('somewhere')
        with OpenClose(door1):
            print('the door to the {}'.format(door1.where))
            
