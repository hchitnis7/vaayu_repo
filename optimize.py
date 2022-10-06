import checkpoints as cp

checkpoints = {}
source_lat = 0
destination_log = 0
destination_lat = 0
source_log = 0
path_crossed = []


def findPath(checkpoints):
    while True:
        sub_ranges = []
        plane_coordinates = list(map(float, input("Enter Plane coordinates : ").split()))
        rangee = checkrange(plane_coordinates)
        copied_range = rangee.copy()
        print(copied_range.values())
        for k, v in copied_range.items():
            if plane_coordinates[1] > v[1]:
                print('Move to Left')
                del rangee[k]
                break
            elif plane_coordinates[1] < v[1]:
                print('Move to right')
                del rangee[k]
                break
            elif v[0] == plane_coordinates[0] and v[1] == plane_coordinates[1]:
                print(f'Crossed the {k}')
                del rangee[k]
                break
            elif v[1] == plane_coordinates[1]:
                print('Correct Logitude')
        """
        for i in range(rangee.values()):
            if(plane_coordinates[1] > i[1]):
                print('Move to Slight Left')
                plane_coordinates.pop(i)
                break
            elif(plane_coordinates[1] < i[1]):
                plane_coordinates.pop(i)
                print('Move to Slight Right')
                break
        """


def checkrange(plane_coordinates):
    global checkpoints
    lat = list(checkpoints.values())
    counter = 0
    for i in lat:
        if (i[1] >= plane_coordinates[1] and i[0] >= plane_coordinates[0]):
            print(f'Next Checkpoint is : Checkpoint{counter + 1} , Coordinates {i[0], i[1]}')
            sub_checkpoints = cp.create_subCheckpoints(lat[counter - 1], i)
            return sub_checkpoints
        counter += 1


source_lat = float(input("Enter Your Latitude : "))
source_log = float(input("Enter Your Longitude : "))

destination_lat = float(input("Enter Destination Latitude : "))
destination_log = float(input("Enter Destination Longitude : "))

midpoints = cp.createCheckpoints(source_lat, source_log, destination_lat, destination_log)
checkpoints = cp.sortmidpoints(midpoints, source_lat, source_log, destination_lat, destination_log)
findPath(checkpoints)

"""
19.12813570468522, 72.83101128264134
19.152575105680402, 72.84457582236722
3.04
"""

"""
19.29328426200737, 72.85724878458772
19.295754777030616, 72.84874155988547
"""