""" Brief description of what the script does """

import argparse

def main(args):
    """run the programe"""
    print('Input file:', args.infile)
    print('Output file:', args.outfile)


if __name__ == '__main__':
    USAGE = 'Brief description of what the script does'
    parser = argparse.ArgumentParser(description=USAGE)
    parser.add_argument('infile', type=str, help='input file name')
    parser.add_argument('outfile', type=str, help='output file name')
    args = parser.parse_args()
    main(args)
