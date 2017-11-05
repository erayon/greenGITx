from setuptools import setup


with open('README.md') as f:
	long_description = f.read()

setup(
     name='greenGITx',    
     version='0.1', 
     description='Go green all month in GIT contribution',
     long_description = long_description,
     author_email='ayon.mi1@iiitmk.ac.in',
     author = "Ayon Saha",  
     url= "https://github.com/erayon/greenGITx",  
     scripts=['gdot.py'], 
     license= 'GPL',
 )
 

