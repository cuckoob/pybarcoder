import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), "r", encoding='utf-8') as fh:
    LONG_DESCRIPTION = fh.read()

DESCRIPTION = (
    'pybarcoder base on python-barcode'
)
CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
    'Programming Language :: Python :: 3.6'
]
KEYWORDS = (
    'barcode barCoder'
)

setup(
    name='pybarcoder',
    version='0.6.13',
    maintainer='Murray',
    maintainer_email='murray.ma@h3c.com',
    url='https://github.com/murray-ma/pybarcoder',
    download_url='https://github.com/murray-ma/pybarcoder',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license='MIT',
    platforms='Platform Independent',
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=[
        'barcode==1.0.1',
        'python-barcode==0.11.0',
        'pillow>=7.1.2'
    ],
)
