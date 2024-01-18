import requests
response = requests.get("https://api.github.com/users/naveenkrnl")

print(response.status_code)
print(response.json())





# Q2. API Documentation
# import requests
# import json
# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

# response = requests.get('https://api.github.com/users/naveenkrnl')

# print(response.status_code)

# jprint(response.json())