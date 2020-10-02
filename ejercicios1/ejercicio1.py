import math

# h height between the X axis and the first edge (proposed height in meters)
h = 2

# l length of each mechanical arm 1 meter
l1 = 1
l2 = 1

# q inclination angles, q2 has the opposite angle to q1 so it is negative (angles in degrees)
q1 = math.radians( 45 ) 
q2 = math.radians( -45 )

# x1 distance between Y axis, and the end point of l1 in meters
x1 = l1 * math.cos( q1 ) 
# x2 distance between Y axis, and the end point of l2 in meters
x2 = l2 * math.cos( q2 )
# x sum of distances from x1 to x2 in meters
x = x1 + x2

# final distance on the X axis in meters
print ( 'x = ' + str(x) + ' m' )

# y1 distance between X axis, and the end point of l1 without taking into account the height in meters
y1 = l1 * math.sin( q1 )
# y2 distance between X axis, and the end point of l2 without taking into account the height in meters
y2 = l2 * math.sin( q2 )
# y sum of distances from y1 with y2 and the height in meters
y = h + y1 + y2

# final distance on the Y axis in meters
print ( 'y = ' + str(y) + ' m' )