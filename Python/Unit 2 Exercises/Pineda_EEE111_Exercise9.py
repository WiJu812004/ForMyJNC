from math import atan2, cos, pi, sin, sqrt
class Point2D:

    total = 0 

    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)
        Point2D.total += 1

    def translateX(self, x):
        self.x += x

    def translateY(self, y):
        self.y += y

    def getRadius(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def getTheta(self):
        return atan2(self.y, self.x)

    def extend(self, r):
        r = self.getRadius()
        theta = self.getTheta()
        r *= r
        self.x = r * cos(theta)
        self.y = r * sin(theta)

    def rotate(self, th):
        r = self.getRadius()
        theta = self.getTheta() + th
        self.x = r * cos(theta)
        self.y = r * sin(theta)

    def getDistance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def getSlope(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        if dx == 0:
            return float('inf')
        return dy / dx

    def getMidpoint(self, other):
        midpoint_x = (self.x + other.x) / 2.0
        midpoint_y = (self.y + other.y) / 2.0
        return Point2D(midpoint_x, midpoint_y)
    
"""
Constructor Tests
"""

p0 = Point2D()
p1 = Point2D(3, 4)
p2 = Point2D(-1.0, 1.0)

print(f"p0: ({p0.x}, {p0.y})")
print(f"p1: ({p1.x}, {p1.y})")
print(f"p2: ({p2.x}, {p2.y})")
print(f"Point2D.total = {Point2D.total}")
print()

""" 
Translate Tests
"""
p0.translateX(12.0)
p1.translateX(-6)
p0.translateY(5.0)
p2.translateY(-1)

print(f"p0: ({p0.x}, {p0.y})")
print(f"p1: ({p1.x}, {p1.y})")
print(f"p2: ({p2.x}, {p2.y})")
print(f"Point2D.total = {Point2D.total}")
print()

""" 
Radius-Theta Tests
"""
print(f"p0: {p0.getRadius()} angle({p0.getTheta()})")
print(f"p1: {p1.getRadius()} angle({p1.getTheta()})")
print(f"p2: {p2.getRadius()} angle({p2.getTheta()})")
print()

""" 
Extend-Rotate Tests
"""
p0.extend(2.5)
p1.rotate(pi/2.0)
p2.rotate(-pi/4.0)
print(f"p0: {p0.getRadius()} angle({p0.getTheta()})")
print(f"p0: ({p0.x}, {p0.y})")
print(f"p1: {p1.getRadius()} angle({p1.getTheta()})")
print(f"p1: ({p1.x}, {p1.y})")
print(f"p2: {p2.getRadius()} angle({p2.getTheta()})")
print(f"p2: ({p2.x}, {p2.y})")
print()

""" 
Point-Point Tests
"""
p0.getDistance(p1)
print(f"p0.getDistance(p1): {p0.getDistance(p1)}")
p1.getDistance(p2)
print(f"p1.getDistance(p2): {p1.getDistance(p2)}")
p1.getDistance(Point2D())
print(f"p1.getDistance(Point2D()): {p1.getDistance(Point2D())}")

p0.getSlope(p1)
print(f"p0.getSlope(p1): {p0.getSlope(p1)}")
p1.getSlope(p2)
print(f"p1.getSlope(p2): {p1.getSlope(p2)}")
p1.getSlope(Point2D())
print(f"p1.getSlope(Point2D()): {p1.getSlope(Point2D())}")

p3 = p0.getMidpoint(p1)
print(f"p3: ({p3.x}, {p3.y})")
p4 = p1.getMidpoint(p2)
print(f"p4: ({p4.x}, {p4.y})")
p5 = p1.getMidpoint(Point2D())
print(f"p5: ({p5.x}, {p5.y})")
print()