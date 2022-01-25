# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 01 (Modules)
# PROBLEM NUMBER: 1a

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'constants.py'
POINTS = 2

def test_pi():
    return _test_variable("pi", 3.141592653589793,
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )
