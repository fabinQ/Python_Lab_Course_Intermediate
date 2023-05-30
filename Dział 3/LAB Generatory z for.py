ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

flight_1 = ((a,b) for a in ports for b in ports)
flight_2 = ((a,b) for a in ports for b in ports if a!=b)
flight_3 = ((a,b) for a in ports for b in ports if a<b)

couter = 0
for start, stop in flight_1:
    print('Lot z {} do {}'.format(start,stop))
    couter+=1
print('Występuje {} lotów.'.format(couter))
print('='*50,'\n')


couter = 0
for start, stop in flight_2:
    print('Lot z {} do {}'.format(start,stop))
    couter+=1
print('Występuje {} lotów.'.format(couter))
print('='*50,'\n')

couter = 0
for start, stop in flight_3:
    print('Lot z {} do {}'.format(start,stop))
    couter+=1
print('Występuje {} lotów.'.format(couter))
print('='*50,'\n')