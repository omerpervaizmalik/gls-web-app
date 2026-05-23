import os
import re
import glob

html_files = glob.glob('*.html')

FA_LINK = '    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n'

def replace_svgs(content):
    # WhatsApp
    content = re.sub(r'<svg viewBox="0 0 448 512"[^>]*>[\s]*<path d="M380.9 97.1[^>]*>.*?<\/svg>', '<i class="fab fa-whatsapp"></i>', content, flags=re.DOTALL)
    # Facebook
    content = re.sub(r'<svg viewBox="0 0 448 512"[^>]*>[\s]*<path d="M400 32H48[^>]*>.*?<\/svg>', '<i class="fab fa-facebook-f"></i>', content, flags=re.DOTALL)
    # Instagram
    content = re.sub(r'<svg viewBox="0 0 448 512"[^>]*>[\s]*<path d="M224.1 141[^>]*>.*?<\/svg>', '<i class="fab fa-instagram"></i>', content, flags=re.DOTALL)
    # Share
    content = re.sub(r'<svg viewBox="0 0 448 512"[^>]*>[\s]*<path d="M352 320[^>]*>.*?<\/svg>', '<i class="fas fa-share-nodes"></i>', content, flags=re.DOTALL)
    return content

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    content = replace_svgs(content)

    if 'font-awesome' not in content:
        # insert FA link before </head>
        content = content.replace('</head>', FA_LINK + '</head>')
    
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Done")
