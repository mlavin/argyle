import os
import sys

from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''

tests_require = ["mock", ]
if sys.version_info < (2, 7):
    tests_require.append("unittest2")


setup(
    name='argyle',
    version=__import__('argyle').__version__,
    author='Mark Lavin',
    author_email='markdlavin@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/mlavin/argyle',
    license='BSD',
    description=u' '.join(__import__('argyle').__doc__.splitlines()).strip(),
    install_requires=['fabric>=1.1.0', 'jinja2>=2.3', ],
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.rst'),
    test_suite="argyle.tests",
    tests_require=tests_require,
)
