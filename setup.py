from setuptools import setup, find_packages

setup(
    name='mail2taskwarrior',
    url='https://github.com/neingeist/mail2taskwarrior',
    author='neingeist',
    author_email='neingeist@bl0rg.net',
    description='add a task to taskwarrior via email',
    scripts=['mail2taskwarrior'],
    install_requires=['taskw >= 1.2.0'],
)
