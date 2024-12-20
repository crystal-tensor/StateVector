from setuptools import setup, find_packages

setup(
    name='statevector',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'scikit-learn',
    ],
    entry_points={
        'console_scripts': [],
    },
    author='crystal-tensor',
    author_email='your.email@example.com',
    description='A vector database optimized for cosine similarity using quantum algorithms',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/crystal-tensor/StateVector',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
