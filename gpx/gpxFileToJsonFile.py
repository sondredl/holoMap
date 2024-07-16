import xml.etree.ElementTree as ET
import json
import os

def extract_coordinates_from_gpx(gpx_file_path):
    try:
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
            coordinates.append({'lat': lat, 'lon': lon})

        # Check if any coordinates were found
        if not coordinates:
            print("No coordinates found in the GPX file.")
            return
        
        # Create JSON file path
        json_file_path = os.path.splitext(gpx_file_path)[0] + '.json'
        
        # Write to JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(coordinates, json_file, indent=4)

        print(f"Extracted {len(coordinates)} coordinates and wrote them to {json_file_path}")
    except ET.ParseError as e:
        print(f"Error parsing GPX file: {e}")
    except FileNotFoundError:
        print(f"GPX file not found: {gpx_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
gpx_file_path = 'HV_Komplett_hero_trail.gpx'
extract_coordinates_from_gpx(gpx_file_path)

