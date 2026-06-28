#screenTransform.py

from Shared.Comps.vectors import Vector3

class ScreenTransform():
    def __init__(
            self,
            position: Vector3 = Vector3.zero(),
            rotation: Vector3 = Vector3.zero(),
            scale: Vector3 = Vector3(1, 1, 1)
    ) -> None:
        self.position = position
        self.rotation = rotation
        self.scale = scale