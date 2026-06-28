import math

class Vector2():
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    @staticmethod
    def zero():
        return Vector2(0, 0)

class Vector3():
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def zero():
        return Vector3(0, 0, 0)

    # Vector subtraction
    def __sub__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    # Cross product
    def cross(self, other: "Vector3") -> "Vector3":
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def dot(self, other: "Vector3") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalized(self) -> "Vector3":
        mag = self.magnitude()
        if mag == 0:
            return Vector3.zero()
        return Vector3(self.x / mag, self.y / mag, self.z / mag)