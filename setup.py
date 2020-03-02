from setuptools import setup

setup(name='faoconnector',
      version='0.1',
      description='connector for FA)',
      url='http://github.com/moldingtofu/faoconnector',
      author='',
      author_email='',
      license='MIT',
      packages=['faoconnector'],
      install_requires=['requests','os','zipfile'],
      #dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0']
      zip_safe=False)
