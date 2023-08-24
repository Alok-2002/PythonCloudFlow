from boxsdk import OAuth2

""" Replace with your Box API credentials """
client_id = 'box.com_client_id'
client_secret = 'box.com_client_secret'

"""Extracted from the redirect URI """

auth_code = 'authorization_code'  
auth = OAuth2(client_id, client_secret)
access_token, refresh_token = auth.authenticate(auth_code)

print("Access Token:", access_token)
print("Refresh Token:", refresh_token)
