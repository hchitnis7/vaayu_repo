import checkpoint as cp
import plotter as ptpr

checkpoints = []
copied_checkpoint = []
x = []
y = []

def checkPath(checkpointss):
    global copied_checkpoint, checkpoints, x, y
    copied_checkpoint = checkpointss
    while True:
        plane_coordinates = list(map(float, input("Enter Plane coordinates : ").split()))
        checkrange(plane_coordinates)
        counter = 0
        for i in range(1, len(copied_checkpoint)):
            if plane_coordinates[1] > checkpoints[i][1]:
                dist_log = abs(plane_coordinates[1] - checkpoints[i][1])
                dist_lat = abs(plane_coordinates[0] - checkpoints[i][0])
                if (dist_log > 6.56168):
                    print('New Route')
                    checkpoints = cp.create_checkpoint(plane_coordinates[0], plane_coordinates[1], destination_lat, destination_log, plane_length)
                    print(checkpoints)
                    ptpr.plot_chkpts(checkpoints)
                    checkPath(checkpoints)

                print(f'diff {dist_lat} in straight & {dist_log} in Left ')
                checkpointss.pop(i)
                break
            elif plane_coordinates[1] < checkpointss[i][1]:
                dist_log = abs(plane_coordinates[1] - checkpointss[i][1])
                dist_lat = abs(plane_coordinates[0] - checkpointss[i][0])
                if (dist_log > 6.56168):
                    print('New Route')
                    checkpoints = cp.create_checkpoint(plane_coordinates[0], plane_coordinates[1], destination_lat, destination_log, plane_length)
                    print(checkpoints)
                    ptpr.plot_chkpts(checkpoints)
                    checkPath(checkpoints)

                print(f'diff {dist_lat} in straight & {dist_log} in Right ')
                break
            elif checkpointss[i][0] == plane_coordinates[0] and checkpointss[i][1] == plane_coordinates[1]:
                print(f'Crossed the Checkpoint{i} : {i}')
                checkpointss.pop(i)
                break
            elif checkpointss[i][1] == plane_coordinates[1]:
                print('Correct Logitude')
                checkpointss.pop(i)
                break


def checkrange(plane_coordinates):
    global checkpoints, copied_checkpoint
    counter = 0
    for i in checkpoints:
        if (i[1] >= plane_coordinates[1] and i[0] >= plane_coordinates[0]):
            print(f'Next Checkpoint is : Checkpoint{copied_checkpoint.index(i) + 1} , Coordinates {i[0], i[1]}')
            break
        counter += 1
    ptpr.plot_chkpts(checkpoints)



source_lat = 0
source_log = 0
destination_lat = 100
destination_log = 100
""" source_lat = 21.99999826405264
source_log = 24.99999574717875
destination_lat = 22.000034324111308
destination_log = 25.002421134682407 """
plane_length = 2

checkpoints = cp.create_checkpoint(source_lat, source_log, destination_lat, destination_log, plane_length)
ptpr.plot_chkpts(checkpoints)
# print(checkpoints)
checkPath(checkpoints)