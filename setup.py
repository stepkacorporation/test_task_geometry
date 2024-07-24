from setuptools import setup, find_packages

setup(
    name="geometry",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'dev': ['unittest']
    },
    author="Kornev Stepan",
    description="A library for calculating the area of various shapes",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
