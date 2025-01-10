# SPDX-FileCopyrightText: 2025 Yuuma Sakurai
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class PressurePublisher(Node):
    def __init__(self):
        super().__init__('pressure_publisher')
        self.publisher_ = self.create_publisher(Float32, 'pressure', 10)
        self.timer = self.create_timer(1.0, self.publish_pressure)

    def publish_pressure(self):
        pressure = random.uniform(950.0, 1050.0)
        msg = Float32()
        msg.data = pressure
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PressurePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

