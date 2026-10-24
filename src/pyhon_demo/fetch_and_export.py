import requests
import csv

# 1. Define the public API endpoint
url = "https://jsonplaceholder.typicode.com/users"

# 2. Fetch data from the API
response = requests.get(url)

# 3. Process and export data if the request is successful
if response.status_code == 200:
    users = response.json()
    
    # Open/create a CSV file to store the data
    with open("users.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(["Name", "Email", "City"])
        
        # Iterate through the API data and write each user's details
        for user in users:
            name = user.get("name")
            email = user.get("email")
            city = user.get("address", {}).get("city")
            
            writer.writerow([name, email, city])
            
    print("Data saved to users.csv file.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")