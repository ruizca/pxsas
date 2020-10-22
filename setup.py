from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="pysas",
    version="1.0",
    author="Angel Ruiz",
    author_email="angel.ruizca@gmail.com",
    description="Python wrapper for the XMM-Newton Science Analysis System (SAS)",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/ruizca/pysas",
    py_modules=["pysas"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
