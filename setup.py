from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='collective.castle',
      version=version,
      description="Plone UI for CAS login.",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zope plone CAS PAS',
      author='Derek Richardson',
      author_email='plone@derekrichardson.net',
      url='',
      license='',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
