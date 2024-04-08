import requests

# Base URL for GitHub API
BASE_URL = "https://api.github.com"

# Test case for failure: No Token Provided
def test_no_token_provided():
    # Make GET request to /user without providing a token
    response = requests.get(f"{BASE_URL}/user")
    
    # Check if status code is 401 Unauthorized
    assert response.status_code == 401
 
# Test case for failure: Invalid Token Provided
def test_invalid_token_provided():
    # Make GET request to /user with an invalid token
    headers = {"Authorization": "Bearer invalid_token"}
    response = requests.get(f"{BASE_URL}/user", headers=headers)
    
    # Check if status code is 401 Unauthorized
    assert response.status_code == 401

# Test case for failure: Forbidden Access (Token Without Necessary Permissions)
def test_forbidden_access():
    # Make GET request to /user with a token without necessary permissions
    headers = {"Authorization": "Bearer your_token_without_permissions"}
    response = requests.get(f"{BASE_URL}/user", headers=headers)
    
    # Check if status code is 403 Forbidden
    assert response.status_code == 403

# Test case for success: Get User With Valid Token
def test_get_user_with_valid_token():
    # Make GET request to /user with a valid token
    headers = {"Authorization": "Bearer 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"}
    response = requests.get(f"{BASE_URL}/user", headers=headers)
    
    # Check if status code is 200 OK
    assert response.status_code == 200

# Test case for success: Update User Bio With Valid Token
def test_update_user_bio_with_valid_token():
    # Make PATCH request to /user with a valid token and body
    headers = {"Authorization": "Bearer your_valid_token", "Content-Type": "application/json"}
    body = {"bio": "Your new bio content here."}
    response = requests.patch(f"{BASE_URL}/user", headers=headers, json=body)
    
    # Check if status code is 200 OK
    assert response.status_code == 200
