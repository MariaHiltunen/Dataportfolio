import requests
import csv
import json

# API token username and password
authUsername = 'USER'
authPassword = 'PASSWORD'

# URL for the API request
url = 'https://api.ravelry.com/yarns/search.json'

# Initialize pagination variables
page = 1
max_page = 2000  # Set the maximum number of pages to retrieve
all_yarns = []

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
        all_yarns.extend(data['yarns'])

        # Check if there's a next page by verifying if the current page returned any companies
        if not data['yarns']:
            break  # No more companies, exit loop
    else:
        print(f"Failed to retrieve data for page {page}")
        break

    # Move to the next page
    page += 1

# Write the full data to a CSV file
if all_yarns:
    with open('Yarns.csv', 'w', newline='', encoding='utf-8') as csvfile:
        columns = ['id', 'name', 'yarn_company_name', 'rating_average', 'machine_washable', 'wpi']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for yarn in all_yarns:  # Iterate over the list directly
            writer.writerow({
                'id': yarn.get('id', ''),
                'name': yarn.get('name', ''),
                'yarn_company_name': yarn.get('yarn_company_name', ''),
                'rating_average': round(yarn.get('rating_average', 0), 0) if yarn.get('rating_average') is not None else '',
                'machine_washable': yarn.get('machine_washable', ''),
                'wpi': yarn.get('wpi', '')
            })

else:
    print("Failed to retrieve data")