from typing import List

from Rendering.Comps.Styling.styling import Style
from Rendering.Comps.vectors import Vector3


class Polygon:
    def __init__(
            self,
            vertices: List[Vector3],
            style: Style = Style(),
    ):
        self.vertices = vertices

    def normal(self) -> Vector3:
        vertices = self.vertices

        if len(vertices) < 3:
            return Vector3(0, 0, 1)  # default
        normal = Vector3.zero()
        v0 = vertices[0]
        for i in range(1, len(vertices) - 1):
            edge1 = vertices[i] - v0
            edge2 = vertices[i + 1] - v0
            normal = Vector3(
                normal.x + edge1.cross(edge2).x,
                normal.y + edge1.cross(edge2).y,
                normal.z + edge1.cross(edge2).z
            )
        return normal.normalized()
