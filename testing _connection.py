import os
from atlassian import Confluence

# Load credentials from environment variables for security
# confluence_url = os.getenv('CONFLUENCE_URL')
# confluence_username = os.getenv('CONFLUENCE_USERNAME')
# confluence_api_token = os.getenv('CONFLUENCE_API_TOKEN')


confluence_url = "https://confluence.wiley.com/display/SRE/SRE+Home"
confluence_username = ""
confluence_api_token = ""

# Initialize Confluence client
confluence = Confluence(
    url=confluence_url,
    username=confluence_username,
    password=confluence_api_token
)

# Test connection by getting current user's details
# try:
#     user = confluence.get_current_user()
    
#     if user:
#         print("Authentication successful!")
#         print(f"Logged in as: {user}")
#     else:
#         print("Failed to authenticate.")
# except Exception as e:
#     print(f"Error: {e}")


# # Test connection by fetching Confluence instance details
# try:
#     instance_info = confluence.get_server_info()
#     if instance_info:
#         print("Authentication successful!")
#         print(f"Confluence Instance Info: {instance_info}")
#     else:
#         print("Failed to authenticate or fetch instance info.")
# except Exception as e:
#     print(f"Error: {e}")

#     confluence.get_user_details_by_username(username, expand=None)


# Test connection by fetching information about a space
space_key = 'SRE'  # Replace with an actual space key from your Confluence instance

try:
    space_info = confluence.get_space(space_key)
    if space_info:
        print("Authentication successful!")
        print(f"Space Info: {space_info}")
    else:
        print("Failed to authenticate or fetch space info.")
except Exception as e:
    print(f"Error: {e}")