from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='py-money',
    packages=[
        'money'
    ],
    version='0.2.0',
    description='Money module for python',
    long_description=long_description,
    url='https://github.com/vimeo/py-money',
    author='Nicky Robinson',
    author_email='nickr@vimeo.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='money currency',
    install_requires=[
        'babel==2.4.0'
    ],
)
