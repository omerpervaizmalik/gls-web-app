import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    card_icons = re.findall(r'<div class="card-icon">(.*?)</div>', content)
    if card_icons:
        print(f"File {f} card-icons:")
        print([i.encode('unicode_escape').decode() for i in card_icons])
