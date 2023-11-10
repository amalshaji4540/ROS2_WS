#!/usr/bin/env python3
import rclpy #python library that is neccesary for using ros functionalities
from rclpy.node import Node #python library for creating nodes
class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.counter=0
        self._logger.info("Hello ROS2 Node !!")
        self.create_timer(0.5,self.timer_Callback)
    
    def timer_Callback(self):
        self.counter+=1
        self._logger.info("Hello "+str(self.counter))
        
def main(args=None):
    rclpy.init(args=args) #intializing the ros functionalities
    node=MyNode()  #for creating the node
    rclpy.spin(node)
    rclpy.shutdown() #for shutting down the node
if __name__=="__main__":
    main()  