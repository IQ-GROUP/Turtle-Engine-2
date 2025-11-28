#transformApplier.py

from math import cos, sin, radians
from Rendering.Comps.vectors import Vector3

class TransformApplier():
    @staticmethod
    def apply_position(
            position: Vector3 = Vector3.zero(),
            vertex: Vector3 = Vector3.zero()
    ) -> Vector3:
        return Vector3(
            vertex.x + position.x,
            vertex.y + position.y,
            vertex.z + position.z
        )

    @staticmethod
    def apply_rotation(
            rotation: Vector3 = Vector3.zero(),
            vertex: Vector3 = Vector3.zero()
    ) -> Vector3:
        x = vertex.x
        y = vertex.y
        z = vertex.z

        rx = radians(rotation.x)
        ry = radians(rotation.y)
        rz = radians(rotation.z)

        y_new = y * cos(rx) - z * sin(rx)
        z_new = y * sin(rx) + z * cos(rx)
        y, z = y_new, z_new

        x_new = x * cos(ry) + z * sin(ry)
        z_new = -x * sin(ry) + z * cos(ry)
        x, z = x_new, z_new

        x_new = x * cos(rz) - y * sin(rz)
        y_new = x * sin(rz) + y * cos(rz)
        x, y = x_new, y_new

        return Vector3(x, y, z)

    @staticmethod
    def apply_scale(
            scale: Vector3 = Vector3.zero(),
            vertex: Vector3 = Vector3.zero()
    ) -> Vector3:

        return Vector3(
            vertex.x * scale.x,
            vertex.y * scale.y,
            vertex.z * scale.z
        )