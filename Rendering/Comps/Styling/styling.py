#styling.py

class RGBA():
    def __init__(self, r=0, g=0, b=0, a=0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def tuple(self) -> tuple:
        return (self.r, self.g, self.b, self.a)

class Color:
    def __init__(self, value: RGBA = RGBA()) -> None:
        self.value = value

class Style:
    def __init__(
            self,
            showVertices: bool = True,
            showEdges: bool = True,
            edgesColor: Color = Color(RGBA(0, 0, 0, 1)),
            fillColor: Color = Color(RGBA(0, 0, 0, 0)),
    ):
        self.showVertices = showVertices
        self.showEdges = showEdges
        self.edgesColor = edgesColor
        self.fillColor = fillColor