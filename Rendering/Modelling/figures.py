#figures

from typing import List

from g4f.gui.server.website import render

from Rendering import renderer
from Rendering.Comps.Styling.styling import Style
from Rendering.Comps.transform import Transform
from Rendering.Comps.vectors import Vector3
from Rendering.Comps.polygon import Polygon
from Rendering.Maths.transformApplier import TransformApplier


class Parallelepiped:
    def __init__(
            self,
            transform: Transform,
            style: Style = Style(),
    ):
        self.transform = transform
        self.style = style

    #   5____________6
    #  / |          /|
    # 1____________2 | h  y
    # |  7_ _ _ _ _|_8
    # | /    .     | /
    # |/           |/ d   z
    # 3____________4
    #       w   x

    def get_verticies(self) -> List[Vector3]:
        x = self.transform.position.x
        y = self.transform.position.y
        z = self.transform.position.z

        scale = self.transform.scale
        width = scale.x
        height = scale.y
        depth = scale.z

        hw = width / 2
        hh = height / 2
        hd = depth / 2
        vertices = [
            Vector3(x + hw, y + hh, z + hd), #1
            Vector3(x - hw, y + hh, z + hd), #2
            Vector3(x + hw, y - hh, z + hd), #3
            Vector3(x - hw, y - hh, z + hd), #4
            Vector3(x + hw, y + hh, z - hd), #5
            Vector3(x - hw, y + hh, z - hd), #6
            Vector3(x + hw, y - hh, z - hd), #7
            Vector3(x - hw, y - hh, z - hd), #8
        ]

        for i in range(len(vertices)):
            vertex = vertices[i]
            vertex = TransformApplier.apply_position(self.transform.position, vertex)
            vertex = TransformApplier.apply_rotation(self.transform.rotation, vertex)
            vertices[i] = vertex
        return vertices

    def get_polygons(self) -> List[Polygon]:
        vertices = self.get_verticies()
        polygons = [
            #1243
            Polygon(
                [
                    vertices[0], vertices[1], vertices[3], vertices[2]
                ]
            ),
            #5687
            Polygon(
                [
                    vertices[4], vertices[5], vertices[7], vertices[6]
                ]
            ),
            #1573
            Polygon(
                [
                    vertices[0], vertices[4], vertices[6], vertices[2]
                ]
            ),
            #2684
            Polygon(
                [
                    vertices[1], vertices[5], vertices[7], vertices[3]
                ]
            ),
            #1265
            Polygon(
                [
                    vertices[0], vertices[1], vertices[5], vertices[4]
                ]
            ),
            #3487
            Polygon(
                [
                    vertices[2], vertices[3], vertices[7], vertices[6]
                ]
            )
        ]

        return polygons

    def draw(self):
        polygons = self.get_polygons()
        for polygon in polygons:
            polygon.style = self.style
            renderer._draw_polygon(polygon)