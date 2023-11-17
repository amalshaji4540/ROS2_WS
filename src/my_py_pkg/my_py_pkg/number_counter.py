#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounter(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter=0
        self.subscriber_=self.create_subscription(Int64,"number",self.callback_number,10)
        self.publishers_=self.create_publisher(Int64,"number_count",10)
        self.service_=self.create_service(SetBool,"reset_counter",self.callback_reset_counter)
        self.get_logger().info("number_counter node has started")
   
    def callback_number(self,msg):
        self.counter+=msg.data
        new_msg=Int64()
        new_msg.data=self.counter 
        self.publishers_.publish(new_msg)
        
    def callback_reset_counter(self,request,response):
        if(request.data==True):
            self.counter=0
            response.success=True
            response.message="Counter value is set to 0"
        else:
            response.success=False
            response.message="Counter is not changed"
        self.get_logger().info("Request is processed")
        return response
         
def main(args=None):
    rclpy.init(args=args)
    node=NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__=="__main__":
    main()