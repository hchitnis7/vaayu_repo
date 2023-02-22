from math import sin, cos, sqrt, atan2, radians
R = 6371.0

lat1 = radians(19.043988843258266)
lon1 = radians( 72.82094179449601)
lat2 = radians(19.04401579329567 )
lon2 = radians( 72.82097030495828)
dlon = lon2 - lon1
dlat = lat2 - lat1
a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
c = 2 * atan2(sqrt(a), sqrt(1 - a))
distance = R * c * 1000
print("Result:", distance)
