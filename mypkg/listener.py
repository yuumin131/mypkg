import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)


def main():
    sub = node.create_subscription(Float32, "pressure", cb, 10)
    rclpy.spin(node)
