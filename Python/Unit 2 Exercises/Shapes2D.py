from math import atan2, cos, sin, pi

class Point2D:
    """
    Point 2D Class
        Each object is point in the x-y plane.
        Coordinates are 2 floating point numbers x and y.
    """
    __precision = 10 

    def __init__(self, x=0, y=0):
        """
        Point2d Constructor
            Default value is (0, 0)
        """
        self.__r  = (x**2 + y**2)**0.5
        self.__th = atan2(y, x)
    
    def getX(self):
        """
        Get x coordinate.
        """
        return round(self.__r * cos(self.__th), Point2D.__precision)
    
    @property
    def x(self):
        return self.getX()
    
    def getY(self):
        """
        Get y coordinate.
        """
        return round(self.__r * sin(self.__th), Point2D.__precision)

    @property
    def y(self):
        return self.getY()
    
    def translateX(self, x):
        """
        Translate in the x direction
        """
        nx = x + self.getX()
        ny = self.getY()
        self.__r  = (nx**2 + ny**2)**0.5
        self.__th = atan2(ny, nx)

    def translateY(self, y):
        """
        Translate in the y direction
        """
        nx = self.getX()
        ny = y + self.getY()
        self.__r  = (nx**2 + ny**2)**0.5
        self.__th = atan2(ny, nx)

    def getRadius(self):
        """
        Get radius of equivalent polar coordinate.
        """
        return round(self.__r, Point2D.__precision)

    def getTheta(self):
        """
        Get angle of equivalent polar coordinate.
        """
        return round(self.__th, Point2D.__precision)

    def extend(self, r):
        """
        Increase radius by a factor of r.
        """
        self.__r  *= r
        

    def rotate(self, th):
        """
        Increase angle by th radians.
        """
        self.__th += th


    def getDistance(self, other):
        """
        Return distance between two points.
        """
        dx = self.getX() - other.getX()
        dy = self.getY() - other.getY()
        return (dx**2 + dy**2)**0.5
    
    def getSlope(self, other):
        """
        Return the slope of the line containing both points.
        """
        dx = self.getX() - other.getX()
        dy = self.getY() - other.getY()
        # Avoid division by zero
        if dx == 0:
            return float('inf') if dy > 0 else float('-inf')
        return dy/dx
    
    def getMidpoint(self, other):
        """
        Return a Point2D object with coordinates 
        equal to the midpoint of the line segment
        connecting self and other.
        """
        dx = self.getX() + other.getX()
        dy = self.getY() + other.getY()
        return Point2D(dx/2.0, dy/2.0)

from copy import deepcopy

class Shape2D:
    """
    Shape 2D Class
        Each object is shape in the x-y plane.
        A shape in this context is defined as a set of points
        that are connected one after the other, where the 
        last point is connected to the first point as well.
    """
    def __init__(self, points=[]):
        """
        Shape2D Constructor
            Defaults to no points yet.
        """
        self._points = points
        self._nsides = len(self._points)

    def set_points(self, new_points):
        self._points = new_points
        self._nsides = len(self._points)

    def clear_points(self):
        self._points = []
        self._nsides = 0

    def get_points(self):
        # Uses deep copy to ensure returned copy
        # does not modify original list.
        return deepcopy(self._points)
    
    def print_points(self):
        # Prints each point as (x, y)
        for p in self.get_points():
            print(f"({p.getX()}, {p.getY()}), ", end="")
        print()
        return deepcopy(self._points)
    

    def copy(self):
        # Returns a copy of the shape
        return Shape2D(self.get_points())

    def add_point(self, new_point):
        self._points.append(new_point)
        self._nsides = len(self._points)

    def get_allX(self):
        return [p.getX() for p in self.get_points()]
    
    def get_allY(self):
        return [p.getY() for p in self.get_points()]

    def translateX(self, x):
        """
        Translate all points to the x direction
        """
        for i in range(self._nsides):
            self._points[i].translateX(x)

    def translateY(self, y):
        """
        Translate all points to the y direction
        """
        for i in range(self._nsides):
            self._points[i].translateY(y)
    
    def rotate(self, th):
        """
        Rotates all points about the shape's center (centroid)
        """
        # Calculate centroid
        if self._nsides == 0:
            return
        sum_x = sum(p.getX() for p in self._points)
        sum_y = sum(p.getY() for p in self._points)
        cx = sum_x / self._nsides
        cy = sum_y / self._nsides

        # Translate all points to origin
        for p in self._points:
            p.translateX(-cx)
            p.translateY(-cy)
        
        # Rotate points
        for p in self._points:
            p.rotate(th)
            
        # Translate back
        for p in self._points:
            p.translateX(cx)
            p.translateY(cy)
        return

    def scale(self, r):
        """
        Scales all points about the shape's center (centroid)
        """
        # Calculate centroid
        if self._nsides == 0:
            return
        sum_x = sum(p.getX() for p in self._points)
        sum_y = sum(p.getY() for p in self._points)
        cx = sum_x / self._nsides
        cy = sum_y / self._nsides

        # Translate all points to origin
        for p in self._points:
            p.translateX(-cx)
            p.translateY(-cy)
        
        # Scale points
        for p in self._points:
            p.extend(r) # Point2D.extend scales from origin
            
        # Translate back
        for p in self._points:
            p.translateX(cx)
            p.translateY(cy)
        return

    def getPerimeter(self):
        """
        Returns the perimeter of the shape
        """
        perim = 0
        for i in range(self._nsides):
            # Corrected typo: getdistance -> getDistance
            perim += self._points[i-1].getDistance(self._points[i])
        return perim

class Triangle(Shape2D):
    def __init__(self, points=[]):
        """
        Triangle Constructor
            Defaults to [(0,0), (1,0), (0,1)].
        """
        # Call super constructor to set points
        super().__init__()
        self.set_points(points)
        

    def set_points(self, points):
        if len(points) == 3:
            self._points = points
        else:
            print("Only Three Points Allowed, using default values")
            self._points = [Point2D(0,0), Point2D(1,0), Point2D(0,1)]
        self._nsides = 3


class Square(Shape2D):
    def __init__(self, side=1, center=(0,0)):
        """
        Square Constructor
            Defaults to Unit Square
            centered at the origin.
        """
        # Create base points for a side=1 square at (0,0)
        h = 0.5 # half-side
        self._points =  [Point2D(h, h), Point2D(-h, h), \
                         Point2D(-h, -h), Point2D(h, -h)]
        self._nsides = 4
        self._center = (0.0, 0.0) # Initial center
        
        # Scale the square (at origin) to the correct side length
        self.scale(side) 
        
        # Translate to the final center position
        self.translateX(center[0])
        self.translateY(center[1])
        self._center = center # Store the final center
       
    def scale(self, r):
        """
        Increases square side length by a factor of r.
        Center of the square is maintained.
        """
        # Get current center
        cx, cy = self._center

        # Translate points to origin
        for p in self._points:
            p.translateX(-cx)
            p.translateY(-cy)
        
        # Scale points (relative to origin)
        for p in self._points:
            p.extend(r)
            
        # Translate back to center
        for p in self._points:
            p.translateX(cx)
            p.translateY(cy)
        
    def get_center(self):
        """
        Returns the center of the square.
        """
        return self._center
    
    def set_center(self, c):
        """
        Sets the center of the square.
        """
        new_cx, new_cy = c
        old_cx, old_cy = self._center
        
        # Calculate translation delta
        dx = new_cx - old_cx
        dy = new_cy - old_cy
        
        # Use Shape2D's translate methods
        self.translateX(dx)
        self.translateY(dy)
        
        # Update stored center
        self._center = c

    def copy(self):
        """
        Returns a new Square object with the same
        points and center.
        """
        new_square = Square() # Create a dummy square
        new_square.set_points(self.get_points()) # Copy points
        new_square._center = self.get_center() # Copy center
        return new_square


import matplotlib.pyplot as plt
# May require `python -m pip install -U matplotlib`

class Drawing:
    def __init__(self, shape_list=[]):
        temp = [issubclass(type(x), Shape2D) for x in shape_list]
        if False in temp:
            # Check if any element of shape_list is not a Shape2D
            print("Invalid list of shapes, creating empty list instead.")
            self.__shape_list=[]
        else:
            # Create a list member that would store the given shapes
            # Fixed: Use the provided list
            self.__shape_list = list(shape_list)
        
    def show(self, a=1):
        fig, ax = plt.subplots()
        # Plot each Shape2D in a figure

        for shape in self.__shape_list:
            x_list = shape.get_allX()
            y_list = shape.get_allY()
            ax.plot(x_list + [x_list[0]], y_list + [y_list[0]], alpha=a)
        
        # Set equal aspect ratio for correct shape display
        ax.set_aspect('equal', adjustable='box')
        plt.show()
    
    def add_shape(self, shape):
        if not (issubclass(type(shape), Shape2D)):
            print("Invalid Shape2D")
            return
        # Insert shape to list of Shape2D
        self.__shape_list.append(shape)

    def clear(self):
        # Remove all the Shape2D
        self.__shape_list=[]
    
# Check if this file is being run directly
# We wrap the test code in a main() function and call it
def main():
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
    print("\n--- Task 1 ---")
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
    print("\n--- Task 2 ---")
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
    print("\n--- Task 3 ---")
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
    print("\n--- Task 4 ---")
    d6 = Drawing()
    # Use the default triangle: (0,0), (1,0), (0,1)
    base_tri = Triangle() 
    
    n_shapes = 100
    r = 0.5 # Initial radius/scale
    th = 0.0 # Initial angle
    
    dr = 0.07 # Radius increase per step
    dth = pi / 6.0 # Angle increase per step (30 degrees)
    d_rot = pi / 12.0 # Rotation of triangle itself
    
    for i in range(n_shapes):
        # Copy the base shape
        tri_copy = base_tri.copy()
        
        # 1. Scale it
        tri_copy.scale(r * 0.5) # Scale based on radius
        
        # 2. Rotate it (orientation)
        tri_copy.rotate(th + d_rot * i) 
        
        # 3. Translate it to position
        x = r * cos(th)
        y = r * sin(th)
        tri_copy.translateX(x)
        tri_copy.translateY(y)
        
        # Add to drawing
        d6.add_shape(tri_copy)
        
        # Update spiral parameters
        r += dr
        th += dth
        
    d6.show()

# Standard Python construct to run main() if the file is executed
if __name__ == "__main__":
    main()