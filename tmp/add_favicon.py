import os
import glob
import re

DIR = 'd:/Anti gravity/get-legal-solution'
FAVICON_TAG = '    <link rel="icon" type="image/png" href="logo.png">\n'

html_files = glob.glob(os.path.join(DIR, '*.html'))

for file_path in html_files:
    if os.path.basename(file_path).startswith('_'):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if favicon already exists
    if 'rel="icon"' in content or 'rel="shortcut icon"' in content:
        print(f"Skipping {os.path.basename(file_path)} - favicon already exists.")
        continue
    
    # Insert before </head>
    if '</head>' in content:
        new_content = content.replace('</head>', FAVICON_TAG + '</head>')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added favicon to {os.path.basename(file_path)}")
    else:
        print(f"Could not find </head> in {os.path.basename(file_path)}")
