#!usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init(self):
        super.__init__("pynode")
        self._logger.info("ROS2 Python Node")
        

def main(args=None):
    rclpy.init(args)
    node=MyNode()
    # rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()