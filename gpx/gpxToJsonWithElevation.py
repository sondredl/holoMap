import xml.etree.ElementTree as ET
import json
import os

def extract_coordinates_from_gpx(gpx_file_path):
    # Parse the GPX file
    tree = ET.parse(gpx_file_path)
    root = tree.getroot()
    
    # Define the namespace
    namespaces = {'default': 'http://www.topografix.com/GPX/1/1'}

    # Extract coordinates
    coordinates = []
    for trkpt in root.findall('.//default:trkpt', namespaces):
        lat = trkpt.get('lat')
        lon = trkpt.get('lon')
        ele = trkpt.find('default:ele', namespaces)
        elevation = ele.text if ele is not None else None
        coordinates.append({'lat': lat, 'lon': lon, 'elevation': elevation})

    # Create JSON file path
    json_file_path = os.path.splitext(gpx_file_path)[0] + '.json'
    
    # Write to JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(coordinates, json_file, indent=4)

    print(f"Extracted {len(coordinates)} coordinates and wrote them to {json_file_path}")

# Usage
gpx_file_path = 'H_gevarde_velo_rama_stifest.gpx'
extract_coordinates_from_gpx(gpx_file_path)

