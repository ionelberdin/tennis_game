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
    
    def __sum__(self, other):
        return Array(*[i + j for i, j in zip(self.xyz, other.xyz)])
    
    def __prod__(self, other):
        if (type(other) in [float, int]):
            return Array