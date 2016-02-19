from setuptools import setup
from os.path import join, dirname
import sys
extra = {}
if sys.version_info >= (3, ):
    extra['use_2to3'] = True

description = open(join(dirname(__file__), 'README.rst')).read()

setup(
    name='demultipart',
    version='0.2',
    author='Vincent Pelletier',
    author_email='plr.vincent@gmail.com',
    description=next(x for x in description.splitlines() if x.strip()),
    long_description='.. contents::\n\n' + description,
    url='http://github.com/vpelletier/demultipart',
    license='GPL 2+',
    platforms=['any'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    py_modules=['demultipart'],
    entry_points = {
        'console_scripts': [
            'demultipart=demultipart:main',
        ],
    },
    zip_safe=True,
    **extra
)
