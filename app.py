import os
import requests
import argparse

def upload_document(file_path, server_url, api_token):
    """
    Upload a single document to Paperless-ngx via API.
    """
    endpoint = f"{server_url.rstrip('/')}/api/documents/post_document/"
    headers = {
        "Authorization": f"Token {api_token}"
    }
    try:
        with open(file_path, 'rb') as f:
            files = {'document': (os.path.basename(file_path), f)}
            response = requests.post(endpoint, headers=headers, files=files)

        if response.status_code == 200:
            print(f"Successfully uploaded {file_path}. Task UUID: {response.text}")
            return True
        else:
            print(f"Failed to upload {file_path}. Status: {response.status_code}, Response: {response.text}")
            return False
    except Exception as e:
        print(f"Error uploading {file_path}: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Upload all files recursively from a folder to Paperless-ngx.")
    parser.add_argument("folder_path", help="Path to the root folder containing files to upload.")
    parser.add_argument("server_url", help="Paperless-ngx server URL (e.g., http://localhost:8000)")
    parser.add_argument("api_token", help="API token for authentication.")

    args = parser.parse_args()

    uploaded_count = 0
    failed_count = 0

    for root, dirs, files in os.walk(args.folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            if upload_document(full_path, args.server_url, args.api_token):
                uploaded_count += 1
            else:
                failed_count += 1

    print(f"\nUpload complete. Successful: {uploaded_count}, Failed: {failed_count}")

if __name__ == "__main__":
    main()