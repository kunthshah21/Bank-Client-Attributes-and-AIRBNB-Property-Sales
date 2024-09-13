#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:36:43 2024

@author: kunthshah
"""

import csv

def remove_empty_rows(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        # Write header
        header = next(reader)
        writer.writerow(header)

        # Iterate through rows, remove those with empty cells in specified columns
        for row in reader:
            latitude = row[15]
            longitude = row[16]
            hot_tub = row[17]
            pool = row[18]
            if latitude != '' and longitude != '' and hot_tub != '' and pool != '':
                writer.writerow(row)

# Example usage:
input_file = 'market_combined.csv'
output_file = 'market_combined_filtered.csv'

remove_empty_rows(input_file, output_file)
