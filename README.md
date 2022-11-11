# JSONL Converters
This project houses some simple scripts to generically convert JSONL files into either CSV or XML.  It currently only supports flat JSON structures and does not support nested arrays or JSON objects.

## JSONL to CSV
```
usage: jsonl_to_csv.py [-h] -i INPUT_FILENAME [-o OUTPUT_FILENAME]
                      [-b BLACKLISTED_FIELDS] [-w WHITELISTED_FIELDS]
                      [-m MAPPING_CSV_FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILENAME, --input-filename INPUT_FILENAME
                        The input file you'd like to convert
  -o OUTPUT_FILENAME, --output-filename OUTPUT_FILENAME
                        The output file name. Defaults to replacing json
                        extension with csv.
  -b BLACKLISTED_FIELDS, --blacklisted-fields BLACKLISTED_FIELDS
                        Colon delimited list of fields you want to exclude.
                        Can't be used with whitelisted fields.
  -w WHITELISTED_FIELDS, --whitelisted-fields WHITELISTED_FIELDS
                        Colon delimited list of the only fields you want.
                        Trumps blacklisted fields.
  -m MAPPING_CSV_FILENAME, --mapping-csv-filename MAPPING_CSV_FILENAME
                        Location of CSV with `from` and `to` columns to remap
                        field names.
```

### example usage
Generates a CSV excluding the `rawhtml` and `value` fields from the output.
```
./jsonl_to_csv.py -i sample.json -b rawhtml|value
```

Generates a CSV including only the `originalurl` and `itemid` fields in the output.
```
./jsonl_to_csv.py -i sample.json -w originalurl:itemid
```

Default usage includes all fields.
```
./jsonl_to_csv.py -i sample.json
```

Customize the name of the output file.
```
./jsonl_to_csv.py -i sample.json -o customized_output_name.csv
```

Customize output fieldnames by providing a field mapping csv file.  Only the fields that need to be renamed need to be provided.  If a mapping does not exist for a field, then the original name will be used.
```
./jsonl_to_csv.py -i sample.json -m mappings.csv
```

## JSONL to XML
```
usage: jsonl_to_xml.py [-h] -f FILENAME [-r ROOT_TAG] [-i ITEM_TAG]
                       [-o OUTPUT_FILENAME] [-b BLACKLISTED_FIELDS]
                       [-w WHITELISTED_FIELDS] [-m MAPPING_CSV_FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        The input file you'd like to convert
  -r ROOT_TAG, --root-tag ROOT_TAG
                        The root element for the XML document. Default 'root'.
  -i ITEM_TAG, --item-tag ITEM_TAG
                        The tag for each object listed in the XML document.
                        Default 'item'.
  -o OUTPUT_FILENAME, --output-filename OUTPUT_FILENAME
                        The output file name. Defaults to replacing json
                        extension with xml.
  -b BLACKLISTED_FIELDS, --blacklisted-fields BLACKLISTED_FIELDS
                        Colon delimited list of fields you want to exclude.
                        Can't be used with whitelisted fields.
  -w WHITELISTED_FIELDS, --whitelisted-fields WHITELISTED_FIELDS
                        Colon delimited list of the only fields you want.
                        Trumps blacklisted fields.
  -m MAPPING_CSV_FILENAME, --mapping-csv-filename MAPPING_CSV_FILENAME
                        Location of CSV with `from` and `to` columns to remap
                        field names.
```
    
### example usage
Generates XML excluding the `rawhtml` and `value` fields from the output.
```
./jsonl_to_xml.py -i sample.json -b rawhtml|value
```

Generates XML including only the `originalurl` and `itemid` fields in the output.
```
./jsonl_to_csv.py -i sample.json -w originalurl:itemid
```

Default usage includes all fields.
```
./jsonl_to_xml.py -i sample.json
```

Customize the name of the output file.
```
./jsonl_to_xml.py -i sample.json -o customized_output_name.xml
```

Customize output fieldnames by providing a field mapping csv file.  Only the fields that need to be renamed need to be provided.  If a mapping does not exist for a field, then the original name will be used.
```
./jsonl_to_xml.py -i sample.json -m mappings.csv
```

Customize root and item tag.
```
./jsonl_to_xml.py -i sample.json -r movies -i movie
```
