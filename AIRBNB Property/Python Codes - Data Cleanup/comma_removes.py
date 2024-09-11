#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:42:58 2024

@author: kunthshah
"""

import csv

def replace_commas(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')
        for row in reader:
            updated_row = [value.replace(',', '.') if isinstance(value, str) else value for value in row]
            writer.writerow(updated_row)

# Example usage:
input_filename = 'market_analysis_2019.csv' 
output_filename = 'market2019.csv'  

replace_commas(input_filename, output_filename)


