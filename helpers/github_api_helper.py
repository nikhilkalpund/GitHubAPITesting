import requests

access_token = "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"

def get_authenticated_user(access_token):
    """
    Helper function to get the authenticated user's details.
    
    Args:
        access_token (str): Personal access token for authentication.
        
    Returns:
        requests.Response: Response object containing user details.
    """
    access_token = "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"
    url = 'https://api.github.com/user'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response

def update_user_bio(access_token, new_bio):
    """
    Helper function to update the authenticated user's bio.
    
    Args:
        access_token (str): Personal access token for authentication.
        new_bio (str): New bio content to update.
        
    Returns:
        requests.Response: Response object containing the result of the update.
    """
    url = 'https://api.github.com/user'
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {'bio': new_bio}
    response = requests.patch(url, headers=headers, json=data)
    return response
