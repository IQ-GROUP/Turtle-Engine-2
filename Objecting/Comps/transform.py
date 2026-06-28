#transform.py
from Rendering.Comps.screenTransform import ScreenTransform
from Shared.Comps.vectors import Vector3

class Transform:
    def __init__(
            self,
            position: Vector3 = Vector3.zero(),
            rotation: Vector3 = Vector3.zero(),
            scale: Vector3 = Vector3(1, 1, 1),
    ):
        self.position = position
        self.rotation = rotation
        self.scale = scale

    def global_to_screen(self) -> ScreenTransform:
        position = self.position
        rotation = self.rotation
        scale = self.scale
        return ScreenTransform(position, rotation, scale)