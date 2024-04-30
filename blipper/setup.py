from setuptools import setup, find_packages
from blipper import __version__

setup(
    name='blipper',
    version=__version__,
    license=None,
    description='Blipper library by Atenea AI',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='http://github.com/epystemic/blipper-library',
    author='Atenea AI',
    author_email='dev@atenea.ai'
)