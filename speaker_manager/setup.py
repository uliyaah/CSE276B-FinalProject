from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'speaker_manager'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/resource', glob('resource/*')),
        ('share/' + package_name + '/audio', glob('audio/*')),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
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
            'service = speaker_manager.mock_speaker_publisher:main',
            'client = speaker_manager.client_speaker:main',
            'music_server = speaker_manager.music_server:main',
        ],
    },
)

