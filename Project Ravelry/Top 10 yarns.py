import requests
import csv

# API token username and password
authUsername = 'USER'
authPassword = 'PASSWORD'

# Ravelry API endpoint to get popular yarns
url = "https://api.ravelry.com/yarns/search.json"

# Parameters to limit the results to top 10 yarns, sorted by popularity
params = {
    'page_size': 10,  # Limit to top 10 yarns
    'sort': 'popularity',  # Sort by popularity
}

# Make the request to Ravelry API
response = requests.get(url, params=params, auth=(authUsername, authPassword))

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    yarns = response.json().get('yarns', [])
    
    # Print out the names and companies of the top 10 yarns
    for i, yarn in enumerate(yarns, start=1):
        yarn_name = yarn['name']
        company_name = yarn['yarn_company_name'] if 'yarn_company_name' in yarn else 'Unknown'
        print(f"{i}. {yarn_name} by {company_name}")

    # Open CSV file to write data
    with open('Top 10 yarns.csv', 'w', newline='') as csvfile:
        columns = ['name', 'company']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for yarn in yarns:
            company_name = yarn['yarn_company_name'] if 'yarn_company_name' in yarn else 'Unknown'
            writer.writerow({
                'name': yarn.get('name', ''),
                'company': company_name
            })

else:
    print(f"Failed to retrieve yarns. Status code: {response.status_code}")