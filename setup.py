#!/usr/bin/env python
import os
import sys
import json
import subprocess 

from distutils.core import setup


if __name__ == "__main__":
    setup(name="ray",
          version='0.1',
          description='Simulated diagnostic package for FLASH',
          author='Anthony Scopatz',
          author_email='scopatz@gmail.com',
          url='http://flash.uchicago.edu/',
          packages=['ray']
          )
