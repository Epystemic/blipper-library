from setuptools import setup, find_packages

setup(
    name='blipper',
    version='0.0.2',
    license=None,
    description='Blipper library by Atenea AI',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=['requests'],
    url='http://github.com/epystemic/blipper-library',
    author='Atenea AI',
    author_email='dev@atenea.ai'
)