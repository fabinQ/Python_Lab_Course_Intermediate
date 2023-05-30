def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(i+1, options[i][2:]))

    choice = input("Podaj cyfre: ")
    return choice

options = ['1.load data', '2.export data', '3.analyze & predict']
choice = 'x'
while choice:
    choice=DisplayOptions(options)
    if choice:
        try:
            choice_num = int(choice)
            if choice_num >0 and choice_num<len(options):
                print ("Wybrano opcje: {} - {}".format(choice_num, options[choice_num-1][2:]))
                print("Kontynuować? y/n")
                choice=input()
                if choice[:1]=='y':
                    continue
                else:
                    break
            else: print("Nie ma takiej opcji!")
        except:
            try:
                if float(choice):
                    print("Musisz podać cyfre z zakresu 1-3")
            except:
                print('To nie liczba')
    else:
        print("Puste")
        choice='x'