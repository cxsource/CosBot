import os
import re
import sys

from io import open

from setuptools import setup, find_packages

# ------------------------------------------------------------------------------- #
    
with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()

# ------------------------------------------------------------------------------- #

setup(
    name = 'helheim',
    author = 'VeNoMouS',
    author_email = 'venom@gen-x.co.nz',
    version='0.8.7',
    packages = find_packages(exclude=['tests*']),
    description = 'A Python module to combat anti-bot technology.',
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords = [
        'cloudflare',
        'scraping',
        'ddos',
        'scrape',
        'webscraper',
        'anti-bot',
        'waf',
        'iuam',
        'bypass',
        'challenge',
        'kasada',
        'slowAES'
    ],
    include_package_data = True,
    package_data={
        'helheim': [
            '*.so',
            '*.dll',
            '*.pyd',
        ]
    },
    install_requires = [
        'brotli >= 1.0.9',
        'cloudscraper >= 1.2.58',
        'cryptography >= 3.4.7',
        'Pillow >= 8.2.0',
        'requests >= 2.25.1',
        'urllib3 >= 1.26.4',
        'python-dateutil >= 2.8.1'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

# ------------------------------------------------------------------------------- #

