#!/bin/bash
# SPDX-FileCopyrightText: 2024 Yuuma Sakurai
# SPDX-License-Identifier: BSD-3-Clause

res=0

# ディレクトリ設定
dir=~
[ "$1" != "" ] && dir="$1"

# ROS 2ワークスペースのビルドと環境設定
cd $dir/ros2_ws
colcon build
source $dir/ros2_ws/install/setup.bash  # ROS 2ワークスペースの環境設定

# タイムアウトでpressure_publisherノードを実行し、ログを/tmp/mypkg.logに保存
timeout 10 ros2 run mypkg pressure_publisher &> /tmp/test.log # バックグラウンドで実行

# 少し待機してノードの動作を確認
sleep 2

# ログファイルから気圧データが含まれているかをgrepでチェック
if grep -qE 'pressure: [0-9]+\.[0-9]+' /tmp/test.log; then
    echo "Test Passed: Valid pressure data found."
else
    echo "Test Failed: No valid pressure data found."
    res=1
fi

exit $res
