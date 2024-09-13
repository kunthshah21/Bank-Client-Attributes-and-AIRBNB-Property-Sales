#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:22:21 2024

@author: kunthshah
"""

import csv

def add_geolocation_info(market_analysis_file, geolocation_file, output_file):
    # Create a dictionary to store geolocation information by unified_id
    geolocation_info = {}
    with open(geolocation_file, 'r') as geo_file:
        geo_reader = csv.reader(geo_file, delimiter=';')
        next(geo_reader)  # Skip header
        for row in geo_reader:
            unified_id = row[0]
            street_name = row[2]
            latitude = row[3]
            longitude = row[4]
            geolocation_info[unified_id] = {'street_name': street_name, 'latitude': latitude, 'longitude': longitude}

    # Add geolocation information to market analysis data
    with open(market_analysis_file, 'r') as market_file, open(output_file, 'w', newline='') as output:
        market_reader = csv.reader(market_file, delimiter=';')
        market_writer = csv.writer(output, delimiter=';')

        # Write header with new columns
        header = next(market_reader)
        header.extend(['Street Name', 'Latitude', 'Longitude'])
        market_writer.writerow(header)

        # Match unified_id and add geolocation data
        for row in market_reader:
            unified_id = row[0]
            geolocation_data = geolocation_info.get(unified_id, {})
            street_name = geolocation_data.get('street_name', '')
            latitude = geolocation_data.get('latitude', '')
            longitude = geolocation_data.get('longitude', '')

            row.extend([street_name, latitude, longitude])
            market_writer.writerow(row)

# Example usage:
market_analysis_file = 'market2019.csv'
geolocation_file = 'geo_clean.csv'
output_file = 'market_analysis_with_geolocation.csv'

add_geolocation_info(market_analysis_file, geolocation_file, output_file)
