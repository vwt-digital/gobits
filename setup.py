from setuptools import setup

setup(
    name='gobits',
    version='0.1',
    description='Small Python package to add GCP metadata to messages',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vwt-digital/gobits',
    author='VWT Digital',
    author_email='support@vwt.digital',
    license='GPLv3+',
    packages=['gobits'],
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
