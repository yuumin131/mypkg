#!/bin/bash -xv
# SPDX-FileCopyrightText: 2024 Yuuma Sakurai
# SPDX-License-Identifier: BSD-3-Clause

res=0

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
#source $dir/ros2_ws/install/setup.bash

source $dir/.bashrc
source install/setup.bash && source install/local_setup.bash

timeout 10 ros2 run mypkg pressure_publisher &
timeout 10 ros2 run mypkg listener &> /tmp/test.log

sleep 2

echo TEST LOG
cat /tmp/test.log

if grep -qE 'Listen: [0-9]+\.[0-9]+' /tmp/test.log; then
    echo "Test Passed: Valid pressure data found."
else
    echo "Test Failed: No valid pressure data found."
    res=1
fi

exit $res
