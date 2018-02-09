# addfullrecord

add fullrecord field into given finc Solr schema conform line-delimited JSON

reads a finc Solr schema conform line-delimited JSON (from stdin), (tries to) retrieves the binary MARC record for each record (by a given folder containing single MARC record files (that can be matched by id)), writes the record into the "fullrecord" field and prints out the result to stdout  

## requirements

[argparse](https://docs.python.org/3/library/argparse.html#module-argparse)
[pymarc](https://github.com/edsu/pymarc)

### install requirements

1. (optionally) install [pip](https://pip.pypa.io/) for Python 3.x:

    sudo apt-get install python3-pip

2. install requirements with pip:

    sudo -H pip3 install -r requirements.txt

## usage

    addfullrecord.py [-h] [-marc_record_folder MARC_RECORD_FOLDER]

optional arguments:

    -h, --help            show this help message and exit
    -marc_record_folder MARC_RECORD_FOLDER set MARC record (containing single MARC record files)

### usage example

    ./addfullrecord.py -marc_record_folder [PATH TO YOUR MARC RECORD FOLDER CONTAINING SINGLE MARC RECORD FILES] < [PATH TO YOUR FINC SOLR SCHEMA CONFORM LINE-DELIMITED JSON FILE] > [PATH TO THE RESULT FINC SOLR SCHEMA CONFORM LINE-DELIMITED JSON FILE]
