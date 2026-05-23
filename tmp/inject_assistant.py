import os

def inject_scripts():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    script_tags = """
    <!-- Smart Assistant & Knowledge Base Integration -->
    <script src="laws_db.js"></script>
    <script src="requirements_db.js"></script>
    <script src="content_db.js"></script>
    <script src="assistant.js"></script>
"""

    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if we need to update
        if 'assistant.js' in content and 'requirements_db.js' not in content:
            # Look for the old block and replace it
            content = content.replace('<script src="laws_db.js"></script>', '') # Clean up old one
            content = content.replace('<script src="assistant.js"></script>', '') # Clean up old one
            content = content.replace('<!-- Smart Assistant Integration -->', '')
            
            # Re-inject at the bottom
            if '</body>' in content:
                content = content.replace('</body>', script_tags + '</body>')
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated scripts in {filename}")
            continue

        if 'assistant.js' in content:
            print(f"Skipping {filename} - Assistant already up to date.")
            continue
            
        if '</body>' in content:
            new_content = content.replace('</body>', script_tags + '</body>')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected assistant into {filename}")
        else:
            print(f"Error: </body> tag not found in {filename}")

if __name__ == "__main__":
    inject_scripts()
