from math import sqrt, cos, sin, pi

class Array:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    @property
    def xy(self):
        return (self.x, self.y)

    @property
    def xyz(self):
        return (*self.xy, self.z)
    
    def __add__(self, other):
        return Array(*[i + j for i, j in zip(self, other)])
    
    def __mul__(self, other):
        if (type(other) in [float, int]):
            return Array(*[i*other for i in self])
        if (type(other) == type(self)):
            return sum([i * j for i, j in zip(self, other)])
    
    def __rmul__(self, other):
        if (type(other) in [float, int]):
            return self * other

    def __truediv__(self, other):
        return self * (1 / other)

    def __iter__(self):
        for i in self.xyz:
            yield i

    def __repr__(self):
        return "Array({})".format(", ".join([str(i) for i in self]))

    def __abs__(self):
        return sqrt(self * self)

    def rotate_z(self, ang:float):
        c, s, x, y, z = cos(ang), sin(ang), *self.xyz
        return Array(x*c - y*s, y*c + x*s, z)

if __name__ == '__main__':
    a = Array()
    print(a)
    b = Array(1,2)
    print(b)
    print(a+b)
    print(4*a, a*4)
    print(4*b, b*4)
    print(b*b, b*a, a*a)
    print(abs(b))
    print(b)
    print(b.rotate_z(pi/6), b.rotate_z(pi/3), b.rotate_z(pi/2), b.rotate_z(2*pi))