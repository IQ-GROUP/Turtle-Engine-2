# engine.py

import os
import importlib
from Behaviours.common import CommonBehaviour
import asyncio

from Rendering.Comps.vectors import Vector3


def import_all_scripts():
    folder_path = os.path.join(os.path.dirname(__file__), "assets")

    for filename in os.listdir(folder_path):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            full_module = f"assets.{module_name}"
            importlib.import_module(full_module)

def import_debug_scripts():
    folder_path = os.path.join(os.path.dirname(__file__), "Debug")

    for filename in os.listdir(folder_path):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            full_module = f"Debug.{module_name}"
            importlib.import_module(full_module)

name = "TV2"
debug = False

async def main():
    print(f"{name}: Booting...")
    import_all_scripts()
    if(debug):
        import_debug_scripts()

    # Create all behaviour instances
    print(f"{name}: Getting scripts instances...")
    instances = [cls() for cls in CommonBehaviour.__subclasses__()]

    # Start all Behaviours
    tasks = []
    for instance in instances:
        if(instance.enabled):
            print(f"{name}: Starting instance - {instance.__class__.__name__} ...")
            tasks.append(asyncio.create_task(instance.run()))

    # Run forever (or until all tasks complete)
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())