import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    pressure_publisher = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'pressure_publisher',
            )

    listener = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'listener',
            output = 'screen'
            )

    return launch.LaunchDescription([pressure_publisher, listener])
