from setuptools import find_packages, setup

package_name = 'lab2task4'

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
    maintainer='udionisio',
    maintainer_email='udionisio@ucsd.edu',
    description='Lab 2 Task 4: Robot moves based on touch',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = lab2task4.service_go_pupper:main',
        	'client = lab2task4.client_go_pupper:main',
        ],
    },
)
