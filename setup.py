"""Boxing clock setup file.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.2'

setup(
    name='cerebellum',
    version=__version__,

    description='Cerebellum',
    long_description=long_description,

    url='',

    # Author details
    author='StudioV98',
    author_email='zedr@zedr.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Other/Nonlisted Topic',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='game',

    packages=find_packages("src"),
    package_dir={'': 'src'},

    install_requires=('Cython==0.25.2', 'kivy==1.10.0', 'jnius'),
)
