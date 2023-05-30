import os, urllib.request
data_dir = os.getcwd()
path = []

# Tworzenie folderu
try:
    os.mkdir("../Strony", )
except:
    pass

#dodaje do scieżki nazwe folderu Strony
data_dir = os.path.join(data_dir, "../Strony")

#lista ze słownikami stron
pages = [
    { 'name': 'getcwd',      'url': 'https://www.tutorialspoint.com/python/os_getcwd.htm'},
    { 'name': 'operacje na katalogach', 'url': 'https://forum.pasja-informatyki.pl/455704/import-os-w-pythonie' },
    { 'name': 'film',       'url': 'https://www.filmweb.pl/film/C%27mon+C%27mon-2021-850352'} ]
pages.append({'name':'info',   'url':'https://wp.pl'}) # eksperymentalnie dodany słownik

#Pętla towrzy liste słowników ze scieżki +nazwa pliku i adres url
for i in pages:
    path.append({'path':os.path.join(data_dir,i['name']), 'url': i['url']})
# print(path)

#Pętla pobiera z listy path strony
for i in path:
    try:
        urllib.request.urlretrieve(i['url'],i['path']+'.html')
        print(f'Pobieram stronę {i["path"]}')
    except:
        print("Nieoczekiwany błąd ze stroną {}\n ERROR BAD GATEWAY".format(i['url']))
        break
else:print("Wszytko git mordeczko")

# # Przypomnienie o słownikach
# dict1 = {'key1': 'napis', 'key2': 123, 'key3': ['1', '2', '3']}
# # dict1['key2'] = dict1['key2'] - 100
# # dict1['key2'] = dict1['key2'] - int(dict1['key3'][0])
#
# print(dict1)
# print(len(dict1))
# print(dict1.items())
# print(dict1.keys())
# print(dict1.values())
#
# dict2 = {'key2': 1}
# dict1.update(dict2) #updejtuje o dict 2 - jeśli key istnieje aktualizuje a jeśli nie ma dodaje
# print(dict1)