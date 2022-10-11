import numpy
import math
from math import sin, cos, sqrt, atan2, radians

def create_checkpoint(sl1,sl2,dl1,dl2,length):
    # distance = findDistance(sl1,sl2,dl1,dl2)
    distance = 100
    no_checkpoits = distance / (2*length)
    return list(getEquidistantPoints((sl1,sl2),(dl1,dl2),math.ceil(no_checkpoits)))

def getEquidistantPoints(p1, p2, parts):
    return zip(numpy.linspace(p1[0], p2[0], parts+1),numpy.linspace(p1[1], p2[1], parts+1))

def findaltitude(sl1,sl2,dl1,dl2):
    x = sl1 - dl1 # x = distance
    res = (x**2)/880.14
    return res

"""
def findDistance(sl1,sl2,dl1,dl2):
    R = 6371.0
    lat1 = radians(sl1)
    lon1 = radians(sl2)
    lat2 = radians(dl1)
    lon2 = radians(dl2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c * 1000
    return distance
"""