import csv
import os

with open(os.path.join(os.getcwd(), 'dane/data.csv'), newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))
    # print(next(csvfile))
    # print(next(csvfile))
    # print(next(csvfile))
    # print(next(csvfile))
    # print(next(csvreader))
    # print(next(csvreader))
    # print(next(csvreader))
    # print(next(csvreader))
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            print('end of file')
            break
        except Exception:
            print('Error')
            break