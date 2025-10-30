# The MRS UAV System Core

## Installation

The Core is installed as a part of the [MRS UAV System](https://github.com/ctu-mrs/mrs_uav_system/tree/ros2#installation).

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
* MRS multirotor simulator.

## Submodules

| Repository                                                                                          |
|-----------------------------------------------------------------------------------------------------|
| [mrs_lib](https://github.com/ctu-mrs/mrs_lib/tree/ros2)                                             |
| [mrs_msgs](https://github.com/ctu-mrs/mrs_msgs/tree/ros2)                                           |
| [mrs_multirotor_simulator](https://github.com/ctu-mrs/mrs_multirotor_simulator/tree/ros2)           |
| [mrs_uav_controllers](https://github.com/ctu-mrs/mrs_uav_controllers/tree/ros2)                     |
| [mrs_uav_autostart](https://github.com/ctu-mrs/mrs_uav_autostart/tree/ros2)                         |
| [mrs_uav_hw_api](https://github.com/ctu-mrs/mrs_uav_hw_api/tree/ros2)                               |
| [mrs_uav_managers](https://github.com/ctu-mrs/mrs_uav_managers/tree/ros2)                           |
| [mrs_uav_state_estimators](https://github.com/ctu-mrs/mrs_uav_state_estimators/tree/ros2)           |
| [mrs_uav_status](https://github.com/ctu-mrs/mrs_uav_status/tree/ros2)                               |
| [mrs_uav_trackers](https://github.com/ctu-mrs/mrs_uav_trackers/tree/ros2)                           |
| [mrs_uav_trajectory_generation](https://github.com/ctu-mrs/mrs_uav_trajectory_generation/tree/ros2) |

# Disclaimer

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
