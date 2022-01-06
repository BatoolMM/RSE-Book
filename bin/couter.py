
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

def main(args):
    with open(args.infile, 'r') as reader:
        word_counts = count_words(reader)
    collection_to_csv(word_counts, num=args.num)


if __name__ =='__main__':
    parser = argparse.ArgumentParser(description="Count Words in a file")
    parser.add_argument("infile", type=str, help="Add the input text file")
    parser.add_argument("_n","__num", default=None, type=int, help="Add the number of words")
    args = parser.parse_args()
    main(args)
