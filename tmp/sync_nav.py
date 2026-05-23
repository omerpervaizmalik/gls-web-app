import os
import glob
import re

DIR = 'd:/Anti gravity/get-legal-solution'

with open(os.path.join(DIR, '_navbar_snippet.html'), 'r', encoding='utf-8') as f:
    master_navbar = f.read()

# Filter out comments and whitespace to get the actual <ul> block
match = re.search(r'(<ul id="nav-links".*?</ul>)', master_navbar, re.DOTALL)
if not match:
    # If the id is on ul
    match = re.search(r'(<ul class="nav-links".*?</ul>)', master_navbar, re.DOTALL)

if match:
    master_navbar_content = match.group(1)
else:
    # Fallback to lines 4-end
    lines = master_navbar.splitlines()
    master_navbar_content = "\\n".join(lines[3:])


html_files = glob.glob(os.path.join(DIR, '*.html'))

for file_path in html_files:
    # Skip the snippet itself
    if os.path.basename(file_path).startswith('_'):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to find the <ul ... id="nav-links">...</ul> or <ul class="nav-links">...</ul>
    # We look for <ul class="nav-links" id="nav-links"> ... </ul>
    new_content = re.sub(r'<ul class="nav-links".*?</ul>', master_navbar_content, content, flags=re.DOTALL)
    
    # If it didn't match (some might not have id), try class only
    if new_content == content:
         new_content = re.sub(r'<ul class=\"nav-links\".*?</ul>', master_navbar_content, content, flags=re.DOTALL)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Propagated navbar to {os.path.basename(file_path)}")
    else:
        print(f"Could not find navbar block in {os.path.basename(file_path)}")
