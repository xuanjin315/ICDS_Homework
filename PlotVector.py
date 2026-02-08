import matplotlib.pyplot as plt

class Vector:
    def __init__(self, lst):
        if not (isinstance(lst, (list, tuple)) and all(isinstance(x, (int, float)) for x in lst)):
            raise TypeError("Vector components must be a list or tuple of numbers")
        self.vec = list(lst)

    def __len__(self):
        return len(self.vec)
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
    

    def __str__(self):
        """
        Return a string representation of the vector.
        """
        # TODO: return something like "[1, 2, 3]"
        return str(self.vec)
    __repr__ = __str__  # so printing in console works the same



def plot_vectors(vecs):
    """
    Plot a head-to-tail path for a list of 2-D vectors and the resultant vector.

    Parameters
    ----------
    vecs : list[Vector]
        Each vector must have length 2.

    Returns
    -------
    None
    """
    # Check all vectors are 2-D
    if not all(len(v) == 2 for v in vecs):
        raise ValueError("All vectors must be 2-D to plot")

    # Start at origin
    xs = [0.0]
    ys = [0.0]
    sum_x=0
    sum_y=0

    # TODO: loop over vecs and update xs, ys cumulatively
    for v in vecs:
        sum_x+=v.vec[0]
        sum_y+=v.vec[1]
        xs.append( sum_x)
        ys.append( sum_y )
        
 
    plt.plot(xs,ys,"o-",color="blue",label="Path")
        
    x_end=xs[-1]
    y_end=ys[-1]
    dx=x_end-0
    dy=y_end-0
    plt.arrow(0,0,dx,dy,head_width=0.1,head_length=0.15,fc="red",ec="red",length_includes_head=True,label="Resultant")

    # TODO: use plt.plot to draw the path (blue with markers)

    # TODO: use plt.quiver (or plt.arrow) to draw the resultant vector (in red)

    # Labels, grid, and title
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Head-to-Tail Path of Vectors")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()


if __name__ == "__main__":
    a = Vector([1, 2])
    b = Vector([2, -1])
    c = Vector([0.5, 1.5])

    plot_vectors([a, b, c])