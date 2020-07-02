
from datetime import datetime
import datetime


import codecs
import functools

open = functools.partial(codecs.open, encoding='utf-8')


class Points:
    def __init__(self, path, path2, encoding='utf-8'):
        self.path = path
        self.path2 = path2
        self.encoding = encoding
        self.create_time = datetime.datetime.now()
        print('Время запуска кода: {}'.format(self.create_time))

    def __enter__(self):
        self.file = open(self.path)
        self.file2 = open(self.path2)
        self.list_txt = self.file.read()  
        self.list_txt2 = self.file2.read()  
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        self.file.close()
        print('Файл 1 закрыт')
        self.file.close()
        print('Файл 2 закрыт')
        self.end_time = datetime.datetime.now()
        print('Время окончания работы кода: {}'.format(self.end_time))
        print('Время выполнения: {}'.format(self.end_time - self.create_time))


with Points('points.txt', 'graphs.txt') as points:
    list_points = points.list_txt.splitlines()   
    dict_points = {}
    for line in list_points:
        line = line.split(' ')
        dict_points[line[0]] = line[1:]

    for keys, values in dict_points.items():
        print('Точка: {} имеет следующие координаты: {}'.format(keys, values))

    list_graphs = points.list_txt2.splitlines()
    dict_graphs = {}
    for line in list_graphs:
        line = line.split(' ')
        dict_graphs[line[0]] = line[1:]

    for keys, values in dict_graphs.items():
        print('Точка {} проходит через данные пути: {}'.format(keys, values))


