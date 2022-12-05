import math
ckpts = []
"""
def merge(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list

"""
drp_h = int(input("enter the hieght at which the plane was dropped: "))
calc_x = int(input("enter the calculated horizontal distance"))
#assuming our landing zone is (0,0) drop point will be (calc_x, drp_h)
slp = drp_h/calc_x
incln = math.atan(slp)
incln = incln*(180/math.pi)
a_speed = int(input("Enter the speed at which the pada is dropped"))
#assuming that speed is constant
as_y = -1*(a_speed*math.sin(a_speed))
as_x = a_speed*math.cos(a_speed)
c_alt = drp_h
c_dst = calc_x
t = 1
while(True):
    ckpts.append(c_alt)
    print(c_alt)
    if ((t * as_y)<0):
        c_alt = drp_h + (t * as_y)
    else:
        c_alt = drp_h - (t * as_y)
    if(c_alt<5):
        break
    t = t+1
print(ckpts)

