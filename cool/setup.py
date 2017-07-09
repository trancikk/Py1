from distutils.core import setup
 
setup(name = "first",
      version = "0.1",
      description = "first",
	  author="Pavlenko Nikita",
      packages=["first","numpy"],
	  package_dir = {"numpy" : 'first/numpy'}
	  )