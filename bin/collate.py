"""
Combine multiple word cpunt in CSV format
into a single CSV File
"""

import csv
import argparse
from collections import Counter

import utilities as utli

def update_counts(reader, word_counts):
    """upadte the count from a file with another reader"""
    for word, count in word_counts:
        word_counts[word] += int(count)


def main(args):
    """Run the command line tool"""
    word_counts = Counter()
    for fname in args.infile:
        with open(fname, 'r') as reader:
            update_counts(reader, word_counts)
    utli.collection_to_csv(word_counts, num=args.num)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=str, nargs='*', help = 'input file name')
    parser.add_argument('-n', '--num', type=int, default= None, help= 'Output n most frquent words')
    args = parser.parse_args()
    main(args)
