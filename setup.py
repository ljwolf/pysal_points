from setuptools import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(name='pointpats',
      version='1.0.0dev',
      description='Methods and Functions for planar point pattern analysis',
      url='https://github.com/pysal/pointpats',
      maintainer='Hu Shao',
      maintainer_email='shaohutiger@gmail.com',
      test_suite = 'nose.collector',
      tests_require=['nose'],
      keywords='spatial statistics',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: GIS',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
        ],
      license='3-Clause BSD',
      packages=['pointpats'],
      install_requires=['numpy', 'scipy', 'matplotlib', 'pysal_core'],
      zip_safe=False,
      cmdclass = {'build.py':build_py})
