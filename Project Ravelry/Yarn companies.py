import requests
import csv
import json

# API token username and password
authUsername = 'USER'
authPassword = 'PASSWORD'

# URL for the API request
url = 'https://api.ravelry.com/yarn_companies/search.json'

# Initialize pagination variables
page = 1
all_companies = []

# Loop through all pages
while True:
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
        all_companies.extend(data['yarn_companies'])

        # Check if there's a next page by verifying if the current page returned any companies
        if not data['yarn_companies']:
            break  # No more companies, exit loop
    else:
        print(f"Failed to retrieve data for page {page}")
        break

    # Move to the next page
    page += 1

# Write the full data to a CSV file
if all_companies:
    with open('Yarn Companies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        columns = ['id', 'name', 'url', 'yarns_count']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for yarn_company in all_companies:
            writer.writerow({
                'id': yarn_company.get('id', ''),
                'name': yarn_company.get('name', ''),
                'url': yarn_company.get('url', ''),
                'yarns_count': yarn_company.get('yarns_count', '')
            })
else:
    print("No data available to write.")