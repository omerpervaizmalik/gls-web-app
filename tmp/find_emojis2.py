import glob
import re

emoji_regex = re.compile(r'[\U0001F000-\U0001F9FF\u2600-\u26FF\u2700-\u27BF]')

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    emojis = emoji_regex.findall(content)
    if emojis:
        unique_emojis = list(set(emojis))
        print(f"File {f} emojis: {[e.encode('unicode_escape').decode() for e in unique_emojis]}")
