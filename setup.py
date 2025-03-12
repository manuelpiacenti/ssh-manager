from setuptools import setup, find_packages

setup(
    name='ssh-manager',
    version='0.3.0',
    packages=find_packages(),
    install_requires=['python-dotenv', 'questionary', 'gitpython'],
    entry_points={
        'console_scripts': ['ssh-manager=ssh_manager.cli:main'],
    },
)
