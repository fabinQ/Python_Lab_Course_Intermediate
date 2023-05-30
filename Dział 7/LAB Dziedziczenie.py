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

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

class SpecialCake(Cake):
    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text


    def show_info(self):
        super().show_info()
        print("occasion:    {}".format(self.occasion.upper()))
        print("shape:        {}".format(self.shape))
        print("ornaments:       {}".format(self.ornaments))
        print("text:       {}".format(self.text))
        print('-$' * 20)

birthday = SpecialCake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', 'birthday', 'cyrcle', 'basketball', 'Happy 23!')
wedding = SpecialCake('Banana Cake', 'cake', 'banana', ['nutella', 'nuts'], 'cream', 'wedding', 'square', '2 person', 'weding time')

# print(birthday.show_info())
# print(wedding.show_info())

for i in SpecialCake.bakery_offer:
    print(i.full_name)
    i.show_info()