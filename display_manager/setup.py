from setuptools import find_packages, setup

package_name = 'display_manager'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    package_data={
        package_name: ['images/*/*'],  
    },
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='CSE276B Team',
    maintainer_email='cse276b@todo.todo',
    description='Display Manager node - receives display commands and updates pupper screen display',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'display_manager = display_manager.display_manager:main',
        ],
    },
)
