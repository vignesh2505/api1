import requests
from constants import SSL_VERIFY, USER_PROFILE_API, TENANT_IDENTIFIER

def get_user_profile(token):
    # API headers
    headers = {
        "tenantIdentifier": TENANT_IDENTIFIER,  # tenant id
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Bearer {token}"
    }

    try:
        # Make the GET request
        response = requests.get(USER_PROFILE_API, headers=headers, verify=SSL_VERIFY)

        # Check for HTTP errors
        response.raise_for_status()

        # Parse JSON response
        data = response.json()
        print("Response Data:", data)
        return data

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

