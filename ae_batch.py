"""
Usage: ae_batch [-i input_file_name] [-o output_file_name] [-e error_file_name] [-a api_key] mms_id_list_file_name

ae_batch accepts a plain text file with one bibliographic MMS ID per line.
"""

from settings import api_key, input_file, output_file, error_file, base_url
from AE import fetch, update
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output-file')
parser.add_argument('-i', '--input-file')
parser.add_argument('-e', '--error-file')
parser.add_argument('-a', '--api-key')
parser.add_argument('mms_id_file')
args = parser.parse_args()

if args.output_file is not None:
    output_file = args.output_file

if args.input_file is not None:
    input_file = args.input_file

if args.error_file is not None:
    error_file = args.error_file

if args.api_key is not None:
    api_key = args.api_key

mms_id_list = []
with open(args.mms_id_file, 'r') as fh:
    for line in fh:
        mms_id_list.append(line.strip())

for mms_id in mms_id_list:
    fetch(mms_id, output_file, error_file, api_key, base_url)
    update(mms_id, input_file, api_key, base_url)