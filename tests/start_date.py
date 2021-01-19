#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
from dateutil.relativedelta import relativedelta

def start_date():
    """Date six (6) months prior to today.
    Returns:
      month/date/year, e.g. 12/31/1999
    """
    return (date.today() + relativedelta(months=-6)).strftime("%x")
