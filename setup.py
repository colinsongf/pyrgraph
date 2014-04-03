from setuptools import setup

setup(
    name='pyrgraph',
    version='0.1.2',
    description='Pyrgraph is a Redis-backed graph database',
    url='http://github.com/alireza-m/pyrgraph',
    author='Alireza Meskin',
    author_email='alireza.meskin@gmail.com',
    license='MIT',
    packages=['pyrgraph'],
    zip_safe=False,
    install_requires=[
        "redis > 2.9.0"
    ]
)
