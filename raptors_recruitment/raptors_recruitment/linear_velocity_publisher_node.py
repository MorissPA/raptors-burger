import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist



class LinearVelocityPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.TOPIC = 'cmd_vel'
        self.publisher_ = self.create_publisher(Twist, self.TOPIC, 10)
        self.TIMER_PERIOD = 0.5
        self.timer = self.create_timer(self.TIMER_PERIOD ,self.timer_callback)
        

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 5.0
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing velocity: {msg.linear.x} on topic {self.TOPIC}')


def main(args = None):
    print('Started Linear Velocity Publisher Node.')
    rclpy.init(args = args)
    minimalPublisher = LinearVelocityPublisher()
    rclpy.spin(minimalPublisher)
    
    minimalPublisher.destroy_node()
    rclpy.shutdown()
    
    
if __name__ == '__main__':
    main()
