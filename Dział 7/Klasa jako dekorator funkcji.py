import random

class MemoryClass:
    list_of_already_selected_items = []

    def __init__(self, funct):
        print('>>init mordo')
        self.funct = funct

    def __call__(self, list):
        print('>>call mordo')
        items_not_selected = [i for i in list if i not in MemoryClass.list_of_already_selected_items]
        print('+-- selecting only from a list of ', items_not_selected)
        item = self.funct(items_not_selected)
        print(item)
        MemoryClass.list_of_already_selected_items.append(item)
        return item
cars = ['Opel', 'VW', 'BMW', 'Mazda', 'Porsche', 'Audi', 'Mercedes', 'Toyota', 'Fiat', 'Mazda', 'Peugeot','Ford']
@MemoryClass
def SelectedTodayPromotion(list_of_cars):
    return random.choice(list_of_cars)
@MemoryClass
def SelectedTodayShow(list_of_cars):
    return random.choice(list_of_cars)

@MemoryClass
def SelectedFreeAccessories(list_of_cars):
    return random.choice(list_of_cars)

print('Promotion: ',SelectedTodayPromotion(cars))
print('Show: ',SelectedTodayShow(cars))
print('Free accessories: ',SelectedFreeAccessories(cars))
