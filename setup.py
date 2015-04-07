from setuptools import setup, find_packages

#requirements.txt
with open('requirements.txt') as f:
  required = f.read().splitlines()

setup(
  name = "myql-cli",
  version = "0.2.3",
  description = "Python Wrapper for the Yahoo ! Query Language",
  long_description = "",
  author = "Josue Kouka",
  author_email = "josuebrunel@gmail.com",
  url = "https://github.com/josuebrunel/myql-cli",
  packages = find_packages(),
  platforms=['Any'],
  license='MIT',
  install_requires = required,
  scripts=['myql-cli.py']
)
