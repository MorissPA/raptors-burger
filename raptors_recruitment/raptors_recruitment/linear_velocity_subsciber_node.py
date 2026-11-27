import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


class LinearVelocitySubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.TOPIC_COMMAND = 'cmd_vel'
        self.TOPIC_ODOMETRY = 'odom'
        self.subscription_command_velocty = self.create_subscription(Twist, self.TOPIC_COMMAND, self.command_callback,10)
        self.subscriptions_odometry_velocity = self.create_subscription(Odometry, self.TOPIC_ODOMETRY, self.odometry_callback, 10)
        self.TIMER_PERIOD = 0.5
        self.timer = self.create_timer(self.TIMER_PERIOD ,self.timer_callback)
        
        self.odometry_velocity = 0
        self.command_velocity = 0
        
        
        
    def command_callback(self, twist:Twist):
        self.command_velocity = twist.linear.x

    def odometry_callback(self, odometry:Odometry):
        self.odometry_velocity = odometry.twist.twist.linear.x


    def timer_callback(self):
        if self.odometry_velocity + 1 <= self.command_velocity:    
            self.get_logger().info(f'Warning! Motors are not catching with commands! current velocity is only: {self.odometry_velocity:.3f} | command velocity: {self.command_velocity:.3f} m/s')
        else:
            self.get_logger().info(f'Current velocity is only: {self.odometry_velocity:.3f} | command velocity: {self.command_velocity:.3f} m/s')
            

def main(args = None):
    print('Started Linear Velocity Publisher Node.')
    rclpy.init(args = args)
    minimalSubscriber = LinearVelocitySubscriber()
    rclpy.spin(minimalSubscriber)
    
    minimalSubscriber.destroy_node()
    rclpy.shutdown()
    
    
if __name__ == '__main__':
    main()
