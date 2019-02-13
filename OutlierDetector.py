#!/usr/bin/python3
#encoding:utf-8

from scipy.spatial import distance
import numpy as np
import CSVIO

class OutlierDetector(object):
    def __init__(self, database):
        self.database = database
        self.distances = []

    def apply(self):
        distan = []
        counter = 0
        for point in self.database:
            for element in self.database:
                distan.append(distance.euclidean(point, element))
            distan = np.array(distan)
            self.distances.append([distan.mean(), counter])
            counter += 1
            distan = list()
        self.distances.sort(reverse=True)
        return self.distances


rg = OutlierDetector(CSVIO.CSVIO("dataset.csv", ignore_class=True, delimiter=',', type_dados='double').read())
ls = rg.apply()


for element in ls:
    print(str(element))