import os
import glob
import re

DIR = 'd:/Anti gravity/get-legal-solution'

NAV_OLD = """                        <div class="dropdown-group-label">Our Firm</div>
                        <a href="about-us.html#who-we-are"><span class="drop-icon">🏛️</span> Who We Are</a>
                        <a href="about-us.html#why-choose-us"><span class="drop-icon">⭐</span> Why Choose Us</a>
                        <div class="dropdown-divider"></div>
                        <a href="attorneys.html"><span class="drop-icon">👔</span> Our Attorneys</a>
                        <a href="testimonials.html"><span class="drop-icon">💬</span> Client Testimonials</a>"""

NAV_NEW = """                        <div class="dropdown-group-label">Our Firm</div>
                        <a href="about-us.html#who-we-are"><span class="drop-icon">🏛️</span> Who We Are</a>
                        <a href="about-us.html#why-choose-us"><span class="drop-icon">⭐</span> Why Choose Us</a>
                        <div class="dropdown-divider"></div>
                        <a href="attorneys.html"><span class="drop-icon">👔</span> Our Attorneys</a>
                        <a href="testimonials.html"><span class="drop-icon">💬</span> Client Testimonials</a>
                        <div class="dropdown-divider"></div>
                        <a href="our-partners.html"><span class="drop-icon">🤝</span> Our Partners</a>
                        <a href="our-happy-clients.html"><span class="drop-icon">😊</span> Our Happy Clients</a>"""

CSS_APPEND = """
/* Logo Carousel / Marquee */
.logo-marquee-container {
    overflow: hidden;
    white-space: nowrap;
    position: relative;
    padding: 3rem 0;
    width: 100%;
}
.logo-marquee-container::before, .logo-marquee-container::after {
    content: '';
    position: absolute;
    top: 0;
    width: 15vh;
    height: 100%;
    z-index: 2;
}
.logo-marquee-container::before {
    left: 0;
    background: linear-gradient(to right, var(--bg-dark), transparent);
}
.logo-marquee-container::after {
    right: 0;
    background: linear-gradient(to left, var(--bg-dark), transparent);
}
.logo-marquee-track {
    display: inline-block;
    animation: marquee 30s linear infinite;
}
.logo-marquee-track:hover {
    animation-play-state: paused;
}
.logo-item {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 200px;
    height: 100px;
    margin: 0 1.5rem;
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 8px;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
    cursor: default;
}
.logo-item:hover {
    border-color: var(--gold-primary);
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(255, 204, 0, 0.15);
}
.logo-item-text {
    font-family: 'Cinzel', serif;
    font-weight: 700;
    font-size: 1.1rem;
    color: var(--text-light);
    transition: color 0.3s ease;
    text-transform: uppercase;
    text-align: center;
    line-height: 1.2;
}
.logo-item:hover .logo-item-text {
    color: var(--gold-primary);
}
@keyframes marquee {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); } 
}
"""

def get_marquee_html(title, items, track_id=""):
    items_html = ""
    for item in items:
        icon, name = item
        items_html += f'''
                    <div class="logo-item">
                        <div class="logo-item-text"><div style="font-size: 1.8rem; margin-bottom: 5px;">{icon}</div>{name}</div>
                    </div>'''
    # We duplicate the items to make the infinite scroll smooth
    items_html *= 2
    
    return f"""
    <!-- {title} Section -->
    <section class="container section-padding animate-on-scroll up" {f'id="{track_id}"' if track_id else ''}>
        <h2 class="section-title">{title}</h2>
        <div class="logo-marquee-container">
            <div class="logo-marquee-track">
{items_html}
            </div>
        </div>
    </section>
"""

PARTNERS = [
    ("🏛️", "Legalist Alliance"),
    ("📈", "TaxPro Global"),
    ("💡", "IP Guardians"),
    ("📊", "Finance Hub"),
    ("🏢", "Corporate Connect"),
    ("🤝", "Gov Relations"),
    ("🌍", "Global Reach Law"),
    ("📋", "Audit Masters")
]

CLIENTS = [
    ("🚀", "Tech Innovators"),
    ("🏗️", "Alpha Construction"),
    ("⚕️", "Apex Medical"),
    ("🛍️", "Nova Retail"),
    ("⚙️", "Quantum Enterprises"),
    ("🌙", "Crescent Group"),
    ("📡", "Signal Logistics"),
    ("🏦", "Capital Ventures")
]


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | GET LEGAL SOLUTION</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <style>
        .internal-hero {{
            padding: 12rem 0 6rem;
            background: linear-gradient(135deg, var(--bg-dark) 0%, #111 100%);
            border-bottom: 1px solid var(--glass-border);
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
    </style>
</head>
<body>
    {nav}

    <!-- Hero -->
    <header class="internal-hero">
        <div class="container animate-on-scroll up">
            <h1>{title}</h1>
            <p>{desc}</p>
        </div>
    </header>

    {content}

    <!-- Footer -->
    {footer}

    <script src="content_db.js"></script>
    <script src="script.js"></script>
</body>
</html>
"""

def extract_section(file_path, start_tag, end_tag):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag, start_idx) + len(end_tag)
    
    if start_idx == -1 or end_idx < len(end_tag):
        return ""
        
    return content[start_idx:end_idx]

def extract_footer(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_idx = content.find('<footer class="footer">')
    end_idx = content.find('</footer>') + len('</footer>')
    
    return content[start_idx:end_idx]

def main():
    # 1. Update Navigation in existing HTML files
    html_files = glob.glob(os.path.join(DIR, '*.html'))
    for f in html_files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if NAV_OLD in content:
            new_content = content.replace(NAV_OLD, NAV_NEW)
            
            # Inject Carousels to index.html
            if os.path.basename(f) == "index.html":
                partners_html = get_marquee_html("Our Partners", PARTNERS)
                clients_html = get_marquee_html("Our Happy Clients", CLIENTS)
                
                # Insert right before services section
                target = '<!-- Services Section -->'
                if target in new_content and "Our Partners" not in new_content:
                    new_content = new_content.replace(target, partners_html + "\n" + clients_html + "\n" + target)
            
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated: {os.path.basename(f)}")

    # 2. Append CSS
    css_file = os.path.join(DIR, 'styles.css')
    with open(css_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
        
    if "logo-marquee-container" not in css_content:
        with open(css_file, 'a', encoding='utf-8') as f:
            f.write(CSS_APPEND)
        print("Updated: styles.css")

    # 3. Create new pages
    base_file = os.path.join(DIR, 'about-us.html')
    nav_html = extract_section(base_file, '<!-- Navbar -->', '</nav>')
    # Ensure nav is updated in the newly created string just in case
    nav_html = nav_html.replace(NAV_OLD, NAV_NEW)
    
    footer_html = extract_footer(base_file)

    # Our Partners
    partners_page = HTML_TEMPLATE.format(
        title="Our Partners",
        desc="We collaborate with top-tier organizations and professionals to bring you unparalleled comprehensive solutions.",
        nav=nav_html,
        content=get_marquee_html("Partnering for Excellence", PARTNERS),
        footer=footer_html
    )
    with open(os.path.join(DIR, 'our-partners.html'), 'w', encoding='utf-8') as f:
        f.write(partners_page)
        
    # Our Happy Clients
    clients_page = HTML_TEMPLATE.format(
        title="Our Happy Clients",
        desc="Trusted by hundreds of forward-thinking businesses and high-net-worth individuals across Pakistan.",
        nav=nav_html,
        content=get_marquee_html("Brands That Trust Us", CLIENTS),
        footer=footer_html
    )
    with open(os.path.join(DIR, 'our-happy-clients.html'), 'w', encoding='utf-8') as f:
        f.write(clients_page)

    print("Created: our-partners.html, our-happy-clients.html")

if __name__ == '__main__':
    main()
