import os

from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='gobits',
    version=os.environ['TAG_NAME'],
    description='Small Python package to add GCP metadata to pub/sub messages',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vwt-digital/gobits',
    author='VWT Digital',
    author_email='support@vwt.digital',
    license='GPLv3+',
    packages=['gobits'],
    install_requires=install_requires,
    test_suite="tests",
    tests_require=["Werkzeug==1.0.1"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering'
    ]
)
