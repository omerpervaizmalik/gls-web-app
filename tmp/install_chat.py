import os
import glob

DIR = 'd:/Anti gravity/get-legal-solution'
TIDIO_TAG = '    <script src="//code.tidio.co/acfgv2rrzlgyzesapsnlcwlfxahhftkm.js" async></script>\n'

html_files = glob.glob(os.path.join(DIR, '*.html'))

for file_path in html_files:
    if os.path.basename(file_path).startswith('_'):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if tidio already exists
    if 'tidio.co' in content:
        print(f"Skipping {os.path.basename(file_path)} - Tidio already exists.")
        continue
    
    # Insert before </body>
    if '</body>' in content:
        new_content = content.replace('</body>', TIDIO_TAG + '</body>')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Installed Tidio on {os.path.basename(file_path)}")
    else:
        print(f"Could not find </body> in {os.path.basename(file_path)}")
