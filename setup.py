from setuptools import setup

setup(
    name='pyrgraph',
    version='0.1',
    description='Pyrgraph is a Redis-backed graph database',
    url='http://github.com/alireza-m/pyrgraph',
    author='Alireza Meskin',
    author_email='alireza.meskin@gmail.com',
    license='MIT',
    packages=['pyrgraph'],
    zip_safe=False,
    long_description=open('README.md').read(),
    install_requires=[
        "redis > 2.9.0"
    ]
)
