import pickle
import os
import glob

class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []
    def __init__(self, name, kind, taste, additives, filling, price, weight, gluten_free, text):
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.price = price
        self.weight = weight
        self.__gluten_free = gluten_free
        if self.kind == 'cake':
            self.__text = text

        else:
            self.__text = ''
            # print('You can not make text on this type of cake')
        Cake.bakery_offer.append(self.name)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:    {}".format(self.kind))
        print("Taste:   {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling: {}".format(self.filling))
        if self.__gluten_free is True:print("GLUTEN FREE!")
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, *args):
        self.additives.extend(args)
    def __get_text(self):
       return self.__text
    def  __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else: print('Cannot change text on cake.')

    Text = property(__get_text,__set_text,None,'Dupa')

    def save_to_file(self, path):
        path_file = os.path.join(path, self.name+'.bakery')
        print('save_to_file'.upper(), path_file)
        with open(path_file, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        print("\nread_from_file\n".upper())
        with open(path, "rb") as f:
            while True:
                try:
                    new_cake = pickle.load(f)
                except:
                    break
                cls.bakery_offer.append(new_cake)
        print('new_cake: ', new_cake)
        print('bakery_offer: ', Cake.bakery_offer)
        print('len: ', len(Cake.bakery_offer))
        return new_cake

    @staticmethod
    def get_bakery_files (path):
        files = glob.glob(os.path.join(path,'*.bakery'))
        return files


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream',20,0.9,True,'Happy birthday!')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '',30,1.2,False,'Happy birthday!')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '',40,0.8,False,'Happy birthday!')
mazuerek = Cake('mazurek', 'cake', 'sweet', ['kruszonka', 'syrop'],'z malinami', 40, 1,False,'Happy birthday!')
apple_pie = Cake('apple_pie', 'pie', 'apple', ['apple','flour','biscuit'], 'with apple', 30, 0.7,False,'Happy birthday!')
banana_cake = Cake('banana_cake', 'cake', 'chocolade', ['banana','flour','chocolade'], 'with cream', 25, 0.6,False,'Happy birthday!')
blueberry_pie = Cake('blueberry_pie', 'pie', 'vanilla', [],'', 70, 1.2,True,'Happy birthday!')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa',20,0.5,True,'Happy birthday!')

# cake01._Cake__text = 'dupala'
# print("TU",cake01._Cake__text)
# cake01.Text = 'Dupa'
# print("TU2",cake01.Text)
# print(Cake.bakery_offer)

path = os.getcwd()

cake01.save_to_file(path)
cake02.save_to_file(path)
cake03.save_to_file(path)

cake05 = Cake.read_from_file(os.path.join(os.getcwd(), 'Vanilla Cake.bakery'))
cake05.show_info()

files = Cake.get_bakery_files(path)
for file in files:
    Cake.read_from_file(file)



# print('Today in our offer:')
# for i in Cake.bakery_offer:
#     print('{} - {} mian taste: {} with aditives of '.format(i.name, i.kind, i.taste), end="")
#     for x in i.additives:
#         print('{} '.format(x), end="")
#     print(', filled with {}. This {}, weighs {} kilograms, and its price is {} zloty'.format(i.filling, i.kind, i.weight, i.price))
#     print('\nShow info:')
#     i.show_info()
#     print('=='*10,'\n')
# print('&'*50)
# cake03.__gluten_free = True
# del cake03.__gluten_free
# delattr(cake03,'__gluten_free')
# cake03._Cake__gluten_free = True

# print(Cake.bakery_offer)
# print('isinstance :',isinstance(cake01,Cake))
# print('type :',type(cake03) is Cake)
# print('vars: \n\t{}\n\t{}'.format(vars(cake01),vars(Cake)))
# print('dir:\n\t{}\n\t{}'.format(dir(cake01),dir(Cake)))

# print("gluten free?")
# print(cake03._Cake__gluten_free )

# blueberry_pie.set_filling('cream')
# blueberry_pie.show_info()
# print('=='*10,'\n')
#
# apple_pie.set_filling('cream')
# apple_pie.show_info()
# print('=='*10,'\n')
#
# mazuerek.add_additives('dynia','czekolada')
# mazuerek.show_info()
# print('=='*10,'\n')
#
# blueberry_pie.add_additives('dynia','czekolada')
# blueberry_pie.show_info()
# print('=='*10,'\n')
#
# print('Today in our offer:')
# cake02.set_filling('cream')
# cake02.show_info()
# print('=='*10,'\n')
#
# cake03.add_additives('coco powder', 'coconuts')
# cake03.show_info()
# print('=='*10,'\n')

