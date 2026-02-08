
class Point:
    """A class to represent a two-dimensional point with operator overloading"""

    def __init__(self, x=0, y=0):
        """
        Initialize a point.

        Parameters
        ----------
        x : int or float, optional
            x-coordinate (default 0)
        y : int or float, optional
            y-coordinate (default 0)
        """
        # TODO: store x and y as attributes on self
        if not isinstance(x,(float, int)) or not isinstance(y,(float,int)):
            raise TypeError
        self.x=x
        self.y=y

    def __add__(self, other):
        """
        Operator overloading for + (Point + Point).

        Returns
        -------
        Point
            A new Point whose coordinates are the sum of self and other.
        """
        if isinstance(other,Point):
            new_x=self.x+other.x
            new_y=self.y+other.y
        elif isinstance(other,(tuple,list)):
            new_x=self.x+other[0]
            new_y=self.y+other[1]
        else:
            raise TypeError
        return Point(new_x,new_y)

    def __sub__(self, other):
        """
        Operator overloading for - (Point - Point).

        Returns
        -------
        Point
            A new Point whose coordinates are the difference between self and other.
        """
        if isinstance(other,Point):
            new_x=self.x-other.x
            new_y=self.y-other.y
        elif isinstance(other,(tuple,list)):
            new_x=self.x-other[0]
            new_y=self.y-other[1]
        else:
            raise TypeError
        return Point(new_x,new_y)
    
    def get_x(self):
        """Return the x-coordinate."""
        return self.x

    def get_y(self):
        """Return the y-coordinate."""
        return self.y
    
    def equals(self, point2):
        """
        Return True if two points have exactly the same coordinates.

        Parameters
        ----------
        point2 : Point

        Returns
        -------
        bool
        """
        return abs(self.x-point2.x)<1e-9 and abs(self.y-point2.y)<1e-9
     

    def move(self, dx, dy):
        """
        Translate the point in place by (dx, dy).

        Parameters
        ----------
        dx : int or float
        dy : int or float
        """
        # TODO: update self.x and self.y by dx and dy
        if not isinstance(dx,(float,int)) or not isinstance(dy,(float, int)):
            raise TypeError
        self.x=self.x+dx
        self.y=self.y+dy

    def distance(self, point2):
        """
        Compute Euclidean distance to another point.

        Parameters
        ----------
        point2 : Point

        Returns
        -------
        float
            The Euclidean distance between self and point2.
        """
        if not isinstance(point2,Point):
            raise TypeError
        
        dx = self.x - point2.x
        dy = self.y - point2.y
        return (dx**2 + dy**2) ** 0.5
       


    def __eq__(self, other):
        """
        Operator overloading for == (Point == Point).

        Returns
        -------
        bool
            True if self and other have the same coordinates.
        """
        if not isinstance(other,Point):
            raise TypeError
        return abs(self.x-other.x)<1e-9 and abs(self.y-other.y)<1e-9

    def __str__(self):
        """
        Return a string representation of the Point.
        """
        # TODO: return something like "(x, y)"
        return f"x={self.x},y={self.y}"

    __repr__ = __str__  # For convenience in interactive sessions


if __name__ == "__main__":
    p1 = Point(2, 3)
    p2 = Point(5, 7)

    print(round(p1.distance(p2), 2))  
    p1.move(-2, 1)
    print(p1)                         

    p3 = p1 + (1, 1)
    print(p3)                         

    p4 = p3 + Point(2, -1)
    print(p4)                         

    p5 = Point(3.0 + 1e-12, 4.0 - 5e-12)
    print(p4 == p5)                   
    print(p4.equals(p5))   