from distutils.core import setup, Extension
import numpy

module1 = Extension("overfeat",
                    include_dirs = ['../..', numpy.get_include()],
                    library_dirs = ['../..'],
                    libraries = ['TH', 'overfeat'],
                    sources = ['overfeatmodule.cpp'])

setup(name = 'overfeat',
      version = '1.0',
      description = 'Python bindings for overfeat',
      ext_modules = [module1],
      install_requires = ['numpy'])
