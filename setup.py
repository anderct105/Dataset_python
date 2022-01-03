from setuptools import setup

setup(
   name='dataset',
   version='0.0.1',
   author='Ander Cejudo',
   author_email='acejudo001@ikasle.ehu.eus',
   packages=['dataset'],
   url='Indicar una URL para el paquete...',
   license='LICENSE.txt',
   description='This package includes some basic functions to work with a dataset object',
   long_description=open('README.txt').read(),
   tests_require=['pytest'],
   install_requires=[
      "seaborn >= 0.9.0",
      "pandas >= 0.25.1",
      "matplotlib >= 3.1.1",
      "numpy >=1.17.2"
   ],
)