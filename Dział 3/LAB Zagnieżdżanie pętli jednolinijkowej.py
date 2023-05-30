ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

flights1 = [(a,b) for a in ports for b in ports]
flights2 = [(a,b) for a in ports for b in ports if a!=b ]
flights3 = [ (start, stop) for start in ports for stop in ports if start < stop]
flights4 = [ (start, stop) for start in ports for stop in ports if ports.index(start) < ports.index(stop)]


# print(flights2)
# print(len(flights2))
# print(len(flights3))
# print('#'*50)
print(flights3)
print("Flight 3: ",len(flights3))
print('#'*50)
print(flights4)
print("Flight 4: ",len(flights4))
# tab = []
# for i in flights4:
#     print("Szukam:", i)
#     for n in flights3:
#         if i[0] == n[0] or i[0] == n[1]:
#             if i[0] == n[0] and i[1] == n[1]:
#                 print("Mamy!1")
#                 print(i,n[0],n[1])
#                 tab.append((i,n))
#             if i[0] == n[1] and i[1] == n[0]:
#                 print("Mamy!2")
#                 print(i,n[1],n[0])
#                 tab.append((i,n))
#             else:pass
# print(tab)
# print(len(tab))
