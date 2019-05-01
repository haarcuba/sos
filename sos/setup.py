from setuptools import setup, find_packages

README = 'Web Application to Send SOS Message'

requires = []
tests_require = [
        'pytest',
        'coverage'
        ]

setup(name='sos',
      version='0.0.1',
      description=README,
      long_description=README,
      package_dir={'': 'source'},
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Yoav Kleinberger',
      author_email="haarcuba@gmail.com",
      packages=find_packages('source'),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points={
          'console_scripts': [ 'sos = sos.main:main' ]
      },
      )
