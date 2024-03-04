#!/usr/bin/env python
import re

sdwan_templates = [
    {
        "deviceType": "dev_type",
        "configType": "template",
        "templateId": "random_template_id_5",
    },
    {
        "deviceType": "dev_type",
        "configType": "template",
        "templateId": "random_template_id_1",
    },
    {
        "deviceType": "dev_type",
        "configType": "template",
        "templateId": "random_template_id_2",
    },
]

vedge_template_ids = ["random_template_id_1", "random_template_id_2"]

used_templates = set(map(lambda template: template["templateId"], sdwan_templates))

list_tpls = [d for d in sdwan_templates if d["templateId"] in vedge_template_ids]

with_re = [d for d in sdwan_templates if re.match(r"^random_template_id_[1,2]", d["templateId"])]
# [{'deviceType': 'dev_type', 'configType': 'template', 'templateId': 'random_template_id_1'}, {'deviceType': 'dev_type', 'configType': 'template', 'templateId': 'random_template_id_2'}]
