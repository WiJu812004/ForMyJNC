import Shapes2D
from math import pi

print("Shape Constructor")
s1 = Shape2D([Point2D(1,0), Point2D(0,0), Point2D(0,1)])
print(s1)
print()

print("Add/Set Point")
s1.add_point(Point2D(1,1))
s1.add_point(Point2D(2,2))
s1.add_point(Point2D(3,3))
print()

print("Get/Set/Clear Points")
print(s1.get_points())
s1.print_points()
s1.set_points([Point2D(2,0), Point2D(0,0), Point2D(0,2)])
s1.print_points()
print(s1.clear_points())
s1.print_points()
print()

print("Get X/Y")
s1.set_points([Point2D(2,2), Point2D(2,-2), Point2D(-2,-2), Point2D(-2,2) ])
print("x:", s1.get_allX())
print("y:", s1.get_allY())
d1 = Drawing()
d1.add_shape(s1)
d1.show()
print()

print("Just Translating the Shape")
tri = Triangle([Point2D(-1,-1/3), Point2D(0,2/3), Point2D(1,-1/3)])
d2 = Drawing()
d2.add_shape(tri.copy())
tri.translateX(5)
d2.add_shape(tri.copy())
tri.translateY(4)
d2.add_shape(tri.copy())
tri.translateX(-3)
d2.add_shape(tri.copy())
tri.translateY(-2)
d2.add_shape(tri.copy())
d2.show(0.5)

print("Rotating and Translating the Shape")
tri = Triangle()
d3 = Drawing()
d3.add_shape(tri.copy())
tri.translateX(2)
tri.rotate(pi/12.0)
d3.add_shape(tri.copy())
tri.rotate(pi/6.0)
d3.add_shape(tri.copy())
tri.rotate(pi/3.0)
d3.add_shape(tri.copy())
d3.show(0.5)

""" 
Task 1
Implement Square with Variable Side Length
Translation rotation should work as well
"""
sq1 = Square()
sq2 = Square(2)
d4 = Drawing()
d4.add_shape(sq1.copy())
d4.add_shape(sq2.copy())

sq1.translateX(4)
sq2.translateX(-4)
d4.add_shape(sq1.copy())
d4.add_shape(sq2.copy())

sq1.translateY(4)
sq2.translateY(-4)
sq1.rotate(-pi/6)
sq2.rotate(pi/6)
d4.add_shape(sq1.copy())
d4.add_shape(sq2.copy())
d4.show()

""" 
Task 2
Implement Square with Variable Center
copy, get_center, and set_center should also work
"""
sq3 = Square(4, (2, 2))
sq4 = sq3.copy()
sq4.set_center((-1, -1))

print("sq3.get_center(): ", sq3.get_center())
print("sq4.get_center(): ", sq4.get_center())

d5 = Drawing()
d5.add_shape(sq3.copy())
d5.add_shape(sq4.copy())
d5.show()

""" 
Task 3
Implement Square with Variable Center
translate and rotate should work
"""

sq3.translateX(8)
sq4.translateX(-8)
d5.add_shape(sq3.copy())
d5.add_shape(sq4.copy())

sq3.translateY(8)
sq4.translateY(-8)
sq3.rotate(pi/4)
d5.add_shape(sq3.copy())
d5.add_shape(sq4.copy())

sq3.scale(0.5)
sq4.set_center((-4, 4))
d5.add_shape(sq3.copy())
d5.add_shape(sq4.copy())

print("sq3.get_center(): ", sq3.get_center())
print("sq4.get_center(): ", sq4.get_center())

d5.show()

""" 
Task 4
Implement your own drawing with at least 
100 unique shapes. You may use/implement
other subclasses if you wish. Feel free 
to modify Drawing.show() to control colors.
"""

