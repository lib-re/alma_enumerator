from settings import api_key, mms_id, input_file, base_url
from AE import update
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mms-id')
parser.add_argument('-i', '--input-file')
parser.add_argument('-a', '--api-key')
args = parser.parse_args()

if args.mms_id is not None:
    mms_id = args.mms_id

if args.input_file is not None:
    input_file = args.input_file

if args.api_key is not None:
    api_key = args.api_key

update(mms_id, input_file, api_key, base_url)