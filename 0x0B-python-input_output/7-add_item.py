#!/usr/bin/python3
"""
Adds arguments to a python list and save them to a file.
"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_file = "add_item.json"
try:
    items = load_from_json_file(my_file)
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, my_file)
