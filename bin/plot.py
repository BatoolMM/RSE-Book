

import pandas as pd


input_csv = 'results/jane_eyre.csv'
df = pd.read(input_csv, header = None, names = ('word', 'word_freq'))

df['rank'] = df['word_freq'].rank(ascending=False, method='max')
df['inverse_rank'] = 1 / df['rank']

scatplot = df.plot.scatter(x='word_freq', y='inverse_rank', figsize=[12,6], grid=True)

fig = scatplot.get_figure

fig.savefig('results/jane_eyre.png')
