# -*- coding: utf-8 -*-
"""
Utility functions for using XMM-Newton SAS through Python.

@author: A. Ruiz
"""
import os
import logging
import subprocess
from pathlib import Path


if "SAS_DIR" not in os.environ:
    raise ImportError("SAS has not been initialized in your system!")



def _check_task(task: str):
    sasbin_dir = Path(os.environ["SAS_PATH"], "bin")
    available_tasks = [f.name for f in sasbin_dir.glob("*")]

    if task not in available_tasks:
        raise ValueError(f"Unknown task: {task}")


def _parse_arguments(args, kwargs):
    return list(args) + [f'{key}={value}' for key, value in kwargs.items()]


def _run_command(task: str, args):
    try:
        logging.info(f"Running {task} {' '.join(args)}")
        output = subprocess.check_output([task] + args, stderr=subprocess.STDOUT)
        output = output.decode()
        logging.info(output)

    except subprocess.CalledProcessError as e:
        logging.error(f"Task {task} failed with status {e.returncode}")
        logging.error(e.output.decode())
        output = None

    return output


def run(task: str, *args, **kwargs):
    """
    Wrapper for SAS tasks. 'task' must be the name of a SAS task, and kwargs
    contains all the parameters passed to the task, with the same name.
    """
    _check_task(task)
    args = _parse_arguments(args, kwargs)
    output = _run_command(task, args)

    return output


def sasversion(full=False):
    """
    Returns the SAS version initialized in the system.
    """
    output = run("sasversion", "-v")
    full_version = output.split("-")[2]

    if full:
        return full_version.split("]")[0]
    else:
        return full_version.split(".")[0]
