
''' Ploting words counts'''

import pandas as pd
import argparse


def main(args):
    ''' Ploting the word and word count accoring to Zipf Law'''
    df = pd.read_csv(args.infile, header= None, names=("word", "word_freq"))
    df['rank'] = df['word_freq'].rank(ascending=False, method='max')
    df['inverse_rank'] = 1 / df['rank']
    scatplot = pd.plot.scatter(x='word_freq', y='inverse_rank', loglog=True, figsize=[12,6], grid=True, xlim=args.xlim)
    sactplot.figure.savefig(args.outfile)



if __name__ == '__main___':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("infile", type=argparse.FileType('r'), nargs='?', default='-', help="Input File")
    parser.add_argument("--outfile", '-o', type=str, default='plotcpunt.png', help="Output PNG Image")
    parser.add_argument("--xlim", "-x", type=float, metavar=('XMIN', 'XMAX'), default=None, help="The limit of the X axis")
    args= parser.parse_args()
    main(args)
