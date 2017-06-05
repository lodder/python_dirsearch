from setuptools import setup

setup(
    name='dirsearch',
    packages=['dirsearch'],
    version='1.0.3',
    description='A simple wrapper to perform a case-insensitive wildcard directory search',
    author='Shaun Lodder',
    author_email='shaun.lodder@gmail.com',
    url='https://github.com/lodder/python_dirsearch',
    keywords=['directory search wildcard'],
    classifiers=[],
    install_requires=[
    ],
    extras_require={
        'develop': ['nose']
    }
)
