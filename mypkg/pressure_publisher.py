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
        pressure = random.uniform(950.0, 1050.0)  # ランダムな気圧 (hPa)
        msg = Float32()
        msg.data = pressure
        self.publisher_.publish(msg)
        self.get_logger().info(f'pressure: {pressure:.2f} hPa')  # ログに気圧を記録


def main(args=None):
    rclpy.init(args=args)
    node = PressurePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

