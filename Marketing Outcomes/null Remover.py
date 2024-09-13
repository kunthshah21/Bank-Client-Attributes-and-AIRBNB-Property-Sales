#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:43:43 2024

@author: kunthshah
"""

import pandas as pd

def remove_null_rows(input_file, output_file):
    # Read CSV file
    df = pd.read_csv(input_file)
    
    # Remove rows with null values
    df = df.dropna()
    
    # Write cleaned data to a new CSV file
    df.to_csv(output_file, index=False)

# Example usage
input_file = 'dataset.csv'
output_file = 'output.csv'
remove_null_rows(input_file, output_file)







