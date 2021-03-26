from setuptools import setup

setup(
    name = 'FurnitureFactory',
    version = '1.0',
    description = 'Furniture Factory project with factory app',
    author = 'Pranav Meshram',
    author_email = 'pranav.mesrham@globallogic.com',
    packages = ['FurnitureFactory'],
    install_requires = ['django = 2.2.5', 'djangorestframework = 3.13.2', 'pytz = 2021.1', 'sqlparse = 0.4.1'],
    scripts=['manage.py']
)