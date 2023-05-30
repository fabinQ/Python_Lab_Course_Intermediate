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

    def __str__(self):
        return "King: {}, name: {}, additives: {}".format(self.kind, self.name, ', '.join(self.additives))

    def __iadd__(self, other):
        additives = self.additives
        if type(other) is list:
            additives.extend(other)
            return Cake(self.name,self.kind,self.taste,additives,self.filling)
        elif type(other) is str:
            additives.append(other)
            return Cake(self.name,self.kind,self.taste,additives,self.filling)
        else:
            raise Exception("Type is not inpementation")

cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')

print(cake01)

cake01+=['posypka', 'lukier']
print(cake01)

# cake01+=3