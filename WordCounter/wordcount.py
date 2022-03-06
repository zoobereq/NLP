#!/usr/bin/env python

import argparse

def main(args: argparse.Namespace) -> None:
	word_count = 0

	with open(args.file_path, 'r') as f:
		#file_text = f.read()
		for line in f:
			word_count += len(line.split())

	print(f"Word count: {word_count}")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("file_path", help="Enter file path.")

	main(parser.parse_args())
