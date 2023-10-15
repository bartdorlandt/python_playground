#!/usr/bin/python3
import re

FILE = "files/apache_logs.txt"
count_dict: dict[str, int] = {}

with open(FILE, "r") as f:
    content = f.readlines()

slash16 = re.compile(r"\d+\.\d+")
ips = [x.split()[0] for x in content]
subnets = [slash16.match(x).group(0) for x in ips]

for subnet in subnets:
    if count_dict.get(subnet):
        count_dict[subnet] += 1
    else:
        count_dict[subnet] = 1

top10_sorted = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)[:10]

for subnet, count in top10_sorted:
    print(f"{count} - {subnet}")
