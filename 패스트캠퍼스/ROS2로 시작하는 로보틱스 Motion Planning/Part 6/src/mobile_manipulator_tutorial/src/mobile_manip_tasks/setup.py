from setuptools import find_packages, setup

package_name = 'mobile_manip_tasks'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Scott Lee',
    maintainer_email='sl148@illinois.edu',
    description='Navigation tasks',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'delivery_task = mobile_manip_tasks.delivery_task:main',
            'send_initialpose = mobile_manip_tasks.send_initialpose:main',
            'slam_toolbox_load_map = mobile_manip_tasks.slam_toolbox_load_map:main',
            'follow_waypoints = mobile_manip_tasks.follow_waypoints:main',
        ],
    },
)
