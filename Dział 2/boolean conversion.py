# isOk = ["","Dupa",0,1,0.0,-0.1,True,False]
# print("Variable isOK: ", isOk, type(isOk))
# for i in isOk:
#     if i:    #sprawdza czy: 1. Jeśli bool to czy jest True.
#         print(i,type(i)," TRUE")    # 2. Jeśli string to sprawdza czy jest pusty.
#     else:print(i, " False")  # 3. Jeśli int to sprawdza czy 0 czy 1.
#                          # 4. Jeśli float to sprawdza czy 0.0 czy inna.
#                          # 5. Jeśli lista jest pusta to False, chyba że odwołujemy się do konkretnej pozycji w listy wtedy 0/1 puste lub nie

# listOfErrors = [100,101,102]
# print("ListOfErrors: ", listOfErrors, type(listOfErrors))
# if listOfErrors:
#     print("TRUE")
# # mozna tez tak zrobić
# listOfErrors = [100,101,102]
# print("ListOfErrors: ", listOfErrors, type(listOfErrors))
# if len(listOfErrors)>0:
#     print("TRUE",len(listOfErrors))

# with open(r'C:\Users\Maciej\iCloudDrive\Python\udemy Srednio zaawansowany\services.txt') as f:
#     line = f.readline()
#     print('.....................')
#     while( line ):
#         print(line)
#         line = f.readline() #readline czyta kolejne linie z f

#   SKRYPT LAB
data = [0,0,0]
print ("1. load data\n2. export data\n3. analyze&predict")
# choice = True
while (data):
    choice = input("Numerek: ")
    if not choice:
        print("Puste, podaj numer! ")
    if (choice.isnumeric()):
        if choice.isdecimal():
            numer=int(choice)
            if numer:
                if numer == 1:
                    print("1. load data")
                    print("..............")
                    print(data)
                if numer == 2:
                    print('2. export data')
                    print("..............")
                if numer == 3:
                    print('3. analyze&predict')
                    print("..............")
                else:
                    print("Podaj poprawny numer")
            if not numer:
                print("Zero ziom")
    else:
        try:
            float(choice)
            print("Podaj cyfre 1,2 lub 3")
        except:
            print("Podaj liczbe!")



