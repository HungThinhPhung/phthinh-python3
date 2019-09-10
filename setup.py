from setuptools import setup
from sphinx.environment.collectors import dependencies

setup(
    name='phthinh',
    version='0.2',
    packages=[
        'phthinh',
        'phthinh.pattern',
        'phthinh.util'
    ],
    url='',
    license='MIT',
    author='phthinh',
    author_email='hungthinhphung1996@gmail.com',
    description='Most Frequently Used Python3 Code of Hung Thinh Phung',
    install_requires=[
        'requests',
        'flask',
    ]
)

