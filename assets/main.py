#main.py

from Behaviours.common import CommonBehaviour
from Objecting.Comps.object import Object
from Objecting.Comps.transform import Transform
from Rendering.Comps.Styling.styling import Style, Color, RGBA
from Rendering.Comps.screenTransform import ScreenTransform
from Rendering.Modelling.figures import Parallelepiped, Model
from Rendering.renderer import *


class Main(CommonBehaviour):
    def __init__(self):
        self.tick = 0.0016  # Tick time in seconds for 60FPS
        self.enabled = True  # Flag to enable the script to run

    sphere_mesh = Model(
        "Models/B.obj",
        ScreenTransform(),
        Style(
            showVertices=False
        )
    )

    sphere = Object(
            Transform(
                position=Vector3(0, 0, -1),
                rotation=Vector3(-45, 0, 0),
                scale=Vector3(20, 20, 20),
            ),
            sphere_mesh
    )

    async def start(self):
       pass

    rx= 0
    ry = 0
    rz = 0
    rate = 1
    async def update(self):
        clear()
        self.sphere.transform.rotation.x = self.rx
        self.sphere.transform.rotation.y = self.ry
        self.sphere.transform.rotation.z = self.rz
        self.sphere.spawn()
        self.rx += self.rate
        self.ry += self.rate
        self.rz += self.rate
        alive()