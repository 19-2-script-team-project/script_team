from distutils.core import setup
files = ["images/*","tierImg/*","UI/*"]
setup(name = 'LOLSearch',
      version = '1.0',
      packages = ['package'],
      package_data = {'package' : files },
)
