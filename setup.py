from setuptools import setup
long_description = "[Documentation](http://github.com/Ehnryu/buildproject)"
setup(name='buildproj',
      version='0.6.8',
      description='Alternative to make',
      url='http://github.com/Ehnryu/buildproject',
      author='Ehnryu/Sakurai07',
      author_email='blzzardst0rm@gmail.com',
      license='MIT',
      packages=['buildproj'],
      long_description=long_description,
      long_description_content_type="text/markdown",
      entry_points={
        'console_scripts': [
            'build = buildproj.cli:start',
        ],
    },
    install_requires=[
        'tqdm',
        'bashflags.py'
        ],
    keywords=['build', 'make',"project"],
    classifiers=["Programming Language :: Python :: 3"],
      zip_safe=False)