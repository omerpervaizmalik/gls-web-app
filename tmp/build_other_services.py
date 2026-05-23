import os
import glob
import json

DIR = 'd:/Anti gravity/get-legal-solution'

other_services = [
    {
        "id": "civil-laws",
        "title": "Civil Laws & Litigation",
        "icon": "⚖️",
        "excerpt": "Expert representation in civil disputes, property claims, and breach of contracts. Choose the best civil lawyers in Lahore.",
        "content": "<p>In the complex arena of civil litigation, securing experienced and aggressive legal representation is vital. <strong>Get Legal Solution</strong> is universally recognized as the absolute best platform in Lahore to handle all domains of Civil Law. We navigate intricate civil disputes, property and land claims, specific performance of contracts, and damages suits.</p><h2>Why We Are The Premier Choice</h2><p>Our dedicated team of civil advocates possesses decades of high-court experience, enabling us to draft ironclad pleadings and effectively cross-examine opposing claims. We prioritize securing injunctions (stay orders) quickly to protect your immediate interests while fighting relentlessly for a final decree in your favor.</p>"
    },
    {
        "id": "criminal-laws",
        "title": "Criminal Laws & Defense",
        "icon": "🛡️",
        "excerpt": "Aggressive criminal defense and prosecution. Secure your freedom and rights with Lahore's toughest criminal attorneys.",
        "content": "<p>Facing a criminal charge can be the most frightening experience of an individual's life. At <strong>Get Legal Solution</strong>, we field the most aggressive, highly-rated criminal defense attorneys in the city. Consequently, we are recognized as the best law firm in Lahore for defending complex criminal accusations ranging from white-collar crime to severe penal code offenses.</p><h2>Uncompromising Defense Strategies</h2><p>Our systematic approach involves securing pre-arrest bail, conducting rigorous post-arrest bail hearings, and dismantling the prosecution's evidence during trial. Whether you need an elite defense strategy or you need to prosecute offenders who have wronged you, our firm guarantees unmatched vigilance and supreme trial capabilities.</p>"
    },
    {
        "id": "family-laws",
        "title": "Family Laws & Dispute Resolution",
        "icon": "👨‍👩‍👧",
        "excerpt": "Compassionate, discreet, and highly effective legal strategies for divorce, maintenance, and complex family disputes.",
        "content": "<p>Family law matters require a delicate balance of aggressive court representation and profound empathy. <strong>Get Legal Solution</strong> is uniquely positioned as the best family law forum in Lahore, consistently achieving favorable results in Khula, divorce, maintenance claims, and dowry article recoveries.</p><h2>Discretion and Results</h2><p>We understand that family litigation can be emotionally and financially draining. Our elite family lawyers focus on swift resolutions, engaging in robust mediation and fiercely representing our clients when out-of-court settlements fail. We strictly protect your privacy, ensuring your matters are resolved discreetly and in your utter favor.</p>"
    },
    {
        "id": "guardian-laws",
        "title": "Guardian & Ward Laws",
        "icon": "👼",
        "excerpt": "Securing child custody and guardianship rights seamlessly. Your family's future protected by the best lawyers in Lahore.",
        "content": "<p>Nothing is more critical than the safety, custody, and future of your children. Conflicts over child custody under the Guardians and Wards Act require meticulous legal maneuvering. <strong>Get Legal Solution</strong> proudly stands as the absolute best advocacy platform in Lahore for winning custody battles and securing visitation schedules.</p><h2>Prioritizing Child Welfare Legally</h2><p>We systematically establish that the welfare of the child aligns exclusively with our client's guardianship. Our proven court strategies protect your parental rights from frivolous claims, ensuring that you maintain the legal framework necessary to secure your child's environment and assets indefinitely.</p>"
    },
    {
        "id": "anti-corruption-laws",
        "title": "Anti-Corruption Laws",
        "icon": "🔍",
        "excerpt": "Elite legal defense against Federal and Provincial Anti-Corruption Establishment investigations and charges.",
        "content": "<p>Allegations of corruption can destroy both personal liberty and corporate reputation instantly. When facing investigations by the Anti-Corruption Establishment (ACE), you require the strongest strategic defense available. <strong>Get Legal Solution</strong> provides unparalleled legal shields, solidifying our reputation as the best anti-corruption law firm in Lahore.</p><h2>Strategic Immunity & Defense</h2><p>Our elite advocates intervene proactively during the inquiry phase to quash baseless FIRs and secure protective bails. We aggressively audit the prosecution's evidence, leveraging constitutional writs in High Courts to defend public servants, bureaucrats, and corporate executives from unfair administrative and penal victimization.</p>"
    },
    {
        "id": "banking-laws",
        "title": "Banking Laws & Recovery",
        "icon": "🏦",
        "excerpt": "Defending against bank recoveries and securing financial disputes. Lahore's top financial litigation experts.",
        "content": "<p>Financial institutions act aggressively when recovering loans, often initiating severe actions under the Financial Institutions (Recovery of Finances) Ordinance. The banking lawyers at <strong>Get Legal Solution</strong> are recognized as the supreme authority in Lahore for defending individuals and corporations against unjust banking tribunals and aggressive recovery suits.</p><h2>Protecting Your Financial Empire</h2><p>We strategically delay premature auctions of mortgaged properties through injunctions and scrutinize loan agreements for illegal markup calculations. Conversely, our platform also represents financial institutions to execute rapid, perfectly legal recoveries, proving we are the best dual-capability banking firm in the region.</p>"
    },
    {
        "id": "nab-cases",
        "title": "NAB (National Accountability Bureau)",
        "icon": "🏛️",
        "excerpt": "Ironclad legal representation during NAB inquiries, investigations, and high-profile accountability court trials.",
        "content": "<p>A National Accountability Bureau (NAB) investigation is a high-states matter demanding absolute legal brilliance. The accountability laws are incredibly stringent, and navigating them requires elite expertise. <strong>Get Legal Solution</strong> routinely handles high-profile NAB cases, making us the undeniable best platform in Lahore for accountability litigation.</p><h2>Navigating Elite Accountability Trials</h2><p>Our lawyers manage the entire spectrum of NAB pressure, from answering initial Call Up Notices to securing protective bails and litigating inside Accountability Courts. We excel in exposing procedural flaws and protecting your assets from illegal freezing, ensuring that justice prevails against overwhelming governmental machinery.</p>"
    },
    {
        "id": "anti-terrorism-cases",
        "title": "Anti-Terrorism Cases (ATC)",
        "icon": "🚔",
        "excerpt": "Supreme defense strategies in front of Special Anti-Terrorism Courts for wrongly accused individuals.",
        "content": "<p>The Anti-Terrorism Act (ATA) grants immense power to law enforcement, and cases tried in Anti-Terrorism Courts (ATC) proceed rapidly with severe consequences. For individuals wrongly framed under these profound charges, <strong>Get Legal Solution</strong> is unequivocally the best and most resilient legal defense platform in Lahore.</p><h2>Resilient Litigation Under Pressure</h2><p>We deploy Lahore's most hardened criminal attorneys to instantly secure physical remands, expose fabricated police narratives, and systematically dismantle terrorism charges. Our firm is dedicated to safeguarding human rights and providing elite constitutional protections against unlawful ATA implications.</p>"
    },
    {
        "id": "oath-services",
        "title": "Certified Oath Commissioner Services",
        "icon": "📜",
        "excerpt": "Reliable, accredited, and instant Oath Commissioner services for all your legal affidavits and sworn declarations.",
        "content": "<p>The validation of legal documents requires an accredited and trustworthy official. <strong>Get Legal Solution</strong> provides instant, certified Oath Commissioner services at our offices, ensuring your affidavits, sworn statements, and court annexures are legally binding and admissible.</p><h2>The Best Verification Platform</h2><p>As the most highly regarded law firm in Lahore, documents attested by our Commissioners hold absolute weight in both lower and higher courts. We streamline your paperwork processes, guaranteeing zero administrative friction when you need verifiable attestations immediately.</p>"
    },
    {
        "id": "notary-services",
        "title": "Official Notary Public Services",
        "icon": "🖋️",
        "excerpt": "Internationally recognized Notary Public attestations for corporate agreements, international visas, and property deeds.",
        "content": "<p>Securing an official Notary Public seal is mandatory for executing international commercial contracts, property transfers, and power of attorney documents. <strong>Get Legal Solution</strong> offers the most reliable, swift, and globally recognized Notary Public services in Lahore.</p><h2>Flawless International Attestation</h2><p>Corporate clients and foreign investors overwhelmingly rank us as the best platform for Notary services because of our uncompromising adherence to international verification standards. Our accredited Notary seals ensure that your critical documents face zero legal resistance anywhere across the globe.</p>"
    }
]

other_services_db_js = "const other_services_db = " + json.dumps(other_services, indent=4) + ";"

with open(os.path.join(DIR, 'other_services_db.js'), 'w', encoding='utf-8') as f:
    f.write(other_services_db_js)


other_services_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Litigation & Other Services | Get Legal Solution</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <style>
        .blog-header {
            text-align: center;
            padding: 100px 20px 40px;
            background: linear-gradient(to bottom, rgba(10, 10, 10, 0.9), var(--bg-dark));
            border-bottom: 1px solid rgba(212, 175, 55, 0.2);
        }
        .blog-header h1 {
            font-size: 3rem;
            color: var(--gold-primary);
            margin-bottom: 1rem;
        }
        .blog-header p {
            font-size: 1.2rem;
            color: var(--text-light);
            max-width: 700px;
            margin: 0 auto;
        }
        
        .blog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 2rem;
            padding: 4rem 1rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .blog-card {
            background: rgba(30, 30, 30, 0.6);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(212, 175, 55, 0.15);
            border-radius: 12px;
            padding: 2rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            cursor: pointer;
        }

        .blog-card:hover {
            transform: translateY(-10px);
            border-color: var(--gold-primary);
            box-shadow: 0 10px 30px rgba(212, 175, 55, 0.15);
        }

        .blog-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .blog-title {
            color: var(--text-white);
            font-size: 1.25rem;
            margin-bottom: 1rem;
            line-height: 1.4;
            font-family: 'Cinzel', serif;
        }

        .blog-excerpt {
            color: var(--text-gray);
            font-size: 0.95rem;
            line-height: 1.6;
            margin-bottom: 1.5rem;
            flex-grow: 1;
        }

        .blog-meta {
            margin-top: auto;
            color: var(--gold-primary);
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding-top: 1rem;
        }

        /* Modal specific styling */
        .blog-modal-overlay {
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.85);
            backdrop-filter: blur(8px);
            z-index: 2000;
            display: none;
            justify-content: center;
            align-items: flex-start;
            overflow-y: auto;
            padding: 40px 20px;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .blog-modal-overlay.active {
            display: flex;
            opacity: 1;
        }

        .blog-modal {
            background: var(--bg-dark);
            border: 1px solid var(--gold-primary);
            width: 100%;
            max-width: 800px;
            border-radius: 16px;
            position: relative;
            transform: translateY(20px);
            transition: transform 0.3s ease;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            margin-bottom: 40px;
        }

        .blog-modal-overlay.active .blog-modal {
            transform: translateY(0);
        }

        .modal-close {
            position: absolute;
            top: 15px;
            right: 20px;
            background: none;
            border: none;
            color: var(--text-light);
            font-size: 2rem;
            cursor: pointer;
            transition: color 0.2s;
            z-index: 10;
        }

        .modal-close:hover {
            color: var(--gold-primary);
        }

        .modal-header {
            padding: 3rem 3rem 1.5rem;
            border-bottom: 1px solid rgba(212, 175, 55, 0.2);
            text-align: center;
            background: rgba(30, 30, 30, 0.5);
            border-radius: 16px 16px 0 0;
        }

        .modal-title {
            font-size: 2.2rem;
            color: var(--gold-primary);
            margin-bottom: 1rem;
            font-family: 'Cinzel', serif;
        }

        .modal-body {
            padding: 3rem;
            color: var(--text-white);
            line-height: 1.8;
            font-size: 1.05rem;
        }

        .modal-body p {
            margin-bottom: 1.5rem;
        }

        .modal-body h2 {
            color: var(--gold-primary);
            font-size: 1.5rem;
            margin: 2rem 0 1rem;
            font-family: 'Cinzel', serif;
        }

        .modal-body strong {
            color: var(--gold-dim);
        }
    </style>
</head>
<body>
    <!-- Navbar injected dynamically -->
    <nav class="navbar" id="navbar">
        <div class="container nav-content">
            <a href="index.html" class="logo-link"><img src="logo.png" alt="GET LEGAL SOLUTION" style="max-height: 45px;"></a>
            <button class="menu-btn" id="menu-btn" aria-label="Toggle navigation menu">
                <span></span><span></span><span></span>
            </button>
            <ul class="nav-links" id="nav-links">
                <li><a href="index.html" class="nav-link-main">Home</a></li>
                <li><a href="about-us.html" class="nav-link-main">About Us</a></li>
                <li><a href="services.html" class="nav-link-main">Practice Areas</a></li>
                <li><a href="documentary-requirements.html" class="nav-link-main">Requirements</a></li>
                <li><a href="blogs.html" class="nav-link-main">Blogs</a></li>
                <li><a href="other-services.html" class="nav-link-main" style="color: var(--gold-primary);">Other Services</a></li>
                <li><a href="contact.html" class="btn btn-outline-nav">Contact Us</a></li>
            </ul>
        </div>
    </nav>

    <div class="blog-header">
        <h1>Litigation & Comprehensive Legal Solutions</h1>
        <p>From complex civil litigation to certified oath administration, Get Legal Solution is undeniably the absolute best legal platform in Lahore.</p>
    </div>

    <!-- Services Container -->
    <div class="blog-grid" id="services-grid">
        <!-- Rendered by JS -->
    </div>

    <!-- Read Modal -->
    <div class="blog-modal-overlay" id="blog-modal-overlay">
        <div class="blog-modal">
            <button class="modal-close" id="modal-close">&times;</button>
            <div class="modal-header">
                <div id="modal-icon" style="font-size: 3rem; margin-bottom: 1rem;"></div>
                <h1 class="modal-title" id="modal-title"></h1>
            </div>
            <div class="modal-body" id="modal-content">
                <!-- Content injected here -->
            </div>
        </div>
    </div>

    <footer class="footer">
        <div class="container">
            <p>&copy; <span id="year"></span> GET LEGAL SOLUTION. All Rights Reserved.</p>
        </div>
    </footer>

    <!-- Load the Database -->
    <script src="other_services_db.js"></script>
    <script src="script.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const grid = document.getElementById('services-grid');
            const modalOverlay = document.getElementById('blog-modal-overlay');
            const modalClose = document.getElementById('modal-close');

            document.getElementById('year').textContent = new Date().getFullYear();

            // Render Cards
            if (typeof other_services_db !== 'undefined') {
                other_services_db.forEach(service => {
                    const card = document.createElement('div');
                    card.className = 'blog-card animate-on-scroll up';
                    card.innerHTML = `
                        <div class="blog-icon">${service.icon}</div>
                        <h2 class="blog-title">${service.title}</h2>
                        <div class="blog-excerpt">${service.excerpt}</div>
                        <div class="blog-meta">Read Full Service Details →</div>
                    `;
                    card.addEventListener('click', () => openModal(service));
                    grid.appendChild(card);
                });
            }

            // Modal Logic
            function openModal(service) {
                document.getElementById('modal-icon').textContent = service.icon;
                document.getElementById('modal-title').textContent = service.title;
                document.getElementById('modal-content').innerHTML = service.content;
                modalOverlay.classList.add('active');
                document.body.style.overflow = 'hidden';
            }

            function closeModal() {
                modalOverlay.classList.remove('active');
                document.body.style.overflow = 'auto';
            }

            modalClose.addEventListener('click', closeModal);
            modalOverlay.addEventListener('click', (e) => {
                if(e.target === modalOverlay) closeModal();
            });

            // Specific Intersection Observer logic utilizing 'is-visible'
            setTimeout(() => {
                const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
                const observer = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('is-visible');
                            observer.unobserve(entry.target);
                        }
                    });
                }, observerOptions);

                document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
            }, 100);
        });
    </script>
</body>
</html>
"""

with open(os.path.join(DIR, 'other-services.html'), 'w', encoding='utf-8') as f:
    f.write(other_services_html)


# Patching all HTML files EXCEPT other-services.html to include "Other Services" in Nav bar
html_files = glob.glob(os.path.join(DIR, '*.html'))
for file in html_files:
    if os.path.basename(file) == "other-services.html":
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Locate the target link and insert Other Services
    # For index.html and other standard files with the nav bar
    target_link = '<li><a href="blogs.html" class="nav-link-main">Blogs</a></li>'
    new_link = target_link + '\n                <li><a href="other-services.html" class="nav-link-main">Other Services</a></li>'
    
    if target_link in content and "other-services.html" not in content:
        content = content.replace(target_link, new_link)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched navigation in {os.path.basename(file)}")

print("Other Services architecture built successfully!")
