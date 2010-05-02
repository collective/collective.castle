import os
from setuptools import setup, find_packages

version = '1.1'


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
      author='Derek Richardson/Plone Community',
      author_email='product-developers@lists.plone.org',
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
          'rwproperty',
          'Products.CAS4PAS',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
