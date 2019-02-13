import numpy as numpy

class CSVIO(object):
    def __init__(self, pathfile, ignore_class=False, delimiter=',', type_dados = 'double'):
        self.path = pathfile
        self.ignore_class = ignore_class
        self.data = list()
        self.delimiter = delimiter
        self.type_dados = type_dados
    
    def read(self):
        with open(self.path, 'r') as file:
            data = []
            for line in file:
                data.append(line.split(self.delimiter))
            
            if self.ignore_class == True:
                for element in data:
                    element.remove(element[-1])
                    self.data.append(element)
            else:
                self.data = data

            if self.type_dados == 'double':
                data = self.data
                self.data = []
                for element in data:
                    element = [float(p) for p in element]
                    self.data.append(element)

            return self.data
