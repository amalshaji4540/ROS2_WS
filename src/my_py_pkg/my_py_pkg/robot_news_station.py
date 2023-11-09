#! usr/bin/env python3
import rclpy
from rclpy.node import Node

class Robotnews(Node):
    def __init__(self):
        super().init("robot_news_station")
        self.publisher_=rclpy

def main(args=None):
    rclpy.init(args=args)
    node=Robotnews()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__=="__main__":
    main()