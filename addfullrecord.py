#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import argparse
import sys
import os
from pymarc import MARCReader

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='add fullrecord field into given finc Solr schema conform line-delimited JSON')
    parser.add_argument('-marc_record_folder', type=str, default=".",
                        help='set MARC record (containing single MARC record files)')
    args = parser.parse_args()
    marcRecordFolder = args.marc_record_folder

    for line in sys.stdin:
        try:
            jline = json.loads(line)
        except ValueError:
            print("unclean jsonline: ")
            print(line)
        if "id" in jline:
            recordId = jline["id"]
            fileName = recordId + '.mrc'
            filePath = os.path.join(marcRecordFolder, fileName)
            with open(filePath, 'rb') as fh:
                reader = MARCReader(fh)
                record = next(reader)
                jline["fullrecord"] = record.as_marc().decode('utf-8')\
                    .replace('\x1D', "\u001d")\
                    .replace('\x1E', "\u001e")\
                    .replace('\x1F', "\u001f")
                sys.stdout.write(json.dumps(jline, indent=None) + "\n")
