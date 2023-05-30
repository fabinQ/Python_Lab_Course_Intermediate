import os
import requests
import chardet

def gen_get_files(dir):
    for i in os.listdir(dir):
        path = os.path.join(dir,i)
        if os.path.isfile(path):
            yield path

def gen_get_file_lines(filename):
    try:
        with open(filename, 'rb') as f:
            result = chardet.detect(f.read())
        encoding = result['encoding']
        print('#' * 20)
        print(os.path.basename(filename))
        print('#' * 20)
        with open(filename, 'r', encoding=encoding) as f:
            for line in f:
                yield line.rstrip('\n')
            print('*' * 50)
    except (UnicodeDecodeError, IsADirectoryError, FileNotFoundError) as e:
        print(f"Nie udało się otworzyć pliku {filename}. Błąd: {e}")

def check_webpage(url):
    print(url)
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

##############################################

path= os.path.join(os.getcwd(), 'links_to_check')
try:
    os.mkdir(path)
except:
    print('pass')
    pass

with open(os.path.join(path,'pl.txt'), 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open(os.path.join(path,'com.txt'), 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')


path= os.path.join(os.getcwd(), 'links_to_check')
for i in gen_get_files(path):
    for j in gen_get_file_lines(i):
        print(check_webpage(j))
