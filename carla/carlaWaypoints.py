import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import argparse

import numpy as np

from agents.navigation.global_route_planner import GlobalRoutePlanner
# from agents.navigation.global_route_planner_dao import GlobalRoutePlannerDAO


client = carla.Client('localhost', 2000)
client.set_timeout(2.0)

def draw_waypoints(waypoints, road_id = None, life_time = 10000):

    for waypoint in waypoints:

        client.get_world().debug.draw_string(waypoint[0].transform.location, 'O', 
        draw_shadow=False,
        color=carla.Color(r=0, g=0, b=255), life_time=life_time,
        persistent_lines=True)

world = client.load_world('Town01')

# world = client.get_world()

amap = world.get_map()


sampling_resolution = 2

grp = GlobalRoutePlanner(amap, sampling_resolution)

spawn_points = amap.get_spawn_points()

a = carla.Location(spawn_points[100].location)

b = carla.Location(spawn_points[0].location)

waypoints = grp.trace_route(a, b)


for points in spawn_points:
    world.debug.draw_string(points.location, 'O', draw_shadow=False,
            color=carla.Color(r=0, g=255, b=0), life_time=5000.0,
            persistent_lines=True)

world.debug.draw_string(spawn_points[0].location, 'O', draw_shadow=False,
        color=carla.Color(r=255, g=0, b=0), life_time=5000.0,
        persistent_lines=True)

# i = 0
# for w in waypoints:
#     if i % 10 == 0:
#         world.debug.draw_string(w[0].transform.location, 'O', draw_shadow=False,
#         color=carla.Color(r=255, g=0, b=0), life_time=120.0,
#         persistent_lines=True)
#     else:
#         world.debug.draw_string(w[0].transform.location, 'O', draw_shadow=False,
#         color = carla.Color(r=0, g=0, b=255), life_time=1000.0,
#         persistent_lines=True)
#     i += 1

draw_waypoints(waypoints)

N = len(waypoints)

T = np.zeros([4, 4, N])

for i in range(N):
    T[:, :, i] = np.array(waypoints[i][0].transform.get_matrix())

np.save("transforms.npy", T)