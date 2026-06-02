from setuptools import find_packages, setup

package_name = 'input_detection'

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
    maintainer='ubuntu',
    maintainer_email='atn046@ucsd.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service_touch = input_detection.service_touch:main',
            'client_touch = input_detection.client_touch:main',
            'service_camera = input_detection.service_camera:main',
            'client_camera = input_detection.client_camera:main',
        ],
    },
)
