import requests
import os
import shutil


def save_url_to_file(url, file_path):

    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
# url = 'https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14880700#overview'
dir = os.getcwd()
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
        save_url_to_file(url, tmpfile_path)
        shutil.copy(tmpfile_path, file_path)
except Exception as e:
    print("Error! Problem with ",e)
else:
    print("Succes!")
finally:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
        print('Usunięto plik {}'.format(os.path.basename(tmpfile_path)))
