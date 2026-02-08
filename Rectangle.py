# Task: Implement a Rectangle class with area, perimeter, scaling,
# equality check, and string representation.
# Do NOT change class name or method names.

class Rectangle:
    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        Parameters
        ----------
        width : int or float (must be > 0)
        height : int or float (must be > 0)
        """
        # TODO: validate inputs (numbers > 0)
        # TODO: assign to self.width and self.height
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("width and height must be numbers")

        if width <= 0 or height <= 0:
            raise ValueError("width and height must be > 0")
        self.width=width
        self.height=height
        
    def area(self):
        """Return the area of the rectangle."""
        # TODO
        output=self.width*self.height
        return output

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # TODO
        output=2*(self.width+self.height)
        return output

    def scale(self, k):
        """
        Scale the rectangle in place by factor k.

        Parameters
        ----------
        k : int or float (must be > 0)
        """
        # TODO: update self.width and self.height
        if not isinstance(k, (int,float)):
            raise TypeError("k must be a number")
        if k<0:
            raise ValueError("k must be>0")
        self.height=k*self.height
        self.width=k*self.width
       

    def scaled(self, k):
        """
        Return a NEW Rectangle scaled by factor k.
        Must not modify the original object.

        Parameters
        ----------
        k : int or float (must be > 0)
        """
        # TODO: return a new Rectangle instance
        if not isinstance(k, (int,float)):
            raise TypeError("k must be a number")
        if k<=0:
            raise ValueError("k must be>0")
        
        new_width=k*self.width
        new_height=k*self.height
        return Rectangle(new_width,new_height)
    
    def __eq__(self, other):
        """
        Compare two rectangles for equality.

        Returns True if width and height are equal
        within a small tolerance.
        """
        # TODO
        if not isinstance(other, Rectangle):
            return False
        return (abs(self.width-other.width)<1e-9 and abs(self.height-other.height)<1e-9)
    
            
            

    def __str__(self):
        """
        Return a string representation of the rectangle,
        e.g., 'Rectangle(w=3, h=4, area=12)'
        """
        # TODO
        return f"Rectangle(w={self.width}, h={self.height}, area={self.area()})"

    __repr__ = __str__


if __name__ == "__main__":
    # Sample usage (for testing after you implement the methods)
    r1 = Rectangle(3, 4)
    print(r1.area())        # Expected: 12
    print(r1.perimeter())   # Expected: 14
    print(r1)               # Expected: Rectangle(w=3, h=4, area=12)

    r2 = r1.scaled(0.5)
    print(r1)               # r1 should stay Rectangle(w=3, h=4, area=12)
    print(r2)               # r2 should be Rectangle(w=1.5, h=2.0, area=3.0)

    r1.scale(2)
    print(r1)               # Now r1 should be Rectangle(w=6, h=8, area=48)

    print(r2 == Rectangle(1.5, 2.0))  # Expected: True