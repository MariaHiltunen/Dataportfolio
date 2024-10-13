import requests
import csv
import json

# API token username and password
authUsername = 'USER'
authPassword = 'PASSWORD'

# URL for the API request
url = 'https://api.ravelry.com/patterns/search.json'

# Initialize pagination variables
page = 1
max_page = 1000  # Set the maximum number of pages to retrieve
all_patterns = []

# Loop through all pages
while page <= max_page:
    # Request with pagination
    params = {'page': page}
    r1 = requests.get(url, auth=(authUsername, authPassword), params=params)

    # Print response details
    print(f"Response code for page {page}: {r1.status_code}")

    # Check if the request was successful
    if r1.status_code == 200:
        # Parse the JSON response
        data = r1.json()

        # Append the results to the full list of yarn companies
        all_patterns.extend(data['patterns'])

        # Check if there's a next page by verifying if the current page returned any companies
        if not data['patterns']:
            break  # No more companies, exit loop
    else:
        print(f"Failed to retrieve data for page {page}")
        break

    # Move to the next page
    page += 1
    
# Write the full data to a CSV file
if all_patterns:
    with open('Patterns.csv', 'w', newline='', encoding='utf-8') as csvfile:
        columns = ['id', 'name', 'designer', 'free']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for pattern in all_patterns:  # Iterate over the list directly
            writer.writerow({
                'id': pattern.get('id', ''),
                'name': pattern.get('name', ''),
                'designer': pattern.get('designer', ''),
                'free': 'free' if pattern.get('free', False) else 'Pay'  # Mapping True to 'Free' and False to 'Pay'
            })
    
else:
    print("Failed to retrieve data")