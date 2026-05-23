import os
from pypdf import PdfReader

def extract_pdf_to_js(pdf_path, js_path, var_name):
    print(f"Reading {pdf_path}...")
    reader = PdfReader(pdf_path)
    full_text = []
    
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            full_text.append(text)
        if (i+1) % 50 == 0:
            print(f"Processed {i+1}/{len(reader.pages)} pages...")

    combined_text = "\n".join(full_text)
    
    # Escape backticks and backslashes for JS template literal
    # Also handle the '$' if needed, but backticks are the main concern
    escaped_text = combined_text.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
    
    js_content = f"window.{var_name} = `{escaped_text}`;"
    
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"Successfully wrote {len(js_content)} bytes to {js_path}")

if __name__ == "__main__":
    PDF_PATH = os.path.join("laws_content", "income tax ordinance latest.pdf")
    JS_PATH = os.path.join("laws_content", "it_2001.js")
    VAR_NAME = "it_2001_text"
    
    if os.path.exists(PDF_PATH):
        extract_pdf_to_js(PDF_PATH, JS_PATH, VAR_NAME)
    else:
        print(f"Error: PDF not found at {PDF_PATH}")
