import os

a= "Pharma A, Vitamin C,100\nDrugstore XYZ,Penicilin, 20, pills\nDrugstore ABC,Aspirin,60\nPharma X,Montelukast,10"
path = os.path.join(os.getcwd(), 'dane/data.csv')
with open(path, 'w+') as file:
    file.write(a)
