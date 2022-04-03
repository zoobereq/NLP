#!/usr/bin/env python 

import argparse
import re

def text_cleaner(input_file_path: str, output_file_path:str) -> None:
    with open(input_file_path, 'r') as source, open(output_file_path, 'w') as sink:
        for line in source:
            line = re.sub(r'[^\w\s]', '', line).casefold()
            sink.write(line)

def main(args: argparse.Namespace) -> None:
    text_cleaner(args.input, args.output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help = "Path for input file")
    parser.add_argument("output", help = "Path for the output file")
    main(parser.parse_args())

