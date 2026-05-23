import os
import glob

DIR = 'd:/Anti gravity/get-legal-solution'
CONFIG_TAG = '    <script src="tidio_config.js"></script>\n'

def apply_fix():
    html_files = glob.glob(os.path.join(DIR, '*.html'))
    for file_path in html_files:
        if os.path.basename(file_path).startswith('_'):
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'tidio_config.js' in content:
            print(f"Already fixed: {os.path.basename(file_path)}")
            continue
            
        if '</body>' in content:
            # Insert CONFIG_TAG before </body>
            new_content = content.replace('</body>', CONFIG_TAG + '</body>')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed: {os.path.basename(file_path)}")

if __name__ == '__main__':
    apply_fix()
