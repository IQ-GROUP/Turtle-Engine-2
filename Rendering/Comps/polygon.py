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