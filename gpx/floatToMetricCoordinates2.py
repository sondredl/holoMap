import json
import math

def lat_lon_to_meters(lat1, lon1, lat2, lon2):
    # Constants
    R = 6378137  # Radius of Earth in meters

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Differences in coordinates
    d_lat = lat2_rad - lat1_rad
    d_lon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(d_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    # Calculate direction
    y = math.sin(d_lon) * math.cos(lat2_rad)
    x = math.cos(lat1_rad) * math.sin(lat2_rad) - math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(d_lon)
    bearing = math.atan2(y, x)

    # Convert to meters in x (East) and y (North) directions
    distance_x = distance * math.sin(bearing)
    distance_y = distance * math.cos(bearing)

    return distance_x, distance_y

def parse_and_convert(json_file, output_file):
    # Load JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Initialize the first coordinates
    first_lat = float(data[0]['lat'])
    first_lon = float(data[0]['lon'])

    # Set the first lat and lon to zero
    data[0]['lat'] = 0
    data[0]['lon'] = 0

    # Convert lat/lon to meters relative to the previous position
    for i in range(1, len(data)):
        prev_lat = float(data[i - 1]['lat']) if i > 1 else first_lat
        prev_lon = float(data[i - 1]['lon']) if i > 1 else first_lon
        current_lat = float(data[i]['lat'])
        current_lon = float(data[i]['lon'])
        
        distance_x, distance_y = lat_lon_to_meters(prev_lat, prev_lon, current_lat, current_lon)
        
        data[i]['lat'] = distance_y
        data[i]['lon'] = distance_x

    # Write the result to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# Usage
# parse_and_convert('input.json', 'metric.json')
parse_and_convert('H_gevarde_velo_rama_stifest.json', 'metric.json')



