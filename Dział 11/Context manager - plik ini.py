import os

class ini_line:

    def __init__(self, path):
        print('__init__')
        print('*'*50,'\n')
        self.path = path
        self.parameters = {}
        self.read_from_disk()

    def read_from_disk(self):
        print('read_from_disc')
        if os.path.isfile(self.path):
            with open(self.path) as file:
                for line in file:
                    dic = tuple(line.replace('\n','').split('='))
                    print('dic "{}","{}"'.format(dic[0],dic[1]))
                    self.parameters[dic[0]] = dic[1]
            print(self.parameters.values())
        print('*'*50,'\n')

    def read_parametr(self, key):
        print('read_parametr')
        if key in self.parameters.keys():
            return self.parameters[key]
        else:
            return None
        print('*' * 50, '\n')

    def write_parametr(self,key,value):
        print('write')
        print(key, value)
        self.parameters[key] = value
        print('*' * 50, '\n')

    def save_on_disk(self):
        print('save')
        with open(self.path, 'w') as file:
            for key, value in self.parameters.items():
                print(key,value)
                file.writelines('{}={}\n'.format(key,value))
        print('*' * 50, '\n')

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save_on_disk()
        pass
        # return self

print('PIERWSZY')
ini = ini_line(os.path.join(os.getcwd(), 'data.ini'))
ini.write_parametr('par4', '5')
ini.save_on_disk()
print('^'*60)

print('DRUGI')
ini2 = ini_line(os.path.join(os.getcwd(), 'data.ini'))
print(ini2.parameters)
print(ini2.read_parametr('parametr 1'))
print(ini2.read_parametr('parametr 2'))
print('^'*60)

print('TRZECI')
with ini_line(os.path.join(os.getcwd(), 'data.ini')) as ini3:
    print(ini3.parameters)
    print(ini3.read_parametr('parametr 1'))
    print(ini3.read_parametr('parametr 2'))