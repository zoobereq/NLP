#!/usr/bin/env python

import argparse
from helpers import reader, writer 

def main(args: argparse.Namespace) -> None:
    totalLength = len(reader(args.input))
    writer(args.train, reader(args.input)[:int(totalLength * 0.8)]) # outputs the train file (80% of the data)
    writer(args.dev, reader(args.input)[int(totalLength * 0.8):int(totalLength * 0.9)]) # outputs the dev file (10% of the data)
    writer(args.test, reader(args.input)[int(totalLength * 0.9):]) # outputs the test file (the other 10% of the data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help = "Path for input file")
    parser.add_argument("train", help = "Path for the output train file")
    parser.add_argument("dev", help = "Path for the output dev file")
    parser.add_argument("test", help = "Path for the output test file")
    main(parser.parse_args())
