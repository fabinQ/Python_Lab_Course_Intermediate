import os
import types
import csv
class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):

        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))

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
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)
    ## Propety ale w inny sposób
    # def __get_text(self):
    #     return self.__text
    #
    # def __set_text(self, new_text):
    #     if self.kind == 'cake':
    #         self.__text = new_text
    #     else:
    #         print('>>>>>Text can be set only for cake ({})'.format(self.name))
    #
    # Text = property(__get_text, __set_text, None, 'Text on the cake')
    @property
    def Text(self):
        return self.__text
    @Text.setter
    def Text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))



cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Good luck!')

print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()

cake01.Text = 'Happy birthday!'
cake02.Text = '18'

for c in Cake.bakery_offer:
    c.show_info()


def export_1_cake_to_html(obj, path):
    path = os.path.join(path,obj.name+'.html')
    print(path)
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)
    print('--'*10)
    print()
def export_all_cake_to_html(cls, path):
    path_csv = os.path.join(path[:-14], 'csv_file.csv')
    print(path)
    print(path_csv)
    template = """
            <table border=1>
                 <tr>
                   <th colspan=2>{}</th>
                 </tr>
                   <tr>
                     <td>Kind</td>
                     <td>{}</td>
                   </tr>
                   <tr>
                     <td>Taste</td>
                     <td>{}</td>
                   </tr>
                   <tr>
                     <td>Additives</td>
                     <td>{}</td>
                   </tr>
                   <tr>
                     <td>Filling</td>
                     <td>{}</td>
                   </tr>
            </table>"""
    with open(path, "w") as f:
        for cake in cls.bakery_offer:
            content = template.format(cake.name, cake.kind, cake.taste, ', '.join(cake.additives), cake.filling)
            f.write(content)
    with open(path_csv, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['name', 'kind', 'taste', 'additives', 'filling'])
        for c in cls.bakery_offer:
            writer.writerow([c.name, c.kind, c.taste, ', '.join(c.additives), c.filling])
    print('--'*10)
    print()

def export_this_cake_to_html(self, path):
    path_html = os.path.join(path, self.name.replace(' ','_') + '.html')
    path_csv = os.path.join(path, self.name + '.csv')
    print(path_html)
    print(path_csv)
    template = """
            <table border=1>
                 <tr>
                   <th colspan=2>{}</th>
                 </tr>
                   <tr>
                     <td>Kind</td>
                     <td>{}</td>
                   </tr>
                   <tr>
                     <td>Taste</td>
                     <td>{}</td>
                   </tr>
                   <tr>
                     <td>Additives</td>
                     <td>{}</td>
                   </tr>
                   <tr>
                     <td>Filling</td>
                     <td>{}</td>
                   </tr>
            </table>"""
    with open(path_html, "w") as f:
        content = template.format(self.name, self.kind, self.taste, ', '.join(self.additives), self.filling)
        f.write(content)
    with open(path_csv, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['name', 'kind', 'taste', 'additives', 'filling'])
        writer.writerow([self.name, self.kind, self.taste, ', '.join(self.additives), self.filling])
    print('--'*10)
    print()

print("$%"*20)

 #statistic method
print('statistic method')
path = os.getcwd()
Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake01, path)

 #class method
print('class method')
path = os.path.join(os.getcwd(), 'html_file.html')
Cake.export_all_cakes_to_html = types.MethodType(export_all_cake_to_html,Cake)
Cake.export_all_cakes_to_html(path)

# instance method
print('instance method')
path = os.getcwd()
for c in Cake.bakery_offer:
    Cake.export_this_cake_to_html = types.MethodType(export_this_cake_to_html,c)
    c.export_this_cake_to_html(path)