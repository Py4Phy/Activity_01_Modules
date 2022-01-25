# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 01 (Modules)
# PROBLEM NUMBER: 1b

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'problem1.py'
POINTS = 2

def test_hbar():
    return _test_variable("hbar", 1.0545718176461565e-34,
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )
