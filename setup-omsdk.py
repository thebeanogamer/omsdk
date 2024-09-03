"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
import sys
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
# Get the version from _version file 
with open('/tmp/_version.txt', 'r') as v:
    ver = v.read()

# conditional dependency:include enum34 if python 2 is in use
debug_l1_en = False

setup(
    name='omsdk',
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=ver,

    description='Dell OpenManage SDK',
    long_description='Dell OpenManage SDK for devices, consoles',

    # The project's main homepage.
    url='https://support.dell.com',

    # Author details
    author='Dell Technologies',
    author_email='OpenManageSDK@Dell.com',

    # Choose your license
    license='Apache Software License',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords='dellemc, dellemcsdk, idrac, cmc',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=[
        'omsdk',
        'omsdk.version',
        'omsdk.catalog',
        'omsdk.http',
        'omsdk.lifecycle',
        'omsdk.listener',
        'omsdk.profiling',
        'omsdk.reflection',
        'omsdk.simulator',
        'omsdk.typemgr',
        'omsdk.omlogs',
        'omsdk.omlogs.config',
        'omsdk.services',
        'omdrivers',
        'omdrivers.lifecycle',
        'omdrivers.lifecycle.iDRAC',
        'omdrivers.enums',
        'omdrivers.enums.iDRAC',
        'omdrivers.helpers',
        'omdrivers.helpers.iDRAC',
        'omdrivers.types',
        'omdrivers.types.iDRAC',
    ],

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        "enum34; python_version<'3.4'",
        "requests>=2.12.3",
        "PyYAML>=3.12",
        "pysnmp_mibs>=0",
        "ipaddress>=0"
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_dir= {
        'omdrivers' : 'omdrivers',
        'omsdk' : 'omsdk'
    },
    package_data={
        'omdrivers': [
                'iDRAC/*.Monitor',
                'iDRAC/Config/*',
                'CMC/*.Monitor'
        ],
        'omsdk': [
                'omlogs/config/*',
                'services/config/*'
        ],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[
    ],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
    },
)
