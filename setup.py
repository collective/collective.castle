from setuptools import setup, find_packages
import sys, os

version = '1.0.1'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()
    
setup(name='collective.castle',
      version=version,
      description="Plone UI for CAS login.",
      long_description=read('README.txt'),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zope plone CAS PAS',
      author='Derek Richardson',
      author_email='plone@derekrichardson.net',
      url='https://svn.plone.org/svn/collective/collective.castle',
      license='GPL',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Products.CAS4PAS',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
