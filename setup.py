from setuptools import setup
from bendercito import __version__

setup(name='bendercito',
      version=__version__,
      description="Change your Slack status from command-line.",
      long_description=open('README.md').read(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Utilities'
      ],
      keywords='',
      author=u'Quique Porta',
      author_email='quiqueporta@gmail.com',
      url='https://github.com/quiqueporta/bendercito',
      download_url='https://github.com/quiqueporta/bendercito/releases',
      license='MIT',
      packages=['bendercito'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[line for line in open('requirements.txt')],
      entry_points={
          'console_scripts': [
              'bendercito = bendercito.bendercito:main'
          ]
      })
