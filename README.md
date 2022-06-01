# folder-generator

This script is a tools which generate folders from a column in a CSV.

## Prerequisites

- Python 3.6 or higher
    - https://www.python.org/downloads/


## Usage
```
usage: folder_generator.py [-h] -i INPUT [-c COLUMN] [-n NEWLINE] [-d DELIMITER] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to input csv file. Required
  -c COLUMN, --column COLUMN
                        Column name where file product are stored. Default: 'product_name'
  -n NEWLINE, --newline NEWLINE
                        Csv newline delimiter. Default: '\n'
  -d DELIMITER, --delimiter DELIMITER
                        Csv column delimiter. Default: ';'
  -o OUTPUT, --output OUTPUT
                        Path where folders are created. Default: '.'
```
## Exemple

```
./folder_generator.py -i ./exemple.csv -o test
```

## Troubleshoot

- Error "env: python3: No such file or directory"
    - Python3 is not installed in default path
    - try: 'python3 ./folder_generator.py -i ./exemple.csv -o test'