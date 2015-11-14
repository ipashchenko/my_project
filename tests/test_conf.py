#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for my_project.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""
from __future__ import absolute_import, division, print_function

import pytest
import my_project


def test_fib():
    assert my_project.skeleton.fib(1) == 1
    

def test_one():
    return True


def test_two():
    return True
