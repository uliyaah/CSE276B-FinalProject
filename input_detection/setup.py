from setuptools import find_packages, setup

package_name = 'final_project_input_detection'

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
    maintainer='atn046',
    maintainer_email='atn046@ucsd.edu',
    description='Final Project: Camera and Touch Input Detection',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = final_project_input_detection.service_touch:main',
            'client = final_project_input_detection.client_touch:main',
        ],
    },
)
