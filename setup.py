from setuptools import setup, find_packages

setup(
    name='expert-octo-computing-machine',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'octo-compute=src.main:main',
        ],
    },
)
