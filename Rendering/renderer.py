#renderer.py

import turtle as t

from Rendering.Comps.polygon import Polygon
from Shared.Comps.vectors import Vector2, Vector3

#default configuration
t.hideturtle()
t.speed("fastest")
t.delay(0)
t.width(2)
t.colormode(255) #RGB color mode
t.pencolor(0, 0, 0)
screen = t.Screen()
screen.tracer(0, 0)

CAMERA_DIR = Vector3(0, 0, -1) #Camera facing direction

#user level public
def clear() -> None:
    t.clear()

#public
def _draw_polygon(polygon: Polygon) -> None:
    vertices = polygon.vertices
    style = polygon.style

    # Back Face Culling
    if style.backFaceCulling:
        normal = polygon.normal()
        facing_camera = normal.dot(CAMERA_DIR) < 0
        if not facing_camera and not getattr(style, "showBack", False):
            return

    ct = style.fillColor.value.tuple()
    if ct[3] != 0:
        t.fillcolor(ct[0], ct[1], ct[2])
        t.begin_fill()

    # Move to first vertex
    first = vertices[0]
    t.penup()
    t.goto(first.x, first.y)
    t.pendown()

    # Draw edges to all vertices
    for v in vertices[1:]:
        t.goto(v.x, v.y)

    # Close the polygon
    t.goto(first.x, first.y)

    if ct[3] != 0:
        t.end_fill()

    # Draw verticies
    if style.showVertices:
        for v in vertices:
            __plot_point_2d(v)

    # Draw edges
    for i in range(len(vertices)):
        __draw_line(vertices[i], vertices[i - 1])

vectorAlly = Vector2 | Vector3
#private
def __plot_point_2d(point: vectorAlly) -> None:
    t.penup()
    t.goto(point.x, point.y)
    t.pendown()
    t.dot(8)

def __draw_line(p1:vectorAlly , p2: vectorAlly) -> None:
    t.penup()
    t.goto(p1.x, p1.y)
    t.pendown()
    t.goto(p2.x, p2.y)

def alive() -> None:
    t.update()
    screen.update()