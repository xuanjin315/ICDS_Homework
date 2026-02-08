class Point:
    """A class to represent a two-dimensional point"""

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
        if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
            raise TypeError
        self.x = x
        self.y = y

    def get_x(self):
        """Return the x-coordinate."""
        return self.x

    def get_y(self):
        """Return the y-coordinate."""
        return self.y
     

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
        return self.x==point2.x and self.y==point2.y
        # TODO: compare self.x/self.y with point2.x/point2.y
       


if __name__ == "__main__":
    p1 = Point(2, 3)
    p2 = Point(5, 7)
    print(round(p1.distance(p2), 2))  

    p1.move(-2, 1)
    print(p1.get_x(), p1.get_y())     
    print(p1.equals(Point(0, 4)))     
    