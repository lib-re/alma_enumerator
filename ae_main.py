from settings import api_key, mms_id, output_file, error_file, input_file, base_url
from AE import fetch, update
from subprocess import run
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('command', help="Options: gui, fetch, update, batch")
parser.add_argument('-m', '--mms-id')
parser.add_argument('-o', '--output-file')
parser.add_argument('-i', '--input-file')
parser.add_argument('-e', '--error-file')
parser.add_argument('-a', '--api-key')
parser.add_argument('mms_id_file', nargs='?')
args = parser.parse_args()

if args.mms_id is not None:
    mms_id = args.mms_id

if args.output_file is not None:
    output_file = args.output_file

if args.input_file is not None:
    input_file = args.input_file

if args.error_file is not None:
    error_file = args.error_file

if args.api_key is not None:
    api_key = args.api_key

if args.command == 'gui':
    run('ae_gui')

if args.command == 'fetch':
    fetch(mms_id, output_file, error_file, api_key, base_url)

if args.command == 'update':
    update(mms_id, input_file, api_key, base_url)

if args.command == 'batch':
    run(['ae_batch', '-i', input_file, '-o', output_file, '-e', error_file, '-a', api_key, args.mms_id_file])