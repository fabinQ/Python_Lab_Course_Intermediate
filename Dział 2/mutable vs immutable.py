# number = 10
# print("Wartość: ", number, "ID zmiennej: ", id(number))
# number += 5
# print("Wartość: ", number, "ID zmiennej: ", id(number))
# print()
#
# text = "Africa"
# print("Wartość: ", text, "ID zmiennej: ", id(text))
# text +=" is hot"
# text = text[:-7]
# print("Wartość: ", text, "ID zmiennej: ", id(text))
# print()
#
# list = [1,2,3]
# print("Wartość list: ", list, "ID zmiennej: ", id(list))
# list.append(4)
# print("Wartość list: ", list, "ID zmiennej: ", id(list))
# print()
#
# list2=list
# print("Wartość list2 : ", list2, "ID zmiennej: ", id(list2))
# list2.append(1)
# print("Wartość list2 : ", list2, "ID zmiennej: ", id(list2))
# print(list,len(list))
# print("==", len(list) == len(list2))
# print("is", list is list2)
# print()
#
# list3=list.copy()
# print("Wartość list : ", list, "ID zmiennej: ", id(list))
# print("Wartość list3 : ", list3, "ID zmiennej: ", id(list3))
# list3.append(5)
# print("Wartość list3 : ", list3, "ID zmiennej: ", id(list3))
#
# # int = immutable - z zastrzeżeniem że jesli + 5 i odejmiemy 5 to interpreter ogarnie że to samo
# # string = immutable
# # lista = mutable

# ZADANIA LAB

days = ['mon','tue','wed','thu','fri','sat','sun']
worksdays = days.copy()
worksdays.pop(5)
worksdays.pop(5)
print(days)
print (worksdays)
print(id(days),id(worksdays))