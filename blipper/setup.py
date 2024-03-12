from setuptools import setup, find_packages

setup(
    name='blipper',
    version='0.0.1',
    license='MIT',
    description='Blipper library by Atenea AI',
    long_description=open('README.md').read(),
    install_requires=['os','requests','json'],
    url='http://github.com/epystemic/blipper-library',
    author='Atenea AI',
    author_email='dev@atenea.ai'
)