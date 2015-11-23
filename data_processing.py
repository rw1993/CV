# -*- coding:utf-8 -*-
import json


def process_data(f, examples):
    example = json.loads(f)
    # TODO processing example

    examples.append(example)


if __name__ == "__main__":
    examples = []
    with open("practice.json", "r") as f:
        for f in f.readlines():
            process_data(f, examples)
            
    
