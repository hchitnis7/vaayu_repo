import numpy

def getEquidistantPoints(p1, p2, parts):
    return zip(numpy.linspace(p1[0], p2[0], parts+1),
               numpy.linspace(p1[1], p2[1], parts+1))
pts = list(getEquidistantPoints((19.044191409886484,72.820267417274642), (19.0442180633,72.8204743530), 19))
print(pts)