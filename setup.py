from setuptools import setup, find_packages

setup(name='featherduster',
      version='0.4',
      description='An automated cryptanalysis tool',
      url='http://github.com/unicornsasfuel/featherduster',
      author='Daniel "unicornfurnace" Crowley',
      license='BSD',
      #packages=['cryptanalib','feathermodules','featherduster'],
      packages=find_packages(exclude=['examples','tests']),
      install_requires=[
          'pycryptodome',
          'ishell'
      ],
      entry_points = {
         'console_scripts': ['featherduster=featherduster.featherduster:main'],
      },
      zip_safe=False)
