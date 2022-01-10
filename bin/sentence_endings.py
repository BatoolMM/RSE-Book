'''Cout the punctuation in a text'''

import string
import argparse

def main(args):
    ''' A function that count the punctuation in a file'''
    text = args.infile.read()
    puncs = [".", "!", "?"]
    for punc in puncs:
        count = text.count(punc)
        print(f'Number of {punc} is {count}')


if __name__ == '__main__':
    '''Run the command line progarme'''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("infile", type=argparse.FileType('r'), help='')
    args= parser.parse_args()
    main(args)
