#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Thu 30 Jan 08:45:49 2014 CET

from setuptools import setup, find_packages, dist
dist.Distribution(dict(setup_requires=['xbob.blitz']))
from xbob.blitz.extension import Extension

packages = ['bob-ip >= 1.2.2']
version = '2.0.0a0'

setup(

    name='xbob.ip.color',
    version=version,
    description='Color conversion utilities',
    url='http://github.com/bioidiap/xbob.ip.color',
    license='BSD',
    author='Andre Anjos',
    author_email='andre.anjos@idiap.ch',

    long_description=open('README.rst').read(),

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
      'setuptools',
      'xbob.blitz',
      'xbob.io.base',
    ],

    namespace_packages=[
      "xbob",
      "xbob.ip",
      ],

    ext_modules = [
      Extension("xbob.ip.color.version",
        [
          "xbob/ip/color/version.cpp",
          ],
        version = version,
        packages = packages,
        ),
      Extension("xbob.ip.color._library",
        [
          "xbob/ip/color/utils.cpp",
          "xbob/ip/color/rgb_to_gray.cpp",
          "xbob/ip/color/rgb_to_yuv.cpp",
          "xbob/ip/color/rgb_to_hsv.cpp",
          "xbob/ip/color/rgb_to_hsl.cpp",
          "xbob/ip/color/main.cpp",
          ],
        packages = packages,
        version = version,
        ),
      ],

    classifiers = [
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Software Development :: Libraries :: Python Modules',
      ],

    )
