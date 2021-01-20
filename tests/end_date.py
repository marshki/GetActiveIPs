#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Placeholder.
"""

import unittest
from datetime import date

def end_date():
    """Today's date.
    Returns:
      month/date/year, e.g. 12/31/1999
    """
    return date.today().strftime("%x")

print(end_date())

#class EndDateTest(unittest.TestCase):
    """Unit tests.
    """
#https://docs.python.org/3/library/unittest.mock-examples.html#partial-mocking

