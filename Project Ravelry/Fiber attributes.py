import requests
import csv

# API token username and password
authUsername = 'USER'
authPassword = 'PASSWORD'

# URL for the API request
url = 'https://api.ravelry.com/fiber_attributes.json'

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
    with open('Fiber attributes.csv', 'w', newline='') as csvfile:
        columns = ['id', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for fiber_attributes in data['fiber_attributes']:
            writer.writerow({
                'id': fiber_attributes.get('id', ''),
                'name': fiber_attributes.get('name', ''),
            })

else:
    print("Failed to retrieve data")