import requests
import csv

# API token username and password
authUsername = 'USER'
authPassword = 'PASSWORD'

# Ravelry API endpoint to get top patterns
url = "https://api.ravelry.com/patterns/search.json"

# Parameters to limit the results to top 10 patterns
params = {
    'page_size': 10,  # Limit to top 10 patterns
    'sort': 'popularity',  # Sort by popularity
}

# Make the request to Ravelry API
response = requests.get(url, params=params, auth=(authUsername, authPassword))

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    patterns = response.json().get('patterns', [])
    
    # Print out the names and designers of the top 10 patterns
    for i, pattern in enumerate(patterns, start=1):
        designer_name = pattern['pattern_author']['name'] if 'pattern_author' in pattern else 'Unknown'
        print(f"{i}. {pattern['name']} from {designer_name}")
    
    # Open CSV file to write data
    with open('Top 10 patterns.csv', 'w', newline='') as csvfile:
        columns = ['name', 'designer']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for pattern in patterns:
            designer_name = pattern['pattern_author']['name'] if 'pattern_author' in pattern else 'Unknown'
            writer.writerow({
                'name': pattern.get('name', ''),
                'designer': designer_name
            })

else:
    print(f"Failed to retrieve patterns. Status code: {response.status_code}")