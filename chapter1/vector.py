# Emulando tipos numericos usando os operadores +

from math import hypot


class Vector:

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(self.x) or bool(self.y)
    
    def __add__(self, other):
        if type(other) is not Vector:
            raise TypeError(f'{type(other)} is not a vector class')
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__ == "__main__":
    v1 = Vector(1,1)
    v2 = v1 + v1
    v3 = v1 + Vector(1,0)

    v4 = v1 * 3

    v0 = Vector()

    print('v1: ', v1)
    print('v2: ', v2)
    print('v3: ', v3)
    print('v4: ', v4)

    print('v0: ', v0)

    print('v1 bool: ', bool(v1))
    print('v0 bool: ', bool(v0))

    
