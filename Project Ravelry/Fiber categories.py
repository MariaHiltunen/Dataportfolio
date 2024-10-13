import requests
import csv
import json

# API token username and password
authUsername = 'USER'
authPassword = 'PASSWORD'

# URL for the API request
url = 'https://api.ravelry.com/fiber_categories.json'

# Request
r1 = requests.get(url, auth=(authUsername, authPassword))

# Print response details
print("Response code: {}".format(r1.status_code))

# Check if the request was successful
if r1.status_code == 200:
    # Parse the JSON response
    data = r1.json()

    # Check the structure of the JSON response
    print(f"Total entries received: {len(data['fiber_categories'])}")
    print(f"Type of data: {type(data)}")

    #print("Parsed JSON:")
    #print(data)

    # JSON data had some issues with missing brackets or braces, so it needs fixing
    # Convert to JSON string
    json_data = json.dumps(data)

    # Replace occurrences as specified
    formatted_data = json_data.replace(', "children": [{', '}, {')
    formatted_data = formatted_data.replace(', "children": []}]}, {', '}, {')
    formatted_data = formatted_data.replace(', "children": []}, {', '}, {')
    formatted_data = formatted_data.replace(', "children": []}]}]}', '}]}')

   
    # Print the final result
    print(formatted_data)

    json_data = json.loads(formatted_data)

    # Open CSV file to write data
    with open('Fiber categories.csv', 'w', newline='') as csvfile:
        columns = ['id', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for fiber_categories in json_data['fiber_categories']:
            writer.writerow({
                'id': fiber_categories.get('id', ''),
                'name': fiber_categories.get('name', ''),
            })

else:
    print("Failed to retrieve data")