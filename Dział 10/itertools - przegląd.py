import itertools
import operator

# # itertools.accumulate.(iterable, [func])  przyjmuje dane iterable np. liste oraz funkcje
# na których ma te dane przeliczyć
#
#
# data = [1, 2, 3, 4, 5]
# result = itertools.accumulate(data, operator.mul) # mul to mnożenie, moży kolejne elementy listy
# for each in result:
#     print(each)
#
# print('-'*100)
#
# data = [1, 2, 13, 4, 5]
# result = itertools.accumulate(data, max) # max zwraca max
# for each in result:
#     print(each)

# # itertools.count(start=0, step =1)
#
# for i in itertools.count(10,3):
#     print(i)
#     if i > 20:
#         break


# # itertools.cycle(iterable) przechodzi nieskończoną ilość razy przez dane
#
# month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# for i in itertools.cycle(month):
#     print(i)

# # itertools.chain(*iterables)
#
# color_baisic = ['red', 'yellow','blue']
# color_mix = ['green','violet','orange']
# result = itertools.chain(color_baisic,color_mix)
# for i in result:
#     print(i)

# # itertools.compress(data, selectors) zwraca te wartosci które mają True slecector nie musi byc tak długi
#
# cars = ['toyota','vw','bmw','audi','volvo']
# selector_car = [True,False,False,True,True]
# result = itertools.compress(cars,selector_car)
# for i in result:
#     print(i)

# # itertools.dropwhile(warunek który ma byc spełniony, iterable) opuszcza dopóki nie osiągnie warunku.
# # 1 i 0 na koncu spełnia warunek bo 5 była wcześniej
#
# data = [1,2,3,4,5,6,7,8,9,10,1,0]
# result = itertools.dropwhile(lambda x:x<5,data)
# for i in result:
#     print(i)

# # itertools.filterfalse(warunek, iterable) zwraca wartosci odrzucone
#
# data = [1,2,3,4,5,6,7,8,9,10,1,0]
# result = itertools.filterfalse( lambda x:x<5, data)
# for i in result:
#     print(i)

# # itertools.islice(data, start, stop)
#
# month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# result = itertools.islice(month,6,8)
# for i in result:
#     print(i)

## itertools.product(data1, data2) iloczyn kartezjański kazdy z każdym
#
# spades = ['Heart','Tiles','Clovers','Pikes']
# figures = ['Ace','King','Queen','Jack','10','9']
# result = itertools.product(spades, figures)
# for i in result:
#     print(i)

## itertools.repeat('co ma powtórzyć', 6) co i ewentualnie ile razy ma powtórzyć
#
# result = itertools.repeat('dupa', 6)
# for i in result:
#     print(i)

## itertools.starmap(operator.add, data) musi miec specjalny operator
#
# data = [(1,2),(3,4),(5,6),(7,8),(9,10),(1,0)]
# result = itertools.starmap( operator.add, data)
# for i in result:
#     print(i)

# # itertools.takewhile(warunek który ma byc spełniony, iterable) bierze dopóki nie osiągnie warunku.
# # 1 i 0 na koncu nie spełnia warunek bo 5 była wcześniej
#
# data = [1,2,3,4,5,6,7,8,9,10,1,0]
# result = itertools.takewhile(lambda x:x<5,data)
# for i in result:
#     print(i)

# # itertools.tee(iterable, n=2) ułatwiacz życia iteruje iteratory, domyslnie n=2
#
# cars = ['toyota','vw','bmw','audi','volvo']
# cars1, cars2 = itertools.tee(cars)
# for each in cars1:
#     print(each)
# print('-'*50)
# for each in cars2:
#     print(each)

## itertools.zip_longest(*iterable, fillvalue=None)
#
# month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# plan = ['busy','busy','free','busy','busy','free','busy','busy','free']
# result = itertools.zip_longest(month,plan,fillvalue='unknown')
# for i in result:
#     print(i)