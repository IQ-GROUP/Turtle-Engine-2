#debugConsole.py

from Behaviours.common import CommonBehaviour
from Rendering.Modelling.figures import Parallelepiped
from Rendering.renderer import alive, clear
from Rendering.Comps.screenTransform import ScreenTransform
from engine import name

import asyncio
from concurrent.futures import ThreadPoolExecutor

_executor = ThreadPoolExecutor(1)

async def ainput(prompt: str = ""):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(_executor, input, prompt)

class DebugConsole(CommonBehaviour):
    def __init__(self):
        super().__init__()
        self.tick = 0.0016
        self.enabled = True
        self.rx = 0
        self.ry = 0
        self.rate = 0.05
        self.current_animation = None
        self.current_shape = None
        self.transform = None
        self.dimensions = None

    async def update(self):
        # --- check if animation is running ---
        if self.current_animation == "rotating" and self.current_shape:
            self.rx += 1 * self.rate
            self.ry += 1 * self.rate

            clear()
            self.current_shape(
                transform=ScreenTransform(
                    position=self.transform,
                    rotation=Point(self.rx, self.ry, 0)
                ),
                width=self.dimensions[0],
                height=self.dimensions[1],
                depth=self.dimensions[2]
            ).draw()
            alive()
            return  # skip reading input until next tick

        # --- read user command ---
        command = await ainput(f"{name} <- ")

        if command.startswith("draw "):
            shapes = {
                "p": Parallelepiped,
                "parallelepiped": Parallelepiped
            }
            parts = command.split()

            # expected format:
            # draw <shape> <pos> <rot> <size> [animation]
            shape_id = parts[1]
            pos_str = parts[2]
            rot_str = parts[3]
            add_str = parts[4]
            anim_str = parts[5] if len(parts) > 5 else None

            # parse strings
            px, py, pz = map(float, pos_str.split(","))
            rx, ry, rz = map(float, rot_str.split(","))
            ax, ay, az = map(float, add_str.split(","))

            print(f"{name} -> Drawing | {shape_id}")
            print(f"{' ' * len(name)}             | {pos_str}")
            print(f"{' ' * len(name)}             | {rot_str}")
            print(f"{' ' * len(name)}             | {add_str}")
            if anim_str:
                print(f"{' ' * len(name)}             | animation: {anim_str}")

            # store for animation if needed
            self.transform = Point(px, py, pz)
            self.dimensions = (ax, ay, az)
            self.current_shape = shapes[shape_id]
            self.rx = rx
            self.ry = ry

            # if animation requested
            if anim_str == "rotating":
                self.current_animation = "rotating"
            else:
                # draw once if no animation
                clear()
                shapes[shape_id](
                    transform=ScreenTransform(
                        position=Point(px, py, pz),
                        rotation=Point(rx, ry, rz),
                    ),
                    width=ax,
                    height=ay,
                    depth=az
                ).draw()
                alive()
                self.current_animation = None

        else:
            print(f"Unknown command: {command}")