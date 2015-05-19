import os
from setuptools import setup, find_packages

__version__ = "0.2.4"

#requirements.txt
with open('requirements.txt') as f:
  required = f.read().splitlines()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = "myql-cli",
  version = __version__,
  description = "Python Wrapper for the Yahoo ! Query Language",
  long_description = read("README.rst"),
  author = "Josue Kouka",
  author_email = "josuebrunel@gmail.com",
  url = "https://github.com/josuebrunel/myql-cli",
  download_url = "https://github.com/josuebrunel/myql-cli/archive/{0}.tar.gz".format(version),
  packages = find_packages(),
  platforms=['Any'],
  license='MIT',
  install_requires = required,
  scripts=['myql-cli.py']
)
