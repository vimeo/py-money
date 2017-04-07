from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py-money',
    packages=[
        'money'
    ],
    version='0.1.0',
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
        'pytest==3.0.6',
        'babel==2.4.0'
    ],
)
