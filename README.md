# Paperless-ngx Uploader

This is a simple Python script to recursively upload all files from a given folder to a Paperless-ngx instance using its API. It handles uploads one by one and can log results or suppress output as needed.


## Requirements

- Python 3.X
- `requests` library (installed via `pip install requests`)

## Usage

Run the script from the command line:

```bash
python3 intake_paperless.py <folder_path> <server_url> <api_token> [options]
```

### Arguments

- `folder_path`: Path to the root folder containing files to upload (required).
- `server_url`: Paperless-ngx server URL (e.g., `http://localhost:8000`) (required).
- `api_token`: API token for authentication (required).


### Options
- `--errors-only`: Output only errors to the console (flag, optional).
- `--silent`: Output nothing to the console until done, then print "Upload complete" (flag, optional).
- `--log-file <path>`: Path to a log file where upload messages will be written (optional).


### Examples

#### Basic upload:

```bash
python3 intake_paperless.py /path/to/folder http://localhost:8000 your_api_token_here
```

#### With errors only:

```bash
python3 intake_paperless.py /path/to/folder http://localhost:8000 your_api_token_here --errors-only
```


#### Silent mode with logging:


```bash
python3 intake_paperless.py /path/to/folder http://localhost:8000 your_api_token_here --silent --log-file upload_log.txt
```

At the end, it will show a summary of successful and failed uploads (unless in silent mode, where it just says "Upload complete"). If using a log file, the summary goes there too.

### Notes

- Make sure your API token has permission to upload documents.
- The script walks recursively through the folder, so it'll grab everything in subfolders.
- If you hit issues like 403 errors, double-check your server URL (no extra paths like /dashboard) and token.
- If it's a very large upload, consider using a tmux session.