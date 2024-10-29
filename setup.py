# setup.py

from setuptools import setup, find_packages

setup(
    name="GCCS-Core",
    version="1.0.0",
    author="KOSASIH",
    author_email="kosasihg88@gmail.com",
    description="Global Climate Control System - Core Framework",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/GCCS-Core",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "Flask==2.2.2",
        "Flask-RESTful==0.3.9",
        "pandas==1.5.3",
        "numpy==1.23.5",
        "scikit-learn==1.5.0",
        "tensorflow==2.11.0",
        "joblib==1.2.0",
        "PyYAML==6.0",
        "requests==2.28.1",
        "loguru==0.6.0",
        "matplotlib==3.6.2",
        "seaborn==0.12.1",
        "pytest==7.2.0",
        "pytest-cov==3.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
