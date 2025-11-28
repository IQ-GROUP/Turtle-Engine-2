#renderer.py

import turtle as t

from Rendering.Comps.polygon import Polygon
from Rendering.Comps.vectors import Vector2, Vector3

#default configuration
t.hideturtle()
t.speed(0)
t.delay(0)
t.width(2)
screen = t.Screen()
screen.tracer(0)

#user level public
def clear() -> None:
    t.clear()

#public
def _draw_polygon(polygon: Polygon) -> None:
    vertices = polygon.vertices
    for i in range(len(vertices)):
        p = vertices[i]
        style = polygon.style


        ect = style.edgesColor.value.tuple()
        t.pencolor(ect[0], ect[1], ect[2])

        fct = style.fillColor.value.tuple()
        t.fillcolor(fct[0], fct[1], fct[2])

        if(fct[3] != 0):
            t.begin_fill()

        if(style.showVertices):
            __plot_point_2d(p)

        __draw_line(p, vertices[i - 1])

        t.end_fill()

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