#main.py

from Behaviours.common import CommonBehaviour
from Rendering.Comps.Styling.styling import Style
from Rendering.Comps.transform import Transform
from Rendering.Modelling.figures import Parallelepiped
from Rendering.renderer import *


class Main(CommonBehaviour):
    def __init__(self):
        self.tick = 0.1  # Tick time in seconds for 60FPS
        self.enabled = True  # Flag to enable the script to run

    async def start(self):
        Parallelepiped(
            Transform(
                Vector3(0, 0, 0),
                Vector3(45, -45, 0),
                Vector3(200, 100, 50)
            ),
            Style(
                True,
                True,
            )
        ).draw()

    rx = 0
    async def update(self):
        # clear()
        # p = Parallelepiped(
        #     Transform(
        #         Vector3(0, 0, 0),
        #         Vector3(self.rx, 0, 0),
        #         Vector3(200, 100, 50),
        #     )
        # )
        # self.rx += 1
        # p.draw()
        alive()