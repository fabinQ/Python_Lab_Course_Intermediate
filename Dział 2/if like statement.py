import os

def CountWord(path):
    with open(path, 'r') as f:
        content = f.read()  #Funkcja read zwraca zawartość pliku
        # print("Funckja read zwroaca wartość:\n",content)

        content_split= content.split() #Split robi z tego tabele, łatwo sprawdzić ilość słów.
        # print("Funckja split zwroaca wartość:\n",content_split)

        word_count = len(content_split)
        # print("Długość tabeli czyli ilość słów: ",word_count)

        length_lines = len(' '.join(content_split)) #usuwa linie i sprawdza długość
        # print(' '.join(content_split))
        # print("Ilość znaków ze spacjami: ",length_lines)
    return content, word_count, length_lines

def badanie_txt(a):
    print(f'Zawartość tego pliku to:\n{a[0]}')  #f umośliwia danie {} czyli zmiwnnej do tekstu.
    print('\nW pliku jest {} słów, a tekst składa się z {} znaków.'.format(a[1],a[2]))  #tak samo .format

########################################################################

tabela = []
zawartosc = ''
path = os.getcwd()
default_file = "services.txt"

choice = input("Chcesz wprowadzić nowy plik czy domyśny plik - %s" % default_file + " Nowy/Domyślny? ")

# #NOWY
if choice[:1].upper() == "N":
    lorem_ipsum = input("Podaj nazwe pliku txt ")

    if lorem_ipsum[-4:] == ".txt":
        lorem_ipsum = lorem_ipsum[0:-4]

    lorem_ipsum=lorem_ipsum.rstrip(" ")
    print('')
    lorem_ipsum = lorem_ipsum + ".txt"
    path = os.path.join(path, lorem_ipsum)

    if os.path.isfile(path):  # Jeśli plik istnieje odczytuje zawartość i liczy ilość znaków.
        a = CountWord(path)
        badanie_txt(a)

    else:  # Jeśli plik nie istnieje tworzy otwiera, write wpisuje tekst
        open(path, "x")
        lorem_ipsum = open(path, mode='w')
        lorem_ipsum.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor \n"
                          "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis \n"
                          "nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \n"
                          "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu \n"
                          "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in \n"
                          "culpa qui officia deserunt mollit anim id est laborum.")
        lorem_ipsum.close()

        a = CountWord(path)
        badanie_txt(a)

if choice[:1].upper() == "D":  # Jesli ma być default to otwiera path + default
    path = os.path.join(path, default_file)

    if os.path.isfile(path):  # Jesli plik jest otwiera i dla kazdej linii rozdziela na \n, tworzy sie "dupa","" dlatego jest [0]
        a = CountWord(path)
        badanie_txt(a)

        # for i in open(path):
        #     # print(i)
        #     print(i.split('\n')[0])
        #     tabela.append(i.split('\n')[0])  # Dodaje do tabeli
        # print('Liczba elementów ', len(tabela))
    else:
        print("\nPlik nie istnieje\nTworzę plik.......\n")
        print("Plik został utworzony w %s" % path)
        open(path, 'x').write('dupa1\ndupa2\ndupa3\ndupa4\ndupa5\ndupa6\ndupa7\ndupa8\ndupa9')
