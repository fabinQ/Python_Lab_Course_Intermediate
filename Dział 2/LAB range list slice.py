color_list = ["red", "orange", "green", "violet", "blue", "yellow", "white"]
dane = list(range(0,11))
# y = []
n = 2
i = 1

indeks_o = []
indeks_o2 = []
indeks_z = []
indeks_z2 = []

def color_mode(color_list, n):
    return color_list[:n]


# n = int(input("Podaj liczbe wykresów: "))
# color = color_mode(color_list,n)
# print(color)

while i < len(color_list)+1:
    print(color_mode(color_list,i))
    i+=1

# for x in dane:
#     y.append(2 * x + 3)
# print(y)

print("."*50)

###################################

def slice (tekst, indeks1,indeks2):
    print("DEFINCJA: ", tekst[indeks1+1:indeks2])
    tekst_slice = tekst[indeks1:indeks2+1]
    tekst = tekst.split(tekst_slice)
    tekst_slice = ''
    for _ in tekst:
        tekst_slice =tekst_slice + _
    return tekst_slice

#Podstawowy z jednym nawiasem ()
tekst2 = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."
for _ in enumerate(tekst2):
    if str(_[1]) == "(" or str(_[1]) == ")":
        if str(_[1])=="(":
            indeks_o2.append(_[0])
        if str(_[1])==")":
            indeks_z2.append(_[0])
print(indeks_o2,indeks_z2)

print(slice(tekst2,indeks_o2[0],indeks_z2[0]))



print("."*50)
# #Zaawansowany z szukaniem indeków nawiasów        NIEDOKOŃCZONE       POMYSŁ - JESLI ZNAJDZIE (ZAPISUJE INDEKS POTEM SZUKA "(" LUB ")" I JEŚLI BĘDZIE "(" ODEJMUJE -1 OD LICZNIKA AŻ ZNAJDZIE ")"
# drugi pomysł to ze for moze przyjąć 2 wartości for x,y in index_marge
# tekst = "Korporacja (z łac. corpo – (ciało, ratus – szczur;) pol. ciało szczura) – organizacja, (która pod przykrywką prowadzenia biznesu włada dzisiejszym światem). Wydawać się może utopijnym miejscem realizacji pasji zawodowych. (W rzeczywistości (jednak) nie jest wcale tak kolorowo.) Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."
#
# for _ in enumerate(tekst):
#     if str(_[1]) == "(" or str(_[1]) == ")":
#         if str(_[1])=="(":
#             indeks_o.append(_[0])
#         if str(_[1])==")":
#             indeks_z.append(_[0])
# print(indeks_o,indeks_z)
# n = 0
# i = 1
# n = 1
# indeks_margin = [0 for i in range(len(indeks_o))]
# while i<len(indeks_o):
#     while n <len(indeks_z):
#         print("otwarty ",indeks_o[i]," zamknięty ",indeks_z[n-1])
#         print(indeks_o[i] < indeks_z[n-1])
#         if indeks_o[i] < indeks_z[n-1]:
#             print("Tutaj",indeks_o[i], indeks_z[n-1])
#             # indeks_margin[i-1] = [indeks_o[i-1],indeks_z[i-1]]
#         n+=1
#     i+=1
# print("Połączony ",indeks_margin)





