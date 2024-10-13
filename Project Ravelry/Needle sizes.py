import requests
import csv

# API token username and password
authUsername = 'USER'
authPassword = 'PASSWORD'

# URL for the API request
url = 'https://api.ravelry.com/needles/sizes.json'

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
    with open('Needle sizes.csv', 'w', newline='') as csvfile:
        columns = ['hook', 'id', 'metric', 'us']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for needle_sizes in data['needle_sizes']:
            writer.writerow({
                'hook': needle_sizes.get('hook', ''),
                'id': needle_sizes.get('id', ''),
                'metric': needle_sizes.get('metric', ''),
                'us': needle_sizes.get('us', '')
            })
    
else:
    print("Failed to retrieve data")