from login import login_api
from user_profile import get_user_profile
from test_req_wm import test_post_request, test_get_request, test_delete_request

def main():
    # Login and get the response
    api_response = login_api()

    if api_response and 'access_token' in api_response:
        access_token = api_response['access_token']

        # Get user profile
        print("Fetching user profile...")
        user_profile = get_user_profile(access_token)
        if user_profile:
            print("User Profile:", user_profile)
        else:
            print("Failed to fetch user profile.")

        # Test POST request
        print("\nTesting POST request...")
        post_response = test_post_request(access_token)
        if post_response:
            print("POST Request Successful:", post_response)

            # Extract 'id' and 'menuTreeEmissionTrackingYearMapId' from POST response
            resource_id = post_response.get("id")
            menu_tree_id = post_response.get("menuTreeEmissionTrackingYearMapId")

            if resource_id and menu_tree_id:
                # Test GET request
                print("\nTesting GET request...")
                get_response = test_get_request(access_token, menu_tree_id, resource_id)
                if get_response:
                    print("GET Request Successful:", get_response)
                else:
                    print("GET Request Failed.")

                # Test DELETE request
                print("\nTesting DELETE request...")
                delete_response = test_delete_request(access_token, resource_id)
                if delete_response:
                    print("DELETE Request Successful:", delete_response)
                else:
                    print("DELETE Request Failed.")
            else:
                print("POST Request did not return required data. Skipping GET and DELETE requests.")
        else:
            print("POST Request Failed.")
    else:
        print("Authentication failed. Unable to fetch access token.")

if __name__ == "__main__":
    main()


