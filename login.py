import requests
from constants import TOKEN_URL, USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET, SSL_VERIFY, TENANT_IDENTIFIER


def login_api():
    headers = {
        "tenantIdentifier": TENANT_IDENTIFIER,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "grant_type": "password",
        "username": USERNAME,
        "password": PASSWORD,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    try:
        response = requests.post(TOKEN_URL, headers=headers, data=data, verify=SSL_VERIFY)
        print("Raw Response:", response.text)  # Debug: Print the raw response
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None
