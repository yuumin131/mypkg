# SPDX-FileCopyrightText: 2025 Yuuma Sakurai
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node = Node("listener")


def cb(sub):
    global node
    node.get_logger().info("Listen: %s" % sub.data)


def main():
    sub = node.create_subscription(String, "chiba_pressure", cb, 10)
    rclpy.spin(node)
