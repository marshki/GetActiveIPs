#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
import argparse
parser = argparse.ArgumentParser(description="Subnet of interest prompt.")
parser.add_argument("--subnet", help="Subnet of interest in CIDR notation, e.g. 128.122.112.0/23 ")
args = parser.parse_args()
print(args.subnet)
import requests
params = (
    ('start_date', '03/13/2020'),
    ('end_date', '09/13/2020'),
    ('input_cidr', '172.22.86.0/23'),
    ('offset', '1'),
    ('limit', '510'),
    ('sort_field', 'IP_ADDRESS_INT'),
    ('sort_type', 'ASC'),
)
request = requests.get('https://url.derp/download-active-hosts.php',
                        params=params, auth=('username', 'password'))
with open('active_hosts.txt','w') as fd:
    fd.write(request.text)
"""
