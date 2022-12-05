import plotter as ptpr
import math
chk_pts[]
drp_h = int(input("enter the hieght at which the plane was dropped: "))
calc_x = int(input("enter the calculated horizontal distance"))
#assuming our landing zone is (0,0) drop point will be (calc_x, drp_h)
slp = drp_h/calc_x
incln = math.atan(slp)
incln = incln*(180/math.pi)
a_speed = int(input("Enter the speed at which the pada is dropped"))
as_y = a_speed*math.sin(a_speed)
as_x = a_speed*math.cos((a_speed))
