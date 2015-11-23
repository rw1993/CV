# -*- coding:utf-8 -*-
import json


with open("practice.json", "r") as f:
    es = []
    for e in f.readlines():
        es.append(json.loads(e))
        print len(es)

