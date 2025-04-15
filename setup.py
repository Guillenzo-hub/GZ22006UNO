from setuptools import setup, find_packages

setup(
    name='ecuaciones',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['numpy'],
    author='Carlos Roberto Guillen Zometa GZ22006',
    author_email='GZ22006@ues.edu.sv',
    url='https://github.com/Guillenzo-hub/GZ22006UNO.git',
    description='Librería para resolver sistemas de ecuaciones lineales y no lineales utilizando metodos vistos en clases',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
