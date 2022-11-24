# -*- coding: utf-8 -*-
"""
Utility functions for using XMM-Newton SAS through Python.

@author: A. Ruiz
"""
import os
import logging
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)


if "SAS_DIR" not in os.environ:
    raise ImportError("SAS has not been initialized in your system!")


class PxsasError(RuntimeError):
    pass


def _check_task(task: str):
    sasbin_dir = Path(os.environ["SAS_PATH"], "bin")
    available_tasks = [f.name for f in sasbin_dir.glob("*")]

    if task not in available_tasks:
        raise ValueError(f"Unknown task: {task}")


def _parse_arguments(args, kwargs):
    return list(args) + [f'{key}={value}' for key, value in kwargs.items()]


def _run_command(task: str, args, level, raise_error):
    try:
        logger.log(level, "Running %s...", task)
        output = subprocess.check_output([task] + args, stderr=subprocess.STDOUT)
        output = output.decode()
        logger.log(level, output)

    except subprocess.CalledProcessError as e:
        logger.error(f"Task {task} failed with status {e.returncode}.")
        logger.error(e.output.decode())
        output = None

        if raise_error:
            raise PxsasError("Error running SAS. Check log for details.")

    return output


def run(task: str, *args, verbosity_level=logging.INFO, raise_error=True, **kwargs):
    """
    Wrapper for SAS tasks. 'task' must be the name of a SAS task, and kwargs
    contains all the parameters passed to the task, with the same name.
    """
    _check_task(task)
    args = _parse_arguments(args, kwargs)
    output = _run_command(task, args, verbosity_level, raise_error)

    return output


def sasversion(full=False):
    """
    Returns the SAS version initialized in the system.
    """
    output = run("sasversion", "-v", verbosity_level=0)
    full_version = output.split("-")[2]

    if full:
        return full_version.split("]")[0]
    else:
        return full_version.split(".")[0]
