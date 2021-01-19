#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
from dateutil.relativedelta import relativedelta

def end_date():
    """Today's date.
    Returns:
      month/date/year, e.g. 12/31/1999
    """
    return date.today().strftime("%x")
