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
after the initialization of SAS. You can install pxsas in this environment, but this
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

    >>> import logging
    >>> import os
    >>> import pxsas

    >>> logging.getLogger().setLevel(logging.INFO)

    # Show SAS version used by pxsas
    >>> pxsas.sasversion(full=True)
    INFO:root:Running sasversion -v
    INFO:root:sasversion (sasversion-1.3) [xmmsas_20190531_1155-18.0.0]

    '18.0.0'

    # Show the version of the task 'evselect'
    >>> pxsas.run("evselect", "-v")

    # Create a Calibration Index File for a given observation
    # Raise exception if the task fails
    >>> os.environ["SAS_ODF"] = "/path/to/observation/ODF"
    >> pxsas.run("cifbuild", calindexset="ccf.cif")

    # Create a Calibration Index File for a given observation
    # Returns None if the task fails
    >>> os.environ["SAS_ODF"] = "/path/to/observation/ODF"
    >>> pxsas.run("cifbuild", calindexset="ccf.cif", raise_error=False)


The output messages from the SAS tasks are captured through the python logging system.
If the task runs succesfully, ``pxsas.run`` returns the output text as a string. By
default, if an error happens during execution, and exception is raised. If the keyword
argument ``raise_error`` is set to False, then no exception is raised and it just returns
``None``.



.. _SAS: https://www.cosmos.esa.int/web/xmm-newton/what-is-sas
.. _installation: https://www.cosmos.esa.int/web/xmm-newton/sas-installation
