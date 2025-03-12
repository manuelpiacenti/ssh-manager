# setup.py
from setuptools import setup, find_packages

setup(
    name='ssh-manager',
    version='0.5.1',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'questionary',
        'gitpython'
    ],
    entry_points={
        'console_scripts': [
            'ssh-manager=ssh_manager.cli:main'
        ],
    },
    include_package_data=True,
    description='Manage SSH configs by group and subgroup from the command line',
    author='Manuel Piacenti',
    license='GPLv3',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)