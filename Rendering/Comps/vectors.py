#vectors.py

class Vector2():
    def __init__(
            self,
            x: float = 0,
            y: float = 0,
    ):
        self.x = x
        self.y = y

    @staticmethod
    def zero():
        return Vector2(0, 0)

class Vector3():
    def __init__(
            self,
            x: float = 0,
            y: float = 0,
            z: float = 0
    ):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def zero():
        return Vector3(0, 0, 0)