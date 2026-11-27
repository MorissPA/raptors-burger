from setuptools import find_packages, setup

package_name = 'raptors_recruitment'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ps',
    maintainer_email='255706@edu.p.lodz.pl',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'linear_velocity_publisher_node = '
            'raptors_recruitment.linear_velocity_publisher_node:main',

            'linear_velocity_subsciber_node = '
            'raptors_recruitment.linear_velocity_subsciber_node:main'
        ],
    },
)
