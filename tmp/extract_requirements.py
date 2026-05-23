import re
import json
import os

path = 'd:/Anti gravity/get-legal-solution/documentary-requirements.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Look for all blocks of checklist-card
# The regex looks for the start of a card and tries to capture until the end of that specific card block
cards = re.findall(r'<div class="checklist-card[^>]*>(.*?)</div>\s*</div>', content, re.DOTALL)
requirements = {}

for card_content in cards:
    # Extract title
    title_match = re.search(r'<h3 class="checklist-title">(.*?)</h3>', card_content)
    if title_match:
        title = title_match.group(1).strip()
        # Extract items from <li> tags
        items = re.findall(r'<li>(.*?)</li>', card_content)
        if items:
            # Clean HTML tags from items
            clean_items = [re.sub(r'<[^>]*>', '', item).strip() for item in items]
            requirements[title] = clean_items

# Save to JS file
output_path = 'd:/Anti gravity/get-legal-solution/requirements_db.js'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('const requirementsDB = ' + json.dumps(requirements, indent=4) + ';')

print(f'Extracted {len(requirements)} requirement sets.')
