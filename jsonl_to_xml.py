#!/usr/bin/env python3

import json
import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--filename", required=True, help="The input file you'd like to convert")
ap.add_argument("-r", "--root-tag", default="root", help="The root element for the XML document. Default 'root'.")
ap.add_argument("-i", "--item-tag", default="item", help="The tag for each object listed in the XML document. Default 'item'.")
ap.add_argument("-o", "--output-filename", required=False, help="The output file name.  Defaults to replacing json extension with xml.")
ap.add_argument("-b", "--blacklisted-fields", help="Colon delimited list of fields you want to exclude.  Can't be used with whitelisted fields.")
ap.add_argument("-w", "--whitelisted-fields", help="Colon delimited list of the only fields you want.  Trumps blacklisted fields.")
ap.add_argument("-m", "--mapping-csv-filename", help="Location of CSV with `from` and `to` columns to remap field names.")
args = ap.parse_args()

input_file = open(args.filename)
current_line = input_file.readline()
json_object = json.loads(current_line.strip())

mappings = {}
reverse_mappings = {}
if args.mapping_csv_filename:
    mapping_csv = csv.DictReader(open(args.mapping_csv_filename))
    for row in mapping_csv:
        mappings[row['from']] = row['to']
        reverse_mappings[row['to']] = row['from']

fieldnames = []
if args.whitelisted_fields:
    for key in json_object.keys():
        if key in args.whitelisted_fields.split(":"):
            fieldnames.append(mappings.get(key, key))

elif args.blacklisted_fields:
    for key in json_object.keys():
        if key not in args.blacklisted_fields.split(":"):
            fieldnames.append(mappings.get(key, key))
else:
    for key in json_object.keys():
        fieldnames.append(mappings.get(key, key))

root = ET.Element(args.root_tag)

while current_line:
    input_object = json.loads(current_line.strip())
    item = ET.SubElement(root, args.item_tag)
    for key in fieldnames:
        key_tag = ET.SubElement(item, key)
        key_tag.text = input_object[reverse_mappings.get(key, key)]
    
    current_line = input_file.readline()

input_file.close()
tree = ET.ElementTree(root)
output_filename = args.output_filename if args.output_filename else f'{args.filename.replace(".json", "")}.xml'
xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml()
with open(output_filename, "w", encoding='utf-8') as f:
    f.write(xmlstr)


