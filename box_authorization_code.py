from boxsdk import OAuth2

""" Replace with your Box API credentials """

client_id = 'box.com_client_id'
client_secret = 'box.com_client_secret'

auth = OAuth2(client_id, client_secret)
auth_url, csrf_token = auth.get_authorization_url('http://localhost:5000/callback')
print("Visit this URL to authorize your app:", auth_url)
