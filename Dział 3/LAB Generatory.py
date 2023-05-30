ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

flights1 = ((a,b) for a in ports for b in ports)
flights2 = ((a,b) for a in ports for b in ports if a!=b )
flights3 = ( (start, stop) for start in ports for stop in ports if start < stop)
flights4 = ( (start, stop) for start in ports for stop in ports if ports.index(start) < ports.index(stop))

i=0
while flights1:
    try:
        print(next(flights1))
        i+=1
    except:
        print("StopIteration!")
        print(i)
        break
print('='*50)

i=0
while flights2:
    try:
        print(next(flights2))
        i+=1
    except:
        print("StopIteration!")
        print(i)
        break

i=0
while flights3:
    try:
        print(next(flights3))
        i+=1
    except:
        print("StopIteration!")
        print(i)
        break

i=0
while flights4:
    try:
        print(next(flights4))
        i+=1
    except:
        print("StopIteration!")
        print(i)
        break