import os
from setuptools import setup


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='app',
    version='1',
    install_requires=[
        'm3-objectpack==2.2.25'
        'django==1.11'
    ],
    license='BSD License',
    description='My test work',
    author='showman',
    author_email='0showman0gmail.com',
)