#object.py
from Objecting.Comps.transform import Transform
from Rendering.Modelling.figures import Parallelepiped, Model
from Shared.Comps.vectors import Vector3

class Object:
    def __init__(
            self,
            transform: Transform,
            mesh: Parallelepiped | Model
    ):
        self.transform = transform
        self.mesh = mesh

    def spawn(self):
        self.mesh.transform = self.transform.global_to_screen()
        self.mesh.draw()
