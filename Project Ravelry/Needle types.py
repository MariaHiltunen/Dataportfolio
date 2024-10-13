import requests
import csv

# API token username and password
authUsername = 'USER'
authPassword = 'PASSWORD'

# URL for the API request
url = 'https://api.ravelry.com/needles/types.json'

# Request
r1 = requests.get(url, auth=(authUsername, authPassword))

# Print response details
print("Response code: {}".format(r1.status_code))

# Check if the request was successful
if r1.status_code == 200:
    # Parse the JSON response
    data = r1.json()

    # Check the structure of the JSON response
    print("Parsed JSON:")
    print(data)
    
    # Open CSV file to write data
    with open('Needle types.csv', 'w', newline='') as csvfile:
        columns = ['description', 'metric_name', 'type_name', 'length (in)', 'length (cm)']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for needle_types in data['needle_types']:
            length_in_inches = needle_types.get('length', '')
        
            # Check if length is a number before converting
            if isinstance(length_in_inches, (int, float)):
                length_in_cm = length_in_inches * 2.54
            else:
                length_in_cm = ''

            writer.writerow({
                'description': needle_types.get('description', ''),
                'metric_name': needle_types.get('metric_name', ''),
                'type_name': needle_types.get('type_name', ''),
                'length (in)': length_in_inches,
                'length (cm)': length_in_cm
            })
    
else:
    print("Failed to retrieve data")