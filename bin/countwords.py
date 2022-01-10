
"""
Count of the occurance of each word in a text
and write them to CSV file
"""
import argparse
import string
from collections import Counter

import utilities as util


def count_words(reader):
    """Count the occurrence of each word in a string"""
    text = reader.read()
    chunks = text.split()
    npunc = [word.strip(string.punctuation) for word in chunks]
    lower_list = [word.lower() for word in npunc]
    count = Counter(lower_list)
    return count

def main(args):
    """Run teh command line Progarme"""
    word_counts = count_words(args.infile)
    util.collection_to_csv(word_counts, num=args.num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="__doc__")
    parser.add_argument("infile", type=argparse.FileType('r'), nargs='?', default='-', help="Add the input text file")
    parser.add_argument("-n","--num", default=None, type=int, help="Add the number of words")
    args = parser.parse_args()
    main(args)
