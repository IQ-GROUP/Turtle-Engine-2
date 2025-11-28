#main.py

from Behaviours.common import CommonBehaviour
from Rendering.Comps.transform import Transform
from Rendering.Comps.vectors import Vector3
from Rendering.Modelling.figures import Parallelepiped
from Rendering.renderer import *


class Main(CommonBehaviour):
    def __init__(self):
        self.tick = 0.0016  # Tick time in seconds for 60FPS
        self.enabled = True  # Flag to enable the script to run

    async def start(self):
       Parallelepiped(
           Transform(
               Vector3(0, 0, 0)
           ),
           200,
           100,
           50
       ).draw()

    async def update(self):
        alive()