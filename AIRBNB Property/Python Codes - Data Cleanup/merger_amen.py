#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:31:17 2024

@author: kunthshah
"""

import csv

def add_amenities_info(market_analysis_file, amen_clean_file, output_file):
    # Create a dictionary to store amenities information by unified_id
    amenities_info = {}
    with open(amen_clean_file, 'r') as amen_file:
        amen_reader = csv.reader(amen_file, delimiter=';')
        next(amen_reader)  # Skip header
        for row in amen_reader:
            unified_id = row[0]
            hot_tub = row[2]
            pool = row[3]
            amenities_info[unified_id] = {'Hot Tub': hot_tub, 'Pool': pool}

    # Add amenities information to market analysis data
    with open(market_analysis_file, 'r') as market_file, open(output_file, 'w', newline='') as output:
        market_reader = csv.reader(market_file, delimiter=';')
        market_writer = csv.writer(output, delimiter=';')

        # Write header with new columns
        header = next(market_reader)
        header.extend(['Hot Tub', 'Pool'])
        market_writer.writerow(header)

        # Match unified_id and add amenities data
        for row in market_reader:
            unified_id = row[0]
            amenities_data = amenities_info.get(unified_id, {})
            hot_tub = amenities_data.get('Hot Tub', '')
            pool = amenities_data.get('Pool', '')

            row.extend([hot_tub, pool])
            market_writer.writerow(row)

# Example usage:
market_analysis_file = 'market_analysis_with_geolocation.csv'
amen_clean_file = 'amen_clean.csv'
output_file = 'market_analysis_with_amenities.csv'

add_amenities_info(market_analysis_file, amen_clean_file, output_file)


