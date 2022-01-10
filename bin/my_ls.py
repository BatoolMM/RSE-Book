
'''
List the files in a given directory with a given suffix
'''


import glob
import argparse


def main(args):
    '''
    Run the Program
    '''
    dir = args.dir if args.dir[-1]=='/' else args.dir + '/'
    global_input = dir +'/*.' + args.suffix
    all_files = sorted(glob.glob(global_input))
    for items in all_files:
        print(items)

if __name__ == '__main__':
    '''
    Command line tool
    '''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dir', type=str, help='Directory')
    parser.add_argument('suffix', type=str, help='File suffix (e.g. py, sh)')
    args = parser.parse_args()
    main(args)
