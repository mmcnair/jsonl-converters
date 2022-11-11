#!/usr/bin/env python3

import json
import csv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input-filename", required=True, help="The input file you'd like to convert")
ap.add_argument("-o", "--output-filename", help="The output file name.  Defaults to replacing json extension with csv.")
ap.add_argument("-b", "--blacklisted-fields", help="Colon delimited list of fields you want to exclude.  Can't be used with whitelisted fields.")
ap.add_argument("-w", "--whitelisted-fields", help="Colon delimited list of the only fields you want.  Trumps blacklisted fields.")
ap.add_argument("-m", "--mapping-csv-filename", help="Location of CSV with `from` and `to` columns to remap field names.")
args = ap.parse_args()

input_file = open(args.input_filename)
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

output_filename = args.output_filename if args.output_filename else f'{args.input_filename.replace(".json", "")}.csv'
output_file = open(output_filename, 'w', encoding='utf-8')
output_csv = csv.DictWriter(output_file, fieldnames=fieldnames, dialect="excel")
output_csv.writeheader()

while current_line:
    output_object = {}
    input_object = json.loads(current_line.strip())
    for key in fieldnames:
        output_object[key] = input_object[reverse_mappings.get(key, key)]
    
    output_csv.writerow(output_object)
    current_line = input_file.readline()

input_file.close()
output_file.close()