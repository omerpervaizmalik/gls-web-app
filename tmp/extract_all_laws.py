import os
from pypdf import PdfReader

def extract_pdf_to_js(pdf_name, js_filename, var_name):
    pdf_path = os.path.join("laws_content", pdf_name)
    js_path = os.path.join("laws_content", js_filename)
    
    if not os.path.exists(pdf_path):
        print(f"Skipping: {pdf_path} (File not found)")
        return

    print(f"Reading {pdf_path}...")
    try:
        reader = PdfReader(pdf_path)
        full_text = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                full_text.append(text)
            if (i+1) % 100 == 0:
                print(f"  Processed {i+1}/{len(reader.pages)} pages...")

        combined_text = "\n".join(full_text)
        escaped_text = combined_text.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
        js_content = f"window.{var_name} = `{escaped_text}`;"
        
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js_content)
        
        print(f"  Successfully wrote {len(js_content)} bytes to {js_path}")
    except Exception as e:
        print(f"  Error processing {pdf_name}: {e}")

if __name__ == "__main__":
    mappings = [
        ("CPC.pdf", "cpc_1908.js", "cpc_1908_text"),
        ("Crpc.pdf", "crpc_1898.js", "crpc_1898_text"),
        ("PPC.pdf", "ppc_1860.js", "ppc_1860_text"),
        ("Qanoon e shahadat.pdf", "qs_1984.js", "qs_1984_text"),
        ("police order.pdf", "po_2002.js", "po_2002_text")
    ]
    
    print(f"Starting batch extraction for {len(mappings)} laws...")
    for pdf, js, var in mappings:
        extract_pdf_to_js(pdf, js, var)
    print("Batch processing complete.")
