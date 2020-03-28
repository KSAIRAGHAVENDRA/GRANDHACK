# Request module must be installed.
# Run pip install requests if necessary.
import requests

subscription_key = 'YOUR_SUBSCRIPTION KEY'

def get_token(subscription_key):
    fetch_token_url = 'https://southeastasia.api.cognitive.microsoft.com/sts/v1.0/issueToken'
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    response = requests.post(fetch_token_url, headers=headers)
    access_token = str(response.text)
    print(access_token)
