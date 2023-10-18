#!/usr/bin/env python3
import rclpy #python library that is neccesary for using ros functionalities
from rclpy.node import Node #python library for creating nodes

def main(args=None):
    rclpy.init(args=args) #intializing the ros functionalities
    node=Node("py_test")  #for creating the node
    node.get_logger().info("Hello ROS2") #for printing Hello ROS2
    rclpy.spin(node)
    rclpy.shutdown() #for shutting down the node
if __name__=="__main__":
    main()  