#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:41:13 2024

@author: kunthshah
"""

import csv

def remove_duplicates(input_file, output_file):
    seen = set()
    output_rows = []
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile, delimiter=';')
        for row in reader:
            unified_id = row[0]
            if unified_id not in seen:
                output_rows.append(row)
                seen.add(unified_id)
    
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=';')
        writer.writerows(output_rows)

# Example usage:
input_filename = 'market_combined_filtered.csv'  
output_filename = 'market2019FINAL.csv'  

remove_duplicates(input_filename, output_filename)






