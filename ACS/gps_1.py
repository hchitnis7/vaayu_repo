from math import sin, cos, sqrt, atan2, radians
R = 6371.0
while True:
    key = cv2.waitKey(1)
    lat1 = radians(19.044204086907392)
    lon1 = radians(72.8203016154393)
    lat2 = radians(19.0442180633)
    lon2 = radians(72.8202743530)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    print("Result:", distance)
    if key == 27:
        break