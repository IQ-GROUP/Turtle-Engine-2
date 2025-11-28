#renderer.py

import turtle as t

from Rendering.Comps.polygon import Polygon

#default configuration
t.hideturtle()
t.speed(0)
t.delay(0)
screen = t.Screen()
screen.tracer(0)

#user level public
def clear():
    t.clear()

#public
def _draw_polygon(polygon: Polygon):
    vertices = polygon.vertices
    for i in range(len(vertices)):
        p = vertices[i]
        __plot_point_2d(p)
        __draw_line(p, vertices[i - 1])

#private
def __plot_point_2d(point):
    t.penup()
    t.goto(point.x, point.y)
    t.pendown()
    t.dot(10)

def __draw_line(p1, p2):
    t.penup()
    t.goto(p1.x, p1.y)
    t.pendown()
    t.goto(p2.x, p2.y)

def alive():
    t.update()
    screen.update()