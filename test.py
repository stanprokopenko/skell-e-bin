import requests
import base64
import random
import string

def generate_html_for_preview(title, html_content):
    template_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Skell-E HTML Preview</title>
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
  <article>
    <h1 id="title"></h1>
    <a href="#" class="button copy-link" onclick="copyToClipboard(); return false;">Copy Code</a>
    <div id="code-to-copy">
    </div>
  </article>
<script src="../assets/script.js"></script>
</body>
</html>'''

    # Insert the title into the <h1> tag
    template_html = template_html.replace('<h1 id="title"></h1>', f'<h1 id="title">{title}</h1>')
    
    # Insert the HTML content into the <div id="code-to-copy">
    template_html = template_html.replace('<div id="code-to-copy">', f'<div id="code-to-copy">\n{html_content}\n')

    return template_html



def upload_file_to_github(token, owner, repo, path, file_content):
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    
    # Convert file content to base64 to comply with GitHub API requirements
    content_base64 = base64.b64encode(file_content.encode('utf-8')).decode('utf-8')

    # Prepare the request payload
    data = {
        "message": "Uploading a file via GitHub API",  # Commit message
        "content": content_base64,
    }

    # Make the PUT request to create or update the file
    response = requests.put(api_url, headers=headers, json=data)

    if response.status_code == 201:
        # Extracting the file's raw URL from the response
        file_url = response.json()['content']['download_url']
        print(f"File uploaded successfully: {file_url}")
    else:
        print(f"Failed to upload file: {response.status_code} {response.text}")
        file_url = None

    return file_url



# Generate the HTML for the preview
title = "This is the TITLE"
html_content = "<h2>Subheader</h2><p>This is the content of the file.</p>"

file_content = generate_html_for_preview(title, html_content)


# Upload to GitHub
YOUR_TOKEN = "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"
owner = "stanprokopenko"
repo = "Skell-E-Bin"
suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
path = f"meta/{title.replace(' ', '_').lower()}_{suffix}.html"  # Include the desired folder and file name

file_url = upload_file_to_github(YOUR_TOKEN, owner, repo, path, file_content)

preview_url = f"https://html-preview.github.io/?url={file_url}"
print(preview_url)

url_for_slack = f"[Lesson Notes]({preview_url})"


