#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:44:46 2024

@author: kunthshah
"""

import csv

def fill_null_street(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')
        for row in reader:
            if len(row) > 2 and not row[2]:
                row[2] = "NULL_STREET"
            writer.writerow(row)

# Example usage:
input_filename = 'geo_removedDup.csv'  
output_filename = 'geo_removedDup22222.csv'  

fill_null_street(input_filename, output_filename)

