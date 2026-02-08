class Vector:
    """A simple Vector class with operator overloading"""

    def __init__(self, lst):
        """
        Initialize a vector with a list of numbers.

        Parameters
        ----------
        lst : list of int or float
            Elements of the vector
        """
        # TODO: store the list in an attribute
        if not isinstance(lst,list):
            raise TypeError
        self.vec = lst

    def __add__(self, other):
        """
        Overload the + operator for vector addition.
        """
        # TODO: implement element-wise addition
        if not isinstance(other, Vector):
            raise TypeError
        if not len(self.vec)==len(other.vec):
            raise ValueError
        new_vec=[]
        for i in range(len(self.vec)):
            new_vec.append(self.vec[i]+other.vec[i])
        return Vector(new_vec)
        

    def __sub__(self, other):
        """
        Overload the - operator for vector subtraction.
        """
        
        if not isinstance(other, Vector):
            raise TypeError
        if not len(self.vec)==len(other.vec):
            raise ValueError
        new_vec=[]
        for i in range(len(self.vec)):
            new_vec.append(self.vec[i]-other.vec[i])
        return Vector(new_vec)

    def __mul__(self, k):
        """
        Overload the * operator for scalar multiplication (Vector * number).
        """
        # TODO: multiply each element by k and return a new Vector
        if not isinstance(k,(int,float)):
            raise TypeError
        new_vec=[]
        for i in range(len(self.vec)):
            new_vec.append(self.vec[i]*k)
        return Vector(new_vec)
        

    def __rmul__(self, k):
        if not isinstance(k,(int,float)):
            raise TypeError
        new_vec=[]
        for i in range(len(self.vec)):
            new_vec.append(self.vec[i]*k)
        return Vector(new_vec)
    
    def __len__(self):
        # TODO: return the lenth of vector
        return len(self.vec)

    def __str__(self):
        """
        Return a string representation of the vector.
        """
        # TODO: return something like "[1, 2, 3]"
        return str(self.vec)
    __repr__ = __str__  # so printing in console works the same


# ===== Sample tests =====
if __name__ == "__main__":
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])

    print("a + b =", a + b)  
    print("a - b =", a - b)  
    print("2 * a =", 2 * a)  