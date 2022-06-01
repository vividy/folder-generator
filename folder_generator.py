#!/usr/bin/env python3

import os
import errno
import csv
import argparse

SUCCESS = "\033[92m"
FAIL = "\033[91m"
END = "\033[0m"

parser = argparse.ArgumentParser()
parser.add_argument('-i', "--input", help='Path to input csv file. Required', required=True)
parser.add_argument('-c', "--column", default="product_name", help="Column name where file product are stored. Default: 'product_name'")
parser.add_argument('-n', "--newline", default="\n", help="Csv newline delimiter. Default: '\\n'")
parser.add_argument('-d', "--delimiter", default=";", help="Csv column delimiter. Default: ';'")
parser.add_argument('-o', "--output", default='.' , help="Path where folders are created. Default: '.'")
args = parser.parse_args()

with open(args.input, newline=args.newline) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=args.delimiter)
    for row in reader:
        print(f"Creating '{args.output}/{row[args.column]}'")
        try:
            os.makedirs(f"{args.output}/{row[args.column]}")
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
            pass