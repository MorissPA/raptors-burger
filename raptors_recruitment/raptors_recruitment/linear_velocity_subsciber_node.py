"""Subscriber node for checking TurtleBot3 linear velocity."""

from geometry_msgs.msg import TwistStamped
from nav_msgs.msg import Odometry
import rclpy
from rclpy.node import Node


class LinearVelocitySubscriber(Node):
    """Listen to cmd_vel and odom topics and compare target vs actual speed."""

    def __init__(self):
        """Set up subscriptions, timer, and starting velocity variables."""
        super().__init__('linear_velocity_subscriber')

        self.TOPIC_COMMAND_VEL = 'cmd_vel'
        self.TOPIC_ODOMETRY = 'odom'
        self.subscription_command_velocty = self.create_subscription(
            TwistStamped, self.TOPIC_COMMAND_VEL, self.command_callback, 10
        )
        self.subscriptions_odometry_velocity = self.create_subscription(
            Odometry, self.TOPIC_ODOMETRY, self.odometry_callback, 10
        )

        self.TIMER_PERIOD = 0.5  # sec
        self.timer = self.create_timer(self.TIMER_PERIOD, self.timer_callback)

        self.odometry_velocity = 0  # init value
        self.command_velocity = 0  # init value

    def command_callback(self, twist: TwistStamped):
        """Get command velocity and assign to local variable."""
        self.command_velocity = twist.twist.linear.x

    def odometry_callback(self, odometry: Odometry):
        """Get odometry velocity and assign to local variable."""
        self.odometry_velocity = odometry.twist.twist.linear.x

    def timer_callback(self):
        """Check odom and cmd velocity periodically and warn if falling behind."""
        if self.odometry_velocity + 1 <= self.command_velocity:
            self.get_logger().info(
                f'Warning! Motors are not catching with commands! '
                f'current velocity is only: {self.odometry_velocity:.3f} | '
                f'command velocity: {self.command_velocity:.3f} m/s'
            )
        else:
            self.get_logger().info(
                f'Current velocity is: {self.odometry_velocity:.3f} | '
                f'command velocity: {self.command_velocity:.3f} m/s'
            )


def main(args=None):
    """Initialize ROS 2 and run the subscriber node until stopped."""
    print('Started Linear Velocity Subscriber Node.')
    rclpy.init(args=args)
    minimal_subscriber = LinearVelocitySubscriber()
    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
