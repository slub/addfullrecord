# addfullrecord

add fullrecord field into given finc Solr schema conform line-delimited JSON

## requirement

pymarc

### install pymarc

1. (optionally) install easy_install3:

    sudo apt-get install python3-setuptools

2. (optionally) install pip for python 3.x:

    sudo easy_install3 pip

3. install pymarc with pip (e.g. pip3.5):

    sudo -H pip3.5 install pymarc

## usage

    addfullrecord.py [-h] [-marc_record_folder MARC_RECORD_FOLDER]

optional arguments:

    -h, --help            show this help message and exit
    -marc_record_folder MARC_RECORD_FOLDER set MARC record (containing single MARC record files)

### usage example

    ./addfullrecord.py -marc_record_folder [PATH TO YOUR MARC RECORD FOLDER CONTAINING SINGLE MARC RECORD FILES] < [PATH TO YOUR FINC SOLR SCHEMA CONFORM LINE-DELIMITED JSON FILE] > [PATH TO THE RESULT FINC SOLR SCHEMA CONFORM LINE-DELIMITED JSON FILE]
