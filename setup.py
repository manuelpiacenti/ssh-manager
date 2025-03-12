from setuptools import setup, find_packages

setup(
    name='ssh-manager',
    version='0.2.1',
    packages=find_packages(),
    install_requires=['python-dotenv', 'questionary', 'gitpython'],
    entry_points={
        'console_scripts': ['ssh-manager=ssh_manager.cli:main'],
    },
)
