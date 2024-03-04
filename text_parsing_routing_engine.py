#!/usr/bin/python3
import os

from tabulate import tabulate

import textfsm
from local_lib import *

# documentation:
# https://github.com/google/textfsm/wiki/TextFSM
# https://pyneng.readthedocs.io/en/latest/book/21_textfsm/textfsm_examples.html

status = os.path.join("TextFSM", "routing_engine_status.txt")
tpl = os.path.join("TextFSM", "routing_engine_status.textfsm")

with open(tpl) as f, open(status) as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(result)
    print(tabulate(result, headers=header))

# output:
# Chassis      Slot  State      Temp    CPUTemp    DRAM  Model
# ---------  ------  -------  ------  ---------  ------  -------
#                 0  Master       39         55    2048  RE-4.0
#                 1  Backup       30         31    2048  RE-4.0
