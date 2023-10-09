# The MRS UAV System Core

## Installation

The core is installed as a part of the [MRS UAV System](https://github.com/ctu-mrs/mrs_uav_system#installation).

## Contents

The core takes care of the collowing aspects of the autonomous UAV flight:

* hardware abstraction,
* state estimation,
* feedback control,
* reference generation,
* trajectory generation,
* flight management,
* takeoff and landing,
* plugin interfaces for *feedback controllers*, *reference trackers*, *state estimators*, and *hardware api*.

Moreover, the core provides

* MRS libraries,
* MRS ROS messages,
* MRS Rviz plugins,
* MRS multirotor simulator.

## Submodules

| Repository                                                                                |
|-------------------------------------------------------------------------------------------|
| [mrs_lib](https://github.com/ctu-mrs/mrs_lib)                                             |
| [mrs_msgs](https://github.com/ctu-mrs/mrs_msgs)                                           |
| [mrs_multirotor_simulator](https://github.com/ctu-mrs/mrs_multirotor_simulator)           |
| [mrs_rviz_plugins](https://github.com/ctu-mrs/mrs_rviz_plugins)                           |
| [mrs_uav_controllers](https://github.com/ctu-mrs/mrs_uav_controllers)                     |
| [mrs_uav_autostart](https://github.com/ctu-mrs/mrs_uav_autostart)                         |
| [mrs_uav_hw_api](https://github.com/ctu-mrs/mrs_uav_hw_api)                               |
| [mrs_uav_managers](https://github.com/ctu-mrs/mrs_uav_managers)                           |
| [mrs_uav_state_estimators](https://github.com/ctu-mrs/mrs_uav_state_estimators)           |
| [mrs_uav_status](https://github.com/ctu-mrs/mrs_uav_status)                               |
| [mrs_uav_trackers](https://github.com/ctu-mrs/mrs_uav_trackers)                           |
| [mrs_uav_trajectory_generation](https://github.com/ctu-mrs/mrs_uav_trajectory_generation) |
