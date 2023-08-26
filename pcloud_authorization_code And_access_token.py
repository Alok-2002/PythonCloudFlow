import requests

# Replace with your pCloud API credentials
client_id = 'your_pCloud_client_id'
client_secret = 'your_pCloud_client_secret'

# Set up the OAuth 2.0 authorization URL
auth_url = 'https://my.pcloud.com/oauth2/authorize'
redirect_uri = 'https://localhost'  # Placeholder URL for desktop/mobile apps

# Generate the authorization URL
authorize_url = f"{auth_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"

# Print the URL and visit it in a web browser
print("Visit the following URL and grant authorization:")
print(authorize_url)

# After granting authorization, you'll receive an authorization code

# Use the authorization code to get the access token
token_url = 'https://api.pcloud.com/oauth2_token'
authorization_code = 'your_authorization_code'  # Replace with the received authorization code

token_data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'code': authorization_code,
    'redirect_uri': redirect_uri,
    'grant_type': 'authorization_code',
}

response = requests.post(token_url, data=token_data)
access_token = response.json().get('access_token')

print(f"Access token: {access_token}")
