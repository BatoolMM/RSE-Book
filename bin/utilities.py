"""Collection of the most used functions"""

import csv

def collection_to_csv(collection, num=None):
    """
    write all the file to csv format

    Parameters:
    ----------
    collections: collections.Counter
        Collection of items and counts
    num: int
        Limit the output to N most frequent items
    """
    collection = collection.most_common()
    if num is None:
        num = len(collection)
    writer = csv.writer(sys.stdout)
    writer.writerow(collection[0:num])
