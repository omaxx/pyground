from setuptools import setup, find_packages
from app import __version__

with open("requirements.txt") as io:
    requirements = io.read().splitlines()

setup(
    name='pyground',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/omaxx/pyground',
    license='MIT',
    author='Maxim Orlov',
    author_email='maxx.orlov@gmail.com',
    description='',
    entry_points={
        "console_scripts": "app=app.__main__:cli",
    },
    install_requires=requirements,
)
