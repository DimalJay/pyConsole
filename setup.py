from setuptools import setup, find_packages
 
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]
 
setup(
    name='piconsole',
    version='0.0.1',
    description='This is a Terminal Widget Library, including Terminal Progresbar Send version',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',  
    author='Dimal Jay',
    author_email='dimalkavindujay@gmail.com',
    license='MIT', 
    classifiers=classifiers,
    keywords='console', 
    packages=find_packages(),
    install_requires=[''] 
)