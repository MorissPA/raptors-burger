# Raptors Burger — Simulation Environment

## Contents

- [1. Project Overview](#1-project-overview)
<!--  -->
- [2. System Requirements](#2-system-requirements)
- [3. System Dependencies](#3-system-dependencies)
<!--  -->
- [4. Workspace Setup](#4-workspace-setup)
- [5. Building the Workspace](#5-building-the-workspace)
- [6. Running the Base Packages](#6-running-the-base-packages)
- [7. Running the Custom Package](#7-running-the-custom-package)
<!--  -->
- [8. References](#8-references)

## 1. Project Overview

if you are here \
and don't know why \
it's your problem

some of **those stages** \
**can be preformed in other way** \
so you don't need to flow them

## 2. System Requirements

### 2.1. Operating System

Install **Ubuntu 24.04 LTS**

[Ubuntu - Desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)

***Where ?*** \
(you should know)

### 2.2. ROS 2 Installation

Install **ROS 2 Jazzy Jalisco**

[ROS 2 Jazzy — Ubuntu](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)

***Where ?*** \
(you should know)

### 2.3. ROS 2 Verification

***Input this:***

```bash
source /opt/ros/jazzy/setup.bash
echo "$ROS_DISTRO"
```

***Output should be this:***

```text
jazzy
```

## 3. System Dependencies

### 3.1. Development Tools

***Run this:***

```bash
sudo apt update

sudo apt install -y \
    build-essential \
    python3-colcon-common-extensions \
```

***What are those ?***

### 3.2. NAV2 Packages

***Run this:***

```bash
sudo apt update

sudo apt install -y \
    ros-jazzy-navigation2 \
    ros-jazzy-nav2-bringup
```

***What are those ?***

### 3.3. Gazebo 

***Run this:***

```bash
sudo apt update

sudo apt install -y \
    ros-jazzy-ros-gz \
```

***What are those ?***

### 3.4. TurtleBot3

***Run this:***

```bash
sudo apt update

sudo apt install -y \
    ros-jazzy-turtlebot3 \
    ros-jazzy-turtlebot3-msgs \
    ros-jazzy-turtlebot3-gazebo \
```

***What are those ?***

## 4. Workspace Setup

### 4.1. Create the Workspace

***Run this:***

```bash
mkdir -p ~/recruitment_ws/src
cd ~/recruitment_ws/src
```

***What it does ?***

### 4.2. Fork the Repository

***How ?*** \
***(use context)***

### 4.3. Clone the Repository

make sure, \
this: 

```text
https://github.com/<username>/raptors-burger.git
```

is correct

---

***Run this:***

```bash
cd ~/recruitment_ws/src

read -rp "username: " username

git clone --branch simulation \
    "https://github.com/${username}/raptors-burger.git"

cd raptors-burger
```

***What it does ?***

### 4.4. Create Branch

make sure, \
this: 

```text
recruitment_<username>_<stage>_<task_id>
```

is correct

---

***Run this:***

```bash
cd ~/recruitment_ws/src/raptors-burger

read -rp "username: " username

read -rp "stage: " stage
read -rp "task_id: " task_id

git switch -c "recruitment_${username}_${stage}_${task_id}"
```

***What it does ?***

---

***Run this:***

```bash
git branch --show-current
```

***What it does ?***


## 5. Building the Workspace

### 5.1. Source the Base Workspace

***Run this:***

```bash
source /opt/ros/jazzy/setup.bash
```

***What it does ?***

### 5.2. Install Project Dependencies

***Run this:***

```bash
cd ~/recruitment_ws

sudo rosdep init

rosdep update

rosdep install \
    --from-paths src \
    --ignore-src \
    -r -y
```

***What it does ?***

### 5.3. Build the Packages

***Run this:***

```bash
cd ~/recruitment_ws

colcon build --symlink-install
```

***What it does ?***

### 5.4. Source the Workspace

***Run this:***

```bash
source ~/recruitment_ws/install/setup.bash
```

***What it does ?***

## 6. Running the Base Packages

The simulation uses the **TurtleBot3 Burger** robot model.

Two terminal windows are required:

- Terminal 1 — Simulation.
- Terminal 2 — Keyboard teleoperation.

### 6.1. Terminal 1 — Simulation

Open a terminal and execute:

```bash
export TURTLEBOT3_MODEL=burger
source ~/recruitment_ws/install/setup.bash

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

This launches the simulation.

### 6.2. Terminal 2 — Keyboard Teleoperation

Open a terminal and execute:

```bash
export TURTLEBOT3_MODEL=burger
source ~/recruitment_ws/install/setup.bash

ros2 run turtlebot3_teleop teleop_keyboard
```

This launches the keyboard teleoperation.

## 7. Running the Custom Package

The recruitment tasks are implemented in the `raptors_recruitment` package.

### 7.1. Find Available Executables

***Run this:***

```bash
ros2 pkg executables raptors_recruitment
```

***What it does ?***

### 7.2. Run the Package

***Run this:***

```bash
source ~/recruitment_ws/install/setup.bash

ros2 run raptors_recruitment <executable_name>
```

***What it does ?***

## 8. References

- [ROS 2 Documentation](https://docs.ros.org/en/jazzy/)
- [ROS 2 Installation](https://docs.ros.org/en/jazzy/Installation.html)
<!--  -->
- [NAV 2 Documentation](https://docs.nav2.org/jazzy/)
<!--  -->
- [Gazebo Harmonic Documentation](https://gazebosim.org/docs/harmonic/)
- [Gazebo Harmonic Installation](https://gazebosim.org/docs/harmonic/ros_installation/)
<!--  -->
- [TurtleBot3 Documentation](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)
- [TurtleBot3 Simulation Guide](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/)