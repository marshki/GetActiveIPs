#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_netid():
    """Prompt user for NetID. Strip case, whitespace.
    Args:
      NetID
    Returns:
      String, stripped of case, whitespace, e.g. nyu007
    """
    return input("Enter NetID: ").lower().strip()
