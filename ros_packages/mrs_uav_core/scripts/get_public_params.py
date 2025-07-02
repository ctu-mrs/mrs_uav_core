#!/usr/bin/python3

import rospkg
import subprocess

class ParamsGetter:

    def __init__(self):

        rospack = rospkg.RosPack()

        packages = [
            "mrs_uav_managers",
            "mrs_uav_trackers",
            "mrs_uav_controllers",
            "mrs_uav_trajectory_generation",
            "mrs_uav_state_estimators",
            "mrs_uav_status",
        ]

        for package in packages:

            s = subprocess.check_output("ros2 run {} get_public_params.py".format(package), shell = True)
            print(s.decode("utf-8"))

if __name__ == '__main__':
    params_getter = ParamsGetter()
