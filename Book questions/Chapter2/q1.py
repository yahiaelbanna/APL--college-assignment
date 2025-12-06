class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return NotImplemented
    
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("v1:", v1)
print("v2:", v2)
print("v1 + v2 =", v1 + v2)
print("v2 - v1 =", v2 - v1)
print("v1 ⋅ v2 =", v1 * v2)
print("representation:", repr(v1))