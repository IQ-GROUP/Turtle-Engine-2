#main.py

from Behaviours.common import CommonBehaviour
from Rendering.Comps.Styling.styling import Style, Color, RGBA
from Rendering.Comps.transform import Transform
from Rendering.Modelling.figures import Parallelepiped, Model
from Rendering.renderer import *


class Main(CommonBehaviour):
    def __init__(self):
        self.tick = 0.0016  # Tick time in seconds for 60FPS
        self.enabled = True  # Flag to enable the script to run

    async def start(self):
        pass

    xr = 45
    yr = 0
    zr = 0
    async def update(self):
        clear()
        Model(
            "Models/Donut.obj",
            Transform(
                Vector3.zero(),
                Vector3(self.xr, self.yr, self.zr),
                Vector3(100, 100, 100)
            ),
            Style(
                showVertices=False,
                fillColor=Color(RGBA(0, 153, 153, 1)),
                backFaceCulling=True
            )
        ).draw()
        self.yr += 1
        self.zr += 1
        alive()