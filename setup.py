import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
    name = 'kata2angka',
    packages = ['kata2angka'],  # this must be the same as the name above
    version = '0.1',
    license=open('LICENSE.txt').read(),
    description = 'Konversi kata ke nomor.',
    author = 'Herman Sugi Harto',
    author_email = 'hermansh.id@gmail.com',
    url = 'hermansh.my.id',  # use the URL to the github repo
    keywords = ['numbers', 'convert', 'words', 'indonesia'],  # arbitrary keywords
    classifiers = [
        'Intended Audience :: Developers',
        'Programming Language :: Python'
    ],
    long_description=open_file('README.md').read()
)