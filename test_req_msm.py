import requests
from constants import SSL_VERIFY, TENANT_IDENTIFIER

def test_post_request(token):
    url = "https://sustainium-dev.12thwonder.com/api/app/fuel-and-energy-activity-management"
    payload = {
  "emissionFactorTypeId": "3a10f724-4317-6f56-c6bc-351945a3992d",
  "menuTreeEmissionTrackingYearMapId": "3a176139-bfe5-b21b-fd90-02dc23696824",
  "emissionFactorDatabaseId": "3a109a0c-ceb2-f15e-cfce-3502e3f86891",
  "timeFrame": "2025",
  "emissionFactorYear": "2025",
  "monthsData": {
    "2025-2025": 10000
  },
  "description": "test",
  "vehicleTypeId": "06a842fd-3bbd-49b5-89bb-f99b33897935",
  "fuelTypeId": "1c9ff5d5-7d9a-4a3b-988a-6874f501c49d",
  "emissionUnitId": "15743d29-46f2-476c-b5fa-d58c6d5023bd",
  "mileTravelledMonthsData": {
    "2025-2025": 10000
  },
  "roadType": 1
}

    headers = {
        "tenantIdentifier": TENANT_IDENTIFIER,
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    try:
        response = requests.post(url, json=payload, headers=headers, verify=SSL_VERIFY)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def test_get_request(token):
    url = "https://sustainium-dev.12thwonder.com/api/app/fuel-and-energy-activity-management"
    headers = {
        "tenantIdentifier": TENANT_IDENTIFIER,
        "Authorization": f"Bearer {token}"
    }
    try:
        response = requests.get(url, headers=headers, verify=SSL_VERIFY)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


# def test_put_request(token, resource_id):
#     url = f"https://sustainium-dev.12thwonder.com/api/app/stationary-combustion-management/{resource_id}"
    
#     payload = {
#         "emissionFactorTypeId": "3a10f724-4317-6f56-c6bc-351945a3992d",
#         "menuTreeEmissionTrackingYearMapId": "3a176139-bfe5-b21b-fd90-02dc23696824",
#         "emissionFactorDatabaseId": "3a109a0c-ceb2-f15e-cfce-3502e3f86891",
#         "timeFrame": "2025",
#         "emissionFactorYear": "2025",
#         "monthsData": {"2025-2025": 11},
#         "description": "test2",
#         "emissionSourceId": "a40e0b02-5570-4338-a274-e9fa15839184",
#         "emissionUnitId": "74e517b1-dbee-4daa-af16-ad12e9598947"
#     }
#     headers = {
#         "tenantIdentifier": TENANT_IDENTIFIER,
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {token}"
#     }
#     try:
#         response = requests.put(url, json=payload, headers=headers, verify=SSL_VERIFY)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.HTTPError as http_err:
#         print(f"HTTP error occurred: {http_err}")
#     except requests.exceptions.RequestException as req_err:
#         print(f"Request error occurred: {req_err}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     return None


def test_delete_request(token, resource_id):
    url = f"https://sustainium-dev.12thwonder.com/api/app/fuel-and-energy-activity-management/{resource_id}"
    headers = {
        "tenantIdentifier": TENANT_IDENTIFIER,
        "Authorization": f"Bearer {token}"
    }
    try:
        response = requests.delete(url, headers=headers, verify=SSL_VERIFY)
        response.raise_for_status()
        return {"status": "Success", "message": "Resource deleted successfully."}
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


# Example usage
if __name__ == "__main__":
    access_token = "your_access_token"  # Replace with your actual token
    print("Testing POST request...")
    post_response = test_post_request(access_token)
    print(post_response)

    if post_response and "id" in post_response:
        resource_id = post_response["id"]
        # print("\nTesting PUT request...")
        # print(test_put_request(access_token, resource_id))
        
        print("\nTesting DELETE request...")
        print(test_delete_request(access_token, resource_id))
    else:
        print("POST request failed or ID not found in the response.")
