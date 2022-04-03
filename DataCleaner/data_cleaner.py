#!/usr/bin/env python 

import argparse
import re

def text_cleaner(input_file_path:str, output_file_path:str) -> None:
    with open(input_file_path, 'r') as source, open(output_file_path, 'w') as sink:
        for line in source:
            line = line.casefold().strip()
            line = re.sub(r'[^A-Za-z0-9 ]+', '', line)
            print(line, file = sink)

def main(args: argparse.Namespace) -> None:
    text_cleaner(args.input, args.output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="path to input file")
    parser.add_argument("output", help="path to output file")
    main(parser.parse_args())

