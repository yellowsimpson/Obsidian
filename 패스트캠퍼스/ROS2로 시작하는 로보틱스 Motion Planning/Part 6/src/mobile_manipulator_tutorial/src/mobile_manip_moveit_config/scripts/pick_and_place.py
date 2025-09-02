#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import math
import numpy as np

# ROS2
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

class Commander(Node):

    def __init__(self):
        super().__init__('pub_path')

        # Create publisher
        self.pub = self.create_publisher(Float64MultiArray, '/target_point', 10)

        # Initialize target point
        self.target_point = np.zeros(3, dtype=np.float64)

    def publish_target(self):
        self.target_point[0] = 0.5
        self.target_point[1] = 0.
        self.target_point[2] = 0.

        # Publish target point
        target_point_pub = Float64MultiArray(data=self.target_point.tolist())  
        self.pub.publish(target_point_pub) 
        self.get_logger().info(f'Published target point: {self.target_point.tolist()}')


def main(args=None):
    rclpy.init(args=args)
    commander = Commander()

    try:
        commander.publish_target()
        rclpy.spin(commander)
    except KeyboardInterrupt:
        pass
    finally:
        commander.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
