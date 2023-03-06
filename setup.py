from setuptools import find_packages, setup

setup(
    name='pypa',
    version='0.1.0', 
    description="Creador de paqutes para Python.",
    author="Jaime Feldman", 
    license='MIT', 
    long_description_content_type='text/markdown',
    url='https://github.com/jaimefeldman/pypa.git',
    packages=find_packages(exclude=('test*', 'testing*')),
    package_data={'': ['*.json']},
    install_requires=[
        'termcolor==2.1.0'
    ],
    entry_points={
        'console_scripts': [
            'pypa = launcher.__main__:main',
        ]
    },
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: Linux",
     ],
)

