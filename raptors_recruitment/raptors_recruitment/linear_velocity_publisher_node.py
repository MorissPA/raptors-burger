"""Publisher node sending a constant linear velocity command."""

from geometry_msgs.msg import TwistStamped
import rclpy
from rclpy.node import Node


class LinearVelocityPublisher(Node):
    """Publish a constant speed on TOPIC_COMMAND_VEL periodically."""

    def __init__(self):
        """Initialize publisher and timer."""
        super().__init__('linear_velocity_publisher')
        self.TOPIC_COMMAND_VEL = 'cmd_vel'
        self.publisher_ = self.create_publisher(
            TwistStamped, self.TOPIC_COMMAND_VEL, 10
        )  # Create publisher on command velocity topic
        self.TIMER_PERIOD = 0.5  # sec
        self.timer = self.create_timer(self.TIMER_PERIOD, self.timer_callback)

    def timer_callback(self):
        """Publish TwistStamped packet periodically on topic."""
        pkg_twist = TwistStamped()  # Empty twist package to be published on topic
        pkg_twist.twist.linear.x = 5.0
        self.publisher_.publish(pkg_twist)
        self.get_logger().info(
            f'Publishing velocity: {pkg_twist.twist.linear.x} '
            f'on topic {self.TOPIC_COMMAND_VEL}'
        )  # Log publish


def main(args=None):
    """Start node and keep alive until Ctrl+C."""
    print('Started Linear Velocity Publisher Node.')
    rclpy.init(args=args)
    minimal_publisher = LinearVelocityPublisher()
    rclpy.spin(minimal_publisher)  # Wait until publisher stops

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
