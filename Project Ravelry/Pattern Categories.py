import requests
import csv
import json

# API token username and password
authUsername = 'USER'
authPassword = 'PASSWORD'

# URL for the API request
url = 'https://api.ravelry.com/pattern_categories/list.json'

# Request
r1 = requests.get(url, auth=(authUsername, authPassword))

# Print response details
print("Response code: {}".format(r1.status_code))

# Check if the request was successful
if r1.status_code == 200:
    # Parse the JSON response
    data = r1.json()

    # Check the structure of the JSON response
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
    formatted_data = formatted_data.replace('{"pattern_categories": {', '{"pattern_categories": [{')
    formatted_data = formatted_data.replace(' "applique"}]}}', ' "applique"}]}')
    formatted_data = formatted_data.replace('}]}, {', '}, {')
 
    # Print the final result
    print(formatted_data)

    json_data = json.loads(formatted_data)

    with open('Fiber categories.json', 'w') as json_file:
       json.dump(json_data, json_file, indent=4)

    
    new_data = json.loads(formatted_data)

    # Open CSV file to write data
    with open('Pattern Categories.csv', 'w', newline='') as csvfile:
        columns = ['id', 'long_name']
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for pattern_categories in new_data['pattern_categories']:
            writer.writerow({
                'id': pattern_categories.get('id', ''),
                'long_name': pattern_categories.get('long_name', ''),
            })
    
else:
    print("Failed to retrieve data")