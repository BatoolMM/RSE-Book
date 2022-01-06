
"""
Combine multiple word count CSV-files
into a single cumulative count.
"""

import string
import csv
import sys
from collections import Counter
import argparse


def count_words(reader):
    """Count the occurrence of each word in a string"""
    text = reader.read()
    chunks = text.split()
    npunc = [word.strip(string.punctuation) for word in chunks]
    lower_list = [word.lower() for word in npunc]
    count = Counter(lower_list)
    return count

def collection_to_csv(collection, num=None):
    """Write collection of items and counts in csv format"""
    collection = collection.most_common()
    if num is None:
        num = len(collection)
    writer = csv.writer(sys.stdout)
    writer.writerow(collection[0:num])

def update_counts(reader, word_counts):
    for word, count in csv.reader(reader):
        word_counts[word] += int(count)

def main(args):
    word_counts = Counter()
    for file in args.infile:
        with open(file, 'r') as reader:
            update_counts(reader, word_counts)
    collection_to_csv(word_counts, num=args.num)


if __name__ =='__main__':
    parser = argparse.ArgumentParser(description="Count Words in a file")
    parser.add_argument("infile", type=argparse.FileType('r'), nargs='?', help="Add the input text file")
    parser.add_argument("-n","--num", default=None, type=int, help="Add the number of words")
    args = parser.parse_args()
    main(args)
