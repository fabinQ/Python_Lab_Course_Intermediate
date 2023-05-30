class HtmlCM():

    def __init__(self):
        pass

    def __enter__(self):
        self.__number = int(input('Podaj ilość wierszy: '))
        self.__description =[]
        for i in range(1,self.__number+1):
            self.__description.append(input('Podaj opis: '))

        print('\n<TABLE>')
        for i, element in enumerate(self.__description):
            print(" <TR>\n     <TD>{}</TD><TD>{}</TD>\n </TR>".format(i+1, element))

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('</TABLE>')

with HtmlCM():
    pass