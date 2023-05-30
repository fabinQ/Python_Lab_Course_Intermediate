import os
import zipfile
import requests


class FileFromWeb:
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        response = requests.get(self.url, stream=True)
        with open(self.tmp_file, mode='wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# url_zip = 'https://www.eminitrader.pl/2018/alfabet-tradingu/'
url_zip = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip'
# path = 'D:\\data.zip'
path = os.path.join(os.getcwd(), 'data.zip')


with FileFromWeb(url_zip, path) as f:
    print(zipfile.is_zipfile(f.tmp_file))
    if zipfile.is_zipfile(f.tmp_file):
        with zipfile.ZipFile(f.tmp_file, mode='r') as z:
            path_zip_dir = os.path.join(os.path.dirname(path), 'unzipdir')
            if not os.path.exists(path_zip_dir):
                os.mkdir(path_zip_dir)
                os.chdir(path_zip_dir)
            else:
                os.chdir(path_zip_dir)
            for x in z.namelist():
                a_file = x
                print(a_file)
                # z.extract(a_file,path_zip_dir, pwd=None)
                z.extract(a_file, '.', pwd=None)      # jeśli wpiszemy kropke to wypakuje nam do cwd - robi to za pomoca os.chdir
