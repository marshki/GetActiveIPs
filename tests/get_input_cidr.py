#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input_cidr():
    """Prompt user for network in CIDR. Strip whitespace.
    Args:
      CIDR
    Returns:
      String, stripped of whitespace, e.g. 128.122.112.0/23
    """
    return input("Enter subnet of interest: ").strip()
