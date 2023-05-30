class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def add_additives(self, additives):
        self.additives.extend(additives)

class NoDuplicates:
    def __init__(self,func):
        self.func = func

    def __call__(self,cake ,additives):
        # print(cake.additives)
        # print(additives)
        no_duplicate_list = [i for i in additives if i not in cake.additives]
        print(no_duplicate_list)
        self.func(cake,no_duplicate_list)

cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')

@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)

add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()

add_extra_additives(cake01, ['strawberries', 'sugar-flowers', 'chocolate', 'nuts','dupa'])
cake01.show_info()