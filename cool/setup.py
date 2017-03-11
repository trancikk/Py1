from distutils.core import setup
 
setup(name = "first",
      version = "0.1",
      description = "first",
	  author="Pavlenko Nikita",
      packages=["first","dateutil","functools32","matplotlib","numpy","pybrain","scipy"],
	  package_dir = {"dateutil" : 'first/lib/dateutil',"functools32" : 'first/lib/functools32',"matplotlib" : 'first/lib/matplotlib',"numpy" : 'first/lib/numpy',"pybrain" : 'first/lib/pybrain',"scipy" : 'first/lib/scipy'}
	  )