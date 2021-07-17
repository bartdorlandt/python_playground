#!/usr/bin/python3
import textfsm
from tabulate import tabulate
import os
from local_lib import *

# documentation:
# https://github.com/google/textfsm/wiki/TextFSM
# https://pyneng.readthedocs.io/en/latest/book/21_textfsm/textfsm_examples.html

status = os.path.join('TextFSM', 'sh_ip_route_ospf.txt')
tpl = os.path.join('TextFSM', 'sh_ip_route_ospf.textfsm')

with open(tpl) as f, open(status) as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(result)
    print(tabulate(result, headers=header))

# output:
# network      mask    distance    metric  nexthop
# ---------  ------  ----------  --------  ---------------------------------------
# 10.1.1.0       24         110        20  ['10.0.12.2']
# 10.2.2.0       24         110        20  ['10.0.13.3']
# 10.3.3.3       32         110        11  ['10.0.12.2']
# 10.4.4.4       32         110        11  ['10.0.13.3', '10.0.14.4']
# 10.5.5.5       32         110        21  ['10.0.13.3', '10.0.12.2', '10.0.14.4']
# 10.6.6.0       24         110        20  ['10.0.13.3']
