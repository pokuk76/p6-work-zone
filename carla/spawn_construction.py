#!/usr/bin/env python


"""Example script to generate traffic in the simulation"""

import glob
import os
import sys
import time

try:
    sys.path.append(glob.glob('/home/carla/carla/Dist/CARLA_Shipping_0.9.14-4-gf14acb257-dirty/LinuxNoEditor/PythonAPI/carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

from carla import VehicleLightState as vls
# from carla import BarrierCones as vls

import argparse
import logging
from numpy import random

client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

world = client.get_world()

_map = world.get_map()

spawn_points = _map.get_spawn_points()


"""

Content/Carla/Static/Dynamic/Construction/SM_{ConstructionCone, SheelBarrow, StreetBarrier, TrafficCones_01, TrafficCones_02, TrafficCones_03, WarningAccident, WarningConstruction}

Content/Carla/Static/GuardRail/SM_{Secfence_03, Secfence_04, Secfence_06, SecWater_01, SecWater_02, SecWater_03}

"""

prop_ids = [
    "static.prop.constructioncone",
    #"static.prop.sheelbarrow",
    "static.prop.streetbarrier",
    "static.prop.trafficcone01",
    "static.prop.trafficcone02",  # This one looks a little weird ngl
    #"static.prop.trafficcone03",
    "static.prop.warningaccident",
    "static.prop.warningconstruction",
    # ...
    "static.prop.secfence03",
    "static.prop.secfence04",
    "static.prop.secfence06",
    "static.prop.secwater01",
    "static.prop.secwater02",
    "static.prop.secwater03",
]


def get_actor_blueprints(world, props):
    bps = [world.get_blueprint_library().find(prop) for prop in props]
    return bps
    
blueprints = get_actor_blueprints(world, prop_ids)

print(blueprints)



