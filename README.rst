pxsas
=====
.. inclusion-marker-main-readme

``pxsas`` is a simple Python 3 wrapper for the 
XMM-*Newton* Science Analysis System (`SAS`_). 

Dependencies
------------

``pxsas`` needs a working SAS `installation`_. SAS has to be initialized
before importing ``pxsas`` into your python environment.

*A note about SAS 17.0.0 and above*

Starting with version 17.0.0, the SAS installation procedure creates its own python 
environment for running some tasks. This is the system's default python environment 
after the initialization of SAS. You can install pysas in this environment, but this
is extremely NOT recomended. Instead, you can redefine your PATH after SAS
initialization like this (in bash)::

    export PATH="/path/to/my/python:$PATH"

Installation
------------

``pxsas`` can be easily installed using ``pip``::

    pip install pxsas

Example
-------
A simple example of using ``pxsas``::

    import os
    import pxsas

    # Show SAS version used by pxsas
    pxsas.sasversion(full=True)

    # Show the version of the task 'evselect'
    pxsas.run("evselect", "-v")

    # Create a Calibration Index File for a given observation
    os.environ["SAS_ODF"] = "/path/to/observation/ODF"
    pxsas.run("cifbuild", calindexset="ccf.cif")

The output messages from the SAS tasks are captured through the python logging system. 
If the task runs succesfully, ``pxsas.run`` returns the output text as a string. If an
error happens during execution, it returns ``None``.



.. _SAS: https://www.cosmos.esa.int/web/xmm-newton/what-is-sas
.. _installation: https://www.cosmos.esa.int/web/xmm-newton/sas-installation
