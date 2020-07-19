"""Setup script form package distribution."""

from setuptools import setup

setup(name='mytrix',
      version='1.0.a',
      description="A Python package for linear algebra focused on the"
      "mathematical user",
      url='https://github.com/THargreaves/mytrix',
      author='Tim Hargreaves',
      author_email='tim.hargreaves@icloud.com',
      license='MIT',
      packages=['mytrix'],
      zip_safe=False)
