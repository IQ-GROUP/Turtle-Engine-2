from typing import List

from Rendering.Comps.vectors import Vector3


class Polygon():
    def __init__(self, vertices: List[Vector3]):
        self.vertices = vertices