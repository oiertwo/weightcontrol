__author__ = 'oier'

import os
import setuptools

from pip.req import parse_requirements
requirements_file = 'requirements.txt'

try:
    install_reqs = parse_requirements(requirements_file)
except Exception as exc:
    print('Error reading requirements file at {}'.format(os.path.abspath(requirements_file)))

setuptools.setup(
    name="WEIGHT CONTROL",
    version="0.0.1",
    url="asmatzen.wordpress.com",
    author="Oier Echaniz",
    author_email="oieretxaniz@gmail.com",
    description="Tests in prostate imaging",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=[str(ir.req) for ir in install_reqs],
    extra_files=['CHANGES.rst', 'LICENSE', 'README.md'],
    scripts=['scripts/scalebreaker'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        ],
    )
