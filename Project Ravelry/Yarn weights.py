import requests
import csv

# API token username and password
authUsername = 'USER'
authPassword = 'PASSWORD'

# URL for the API request
url = 'https://api.ravelry.com/yarn_weights.json'

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
    with open('Yarn_weights.csv', 'w', newline='') as csvfile:
        columns = ['id', 'knit_gauge', 'name', 'ply', 'wpi']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for weight in data['yarn_weights']:
            writer.writerow({
                'id': weight.get('id', ''),
                'knit_gauge': weight.get('knit_gauge', ''),
                'name': weight.get('name', ''),
                'ply': weight.get('ply', ''),
                'wpi': weight.get('wpi', '')
            })
else:
    print("Failed to retrieve data")