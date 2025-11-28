#transform.py

from Rendering.Comps.vectors import Vector3

class Transform():
    def __init__(
            self,
            position: Vector3 = Vector3.zero(),
            rotation: Vector3 = Vector3.zero(),
            scale: Vector3 = Vector3.zero()
    ) -> None:
        self.position = position
        self.rotation = rotation
        self.scale = scale