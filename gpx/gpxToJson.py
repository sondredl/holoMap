import os
import json
from bs4 import BeautifulSoup

def extract_coordinates_from_html(html_file_path):
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Extract coordinates
    coordinates = []
    for trkpt in soup.find_all('trkpt'):
        lat = trkpt.get('lat')
        lon = trkpt.get('lon')
        ele = trkpt.get('ele')
        if lat is not None and lon is not None:
            try:
                lat = float(lat)
                lon = float(lon)
                coordinates.append({'lat': lat, 'lon': lon})
            except ValueError:
                print(f"Skipping invalid coordinates: lat={lat}, lon={lon}")

    # Create JSON file path
    json_file_path = os.path.splitext(html_file_path)[0] + '.json'
    
    # Write to JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(coordinates, json_file, indent=4)

    print(f"Extracted {len(coordinates)} coordinates and wrote them to {json_file_path}")

# Usage
html_file_path = 'HV_Komplett_hero_trail.html'
extract_coordinates_from_html(html_file_path)

