import numpy
import math
from math import sin, cos, sqrt, atan2, radians


def getEquidistantPoints(p1, p2, parts):
    return zip(numpy.linspace(p1[0], p2[0], parts+1),
               numpy.linspace(p1[1], p2[1], parts+1))


R = 6371.0
lat1 = radians(19.044191409886484)
lon1 = radians(72.820267417274642)
lat2 = radians(19.0442180633)
lon2 = radians(72.8204743530)
dlon = lon2 - lon1
dlat = lat2 - lat1
a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))
distance = R * c * 1000
n = math.floor(distance)-2
print("distance :", distance)
print("Number of points: ",n)
pts = list(getEquidistantPoints((19.044191409886484,72.820267417274642), (19.0442180633,72.8204743530), n))
print(pts)
