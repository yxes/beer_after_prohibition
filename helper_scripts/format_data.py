#!/usr/bin/env python

"""

only need the values from the first 3 columns

 Original Data URL: http://www.stat.ufl.edu/~winner/data/beerreg.dat

"""
import csv

original_dataset = "../beerreg.dat"
output_dataset  = "../beerreg.tsv"

headers = ['year', 'region', 'drunk']

# spit it out
with open (output_dataset, 'w') as csv_out, open(original_dataset, 'r') as csv_orig:
    orig_reader = csv.reader(csv_orig, delimiter=' ', quotechar='"', skipinitialspace=True)
    out_writer  = csv.writer(csv_out,  delimiter="\t",  quoting=csv.QUOTE_MINIMAL)

    out_writer.writerow(headers)
    for row in orig_reader:
        out_writer.writerow(row[0:3])

print("done.")
