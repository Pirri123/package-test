
from distutils.core import setup
setup(
  name = 'package-test',         
  packages = ['package-test'],  
  version = '0.1',     
  license='MIT',        
  description = 'test for uploading packages to pypi',  
  author = 'Ernesto Ramirez-Sayago',                  
  author_email = 'rs.ernesto1@gmail.com',     
  url = 'https://github.com/Pirri123/package-test/edit/master/README.md',  
  download_url = 'https://github.com/Pirri123/package-test/archive/v0.1.tar.gz', 
  keywords = ['test'],   
  install_requires=[ ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
