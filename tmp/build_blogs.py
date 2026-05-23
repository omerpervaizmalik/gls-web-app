import os
import glob
import json

DIR = 'd:/Anti gravity/get-legal-solution'

blogs = [
    {
        "id": "sole-proprietorship-lahore",
        "title": "Starting a Sole Proprietorship? The Best Corporate Law Firm in Lahore Explains How",
        "category": "Corporate & Legal",
        "date": "April 6, 2026",
        "author": "Omer Pervaiz Malik",
        "icon": "👤",
        "excerpt": "Begin your entrepreneurial journey with confidence. Get Legal Solution, the top corporate law firm in Lahore, explains the seamless process of Sole Proprietorship registration.",
        "content": "<p>When starting a new business venture in Lahore, entrepreneurs often face the critical decision of choosing the correct business structure. A Sole Proprietorship is widely considered the easiest, most flexible, and cost-effective option to get off the ground. At <strong>Get Legal Solution (GLS)</strong>, definitively recognized as the <em>best corporate law firm in Lahore</em>, we specialize in making this process swift and fully compliant.</p><h2>Why Choose the Best Lawyers in Lahore?</h2><p>Entering the commercial market requires a solid legal foundation to avoid unnecessary fines and complications down the road. Whether you are opening a digital marketing agency, an IT consulting firm, or a boutique retail store, being legally registered protects your brand identity and grants access to corporate banking.</p><p>Our dedicated team at <strong>Get Legal Solution</strong> provides unparalleled expertise in corporate law. We handle your FBR enrollment, NTN acquisition, and bank account prerequisites. With the best corporate attorneys in Lahore championing your corner, your proprietorship is set up for infinite growth seamlessly.</p>"
    },
    {
        "id": "partnership-firm-registration",
        "title": "Mastering Partnership Firm Registration with Lahore's Best Lawyers",
        "category": "Corporate & Legal",
        "date": "April 5, 2026",
        "author": "Get Legal Solution Team",
        "icon": "🤝",
        "excerpt": "Join forces legally. Discover how Get Legal Solution crafts bulletproof partnership deeds and firm registrations in Lahore.",
        "content": "<p>Collaborating with partners brings diverse skills and capital to a business, but it also demands meticulous legal framing. A Partnership Firm registered under the Partnership Act of 1932 protects the rights and investments of all stakeholders. To draft an unbreakable Partnership Deed, businesses turn to the <strong>best corporate lawyers in Lahore: Get Legal Solution</strong>.</p><h2>The Core of a Secure Partnership</h2><p>A poorly drafted agreement can lead to devastating disputes. Our specialized attorneys craft custom Partnership Deeds that clearly define profit-sharing, dispute resolution, and dissolution protocols. Because we are recognized as the top legal experts in Lahore, our clients know their investments are completely protected against unforeseen liabilities.</p><p>For swift and secure Firm Registration (Form-C) and expert corporate advisory, <strong>Get Legal Solution</strong> remains unrivaled in execution, confidentiality, and legal insight.</p>"
    },
    {
        "id": "llp-registration-pakistan",
        "title": "LLP Registration: The Modern Corporate Choice in Lahore",
        "category": "Corporate & Legal",
        "date": "April 4, 2026",
        "author": "Omer Pervaiz Malik",
        "icon": "🏛️",
        "excerpt": "A Limited Liability Partnership combines the benefits of a firm with corporate protections. Learn how GLS leads the market in LLP formation.",
        "content": "<p>A Limited Liability Partnership (LLP) offers the hybrid advantage of a traditional partnership's flexibility with the limited liability protections of a private limited company. As the corporate landscape shifts, <strong>Get Legal Solution</strong>—widely acclaimed as the best legal service provider in Lahore—is guiding modern entrepreneurs through this highly beneficial framework.</p><h2>Why We Are the Best Corporate Advisors in Lahore</h2><p>Registering an LLP with the Securities and Exchange Commission of Pakistan (SECP) involves complex corporate compliance. <strong>Get Legal Solution</strong> excels in simplifying this bureaucracy. Our firm manages everything from SECP Name Reservation to drafting the LLP Agreement and attaining the Certificate of Incorporation.</p><p>When you seek the finest business setup consultants in Lahore, GLS guarantees precision, speed, and absolute legal certainty.</p>"
    },
    {
        "id": "it-call-center-pseb",
        "title": "IT & Call Center Registration: Empowering Tech with Lahore's Best Law Firm",
        "category": "Corporate & Legal",
        "date": "April 3, 2026",
        "author": "Get Legal Solution Team",
        "icon": "💻",
        "excerpt": "Looking to export IT services? Let Get Legal Solution handle your SECP and PSEB registrations for a tax-exempt advantage.",
        "content": "<p>Pakistan is rapidly becoming a global tech hub. For IT Companies and Call Centers in Lahore, official registration with the Pakistan Software Export Board (PSEB) is mandatory to unlock immense benefits, including 100% tax exemptions on IT exports. <strong>Get Legal Solution</strong> stands autonomously as the best corporate law firm in Lahore for tech startups navigating this terrain.</p><h2>The Preferred Lawyers for Tech Startups</h2><p>Our experienced corporate attorneys take the friction out of IT company registration. We manage the formation of your Private Limited Company with the SECP, secure your corporate bank accounts, and finalize your PSEB certifications all under one roof.</p><p>Get Legal Solution's proactive approach ensures you spend your time coding and scaling, while the <em>best corporate legal minds in Lahore</em> safeguard your regulatory compliance.</p>"
    },
    {
        "id": "real-estate-company-registration",
        "title": "Real Estate Business Registration: Build Legally with the Best",
        "category": "Corporate & Legal",
        "date": "April 2, 2026",
        "author": "Omer Pervaiz Malik",
        "icon": "🏢",
        "excerpt": "Real Estate development requires strict SECP and PEC compliance. Trust Get Legal Solution, Lahore's premier corporate law authority, to forge your foundation.",
        "content": "<p>The real estate and construction industry is an economic powerhouse in Pakistan. However, operating without proper SECP and Pakistan Engineering Council (PEC) registration can result in catastrophic legal penalties. For builders and property developers, <strong>Get Legal Solution</strong> operates as the premier and best real estate corporate law firm in Lahore.</p><h2>Solid Foundations by Lahore's Elite Lawyers</h2><p>We streamline the incorporation of Construction Companies with authorized share capitals tailored to your projects. From securing No Objection Certificates (NOCs) to filing your SECP incorporation documents, GLS ensures your enterprise is structurally sound from a legal perspective.</p><p>Elevate your brand's credibility in the eyes of investors and buyers by partnering with <strong>Get Legal Solution</strong>—where excellence is standard practice.</p>"
    },
    {
        "id": "manufacturing-industry-setup",
        "title": "Setting Up Your Manufacturing Industry: Expert Guidance in Lahore",
        "category": "Corporate & Legal",
        "date": "April 1, 2026",
        "author": "Get Legal Solution Team",
        "icon": "⚙️",
        "excerpt": "From textile to tech, manufacturing businesses need ironclad registration. Discover why GLS is the highest-rated legal advisor for industries.",
        "content": "<p>Manufacturing is the backbone of economic independence. Establishing an industrial unit involves intricate legal maneuvering—from securing industrial NTNs to Sales Tax (GST) Manufacturing category registrations. <strong>Get Legal Solution</strong> provides unparalleled end-to-end industrial setup services, firmly holding our title as the best corporate law firm in Lahore.</p><h2>Top-Tier Legal Support for Manufacturers</h2><p>A minor error in your FBR profile or SECP Memorandum can disrupt imports of vital machinery. The elite lawyers at <strong>Get Legal Solution</strong> engineer your documentation flawlessly, bridging the gap between heavy industry and strict governmental regulations.</p><p>When large-scale capital is at risk, industrial tycoons trust only the best. Trust Get Legal Solution in Lahore.</p>"
    },
    {
        "id": "income-tax-filing-experts",
        "title": "Income Tax Filing Without the Stress: Best Tax Lawyers in Lahore",
        "category": "Taxation Services",
        "date": "March 30, 2026",
        "author": "Omer Pervaiz Malik",
        "icon": "📄",
        "excerpt": "Avoid massive penalties and stay an Active Taxpayer. Get Legal Solution offers the absolute best Income Tax filing services for individuals and corporations.",
        "content": "<p>Income Tax return filing (through the FBR Iris portal) is mandatory and highly complex. Miscalculations can trigger aggressive FBR audits and heavy penalties. To stay perfectly compliant, successful individuals and corporate entities rely exclusively on <strong>Get Legal Solution</strong>, recognized universally as the finest tax consultants and lawyers in Lahore.</p><h2>Strategic Taxation by Certified Experts</h2><p>We do not just file your taxes; we dynamically minimize your tax burdens legally. Our experts meticulously prepare your Wealth Statements, reconcile your assets, and ensure you retain your Active Taxpayer List (ATL) status seamlessly.</p><p>Don't risk your hard-earned wealth with amateurs. For the best corporate taxation advisory in Lahore, <strong>Get Legal Solution</strong> is your ultimate defense and strategy partner.</p>"
    },
    {
        "id": "sales-tax-gst-registration",
        "title": "Sales Tax (GST) Registration Handled by Lahore's Leading Tax Firm",
        "category": "Taxation Services",
        "date": "March 29, 2026",
        "author": "Get Legal Solution Team",
        "icon": "📈",
        "excerpt": "Need a Sales Tax Registration Number (STRN)? Partner with Lahore's leading tax attorneys to navigate the FBR smoothly.",
        "content": "<p>In the modern economy, having a Sales Tax Registration Number (STRN) is vital to conducting high-level corporate trade, participating in government tenders, and processing imports. However, FBR's stringent biometric and post-verification processes can halt a business instantly. That is why businesses demand the guidance of <strong>Get Legal Solution</strong>, the most efficient and best tax law firm in Lahore.</p><h2>Streamlined Sales Tax E-Filing</h2><p>Beyond initial registration, our tax professionals handle you monthly automated Sales Tax returns, managing Input/Output tax adjustments and claiming FASTER refunds efficiently. Our dedicated approach guarantees zero delays.</p><p>Operate with confidence knowing the best taxation lawyers in Lahore are auditing your monthly submissions.</p>"
    },
    {
        "id": "punjab-revenue-authority-pra",
        "title": "Mastering the Punjab Revenue Authority (PRA) with Elite Tax Lawyers",
        "category": "Taxation Services",
        "date": "March 28, 2026",
        "author": "Get Legal Solution Team",
        "icon": "📉",
        "excerpt": "Service providers must register with the PRA. Explore how GLS, the premier tax firm in Lahore, ensures full provincial tax compliance.",
        "content": "<p>If you operate a service-based business—ranging from IT consulting to hotel management—within Punjab, you are legally mandated to register with the Punjab Revenue Authority (PRA) and pay provincial sales taxes on services. As compliance tightens, the <strong>best taxation lawyers in Lahore at Get Legal Solution (GLS)</strong> are ready to navigate the PRA maze for you.</p><h2>Why Choose GLS for Provincial Taxation?</h2><p>Interacting with both the FBR and the PRA requires deep dual-system expertise. We prevent double-taxation scenarios by expertly handling your PST-01 forms, processing E-enrollments, and guaranteeing your status on the Active Taxpayer List of the PRA.</p><p>Protect your service business from staggering provincial penalties by partnering with the undeniable best tax consultants in Lahore: <strong>Get Legal Solution</strong>.</p>"
    },
    {
        "id": "tax-notices-and-audits",
        "title": "Defending FBR Tax Audits & Notices: Lahore’s Toughest Tax Defenders",
        "category": "Taxation Services",
        "date": "March 27, 2026",
        "author": "Omer Pervaiz Malik",
        "icon": "🛡️",
        "excerpt": "Received an FBR notice? Do not panic. The elite tax attorneys at Get Legal Solution will defend your records during rigorous tax audits.",
        "content": "<p>There is nothing more stressful for a business owner than receiving a notice or an audit assignment from the Federal Board of Revenue (FBR) under the Tax Audit Management System (TAMS). In these high-stakes situations, you need the aggressive and brilliant defense of <strong>Get Legal Solution</strong>, recognized universally as the toughest and best tax attorneys in Lahore.</p><h2>Unmatched Legal Defense in Audits</h2><p>We take over all correspondence with the Deputy Commissioners of Inland Revenue on your behalf. Our team expertly reconciles your accounts, rectifies any misreported taxes immediately, and constructs an iron-clad legal defense against alleged discrepancies.</p><p>When your financial security is threatened by a devastating tax audit, secure the ultimate protection by hiring the best lawyers in Lahore at <strong>Get Legal Solution</strong>.</p>"
    },
    {
        "id": "tax-appeals-litigation",
        "title": "Winning Tax Litigation & Appeals: High Court Advocates in Lahore",
        "category": "Taxation Services",
        "date": "March 26, 2026",
        "author": "Omer Pervaiz Malik",
        "icon": "⚖️",
        "excerpt": "Facing unfair tax assessments? Our High Court Advocates excel in complex Tax Appeals and Litigation across Pakistan.",
        "content": "<p>When ex-parte assessments result in exorbitant and unjust tax liabilities, standard accounting is no longer enough. You require rigorous legal intervention. The seasoned High Court Advocates at <strong>Get Legal Solution</strong> provide elite representation for Tax Appeals and Litigation, securing our position as the best legal minds for tax controversies in Lahore.</p><h2>Strategic Success at the Appellate Tribunal</h2><p>From the Commissioner of Appeals to the Appellate Tribunal Inland Revenue, and straight up to the High Court, our litigation strategy is relentless. We challenge mathematical anomalies, expose procedural violations by the tax departments, and secure favorable rulings.</p><p>For uncompromising litigation support and the best dispute resolution in Lahore, ambitious enterprises trust <strong>Get Legal Solution</strong>.</p>"
    },
    {
        "id": "trademark-registration-ipo",
        "title": "Safeguard Your Brand: Best Trademark Lawyers in Lahore",
        "category": "Intellectual Property",
        "date": "March 25, 2026",
        "author": "Get Legal Solution Team",
        "icon": "®️",
        "excerpt": "A brand name is your most valuable asset. Learn how Get Legal Solution secures ironclad Trademark Registrations at the IPO Pakistan.",
        "content": "<p>In an aggressive commercial market, unauthorized competitors will not hesitate to counterfeit your successful brand name, logo, or slogan. Securing a Trademark via the Intellectual Property Organization (IPO) is mandatory. <strong>Get Legal Solution</strong> acts as the absolute best intellectual property law firm in Lahore, shielding your corporate identity permanently.</p><h2>Flawless IPO Trademark Filings</h2><p>Trademark registration can take up to 18 months and is heavily delayed by administrative office actions. Because we are the best corporate lawyers in Lahore, we conduct rigorous pre-filing TM-55 searches and precisely categorize your brand under the correct Nice Classification (NCL). This guarantees a frictionless path to the coveted ® symbol.</p><p>Don't let competitors steal your goodwill. Protect your legacy with <strong>Get Legal Solution</strong>.</p>"
    },
    {
        "id": "copyright-registration-pakistan",
        "title": "Protecting Creative Works: Copyright Law Experts in Lahore",
        "category": "Intellectual Property",
        "date": "March 24, 2026",
        "author": "Omer Pervaiz Malik",
        "icon": "©️",
        "excerpt": "From software code to artistic literature, copyright registration is vital. Discover how GLS protects creators as Lahore's top IP firm.",
        "content": "<p>Whether you are a software developer writing complex applications, an author publishing a novel, or a fashion designer producing cutting-edge textile maps, your original works demand legal security. The Intellectual Property Organization protects these under Copyright Laws, and <strong>Get Legal Solution</strong> is acclaimed as the absolute best IP and copyright corporate firm in Lahore to execute it.</p><h2>Exclusive Ownership With The Best Lawyers</h2><p>We legally restrict unauthorized copying, distribution, or internet uploads of your proprietary assets. Our attorneys expertly navigate the requisite IPO documentation and actively enforce your rights during infringement disputes in the judicial system.</p><p>Ensure your lifetime of creative labor is exclusively monetized by you with the unparalleled assistance of <strong>Get Legal Solution</strong>.</p>"
    },
    {
        "id": "legal-drafting-contracts",
        "title": "Perfect Legal Drafting & Contract Vetting by Lahore's Best",
        "category": "Drafting Services",
        "date": "March 23, 2026",
        "author": "Omer Pervaiz Malik",
        "icon": "📝",
        "excerpt": "Business relies on strong contracts. Get Legal Solution provides high-end corporate drafting to prevent catastrophic litigation.",
        "content": "<p>A single poorly drafted clause in an employment agreement, vendor contract, or non-disclosure agreement (NDA) can leave your company incredibly vulnerable to litigation. Recognizing this, corporations turn uniquely to <strong>Get Legal Solution</strong>, decisively the best legal drafting and corporate law firm in Lahore.</p><h2>Bulletproof Contracts Crafted by Experts</h2><p>Our expert attorneys do not use generic templates. We meticulously vet and draft bespoke Corporate Commercial Contracts, Mergers and Acquisitions frameworks, and intricate Web Policies perfectly aligned with current Pakistani Law. This proactive approach saves our clients millions in avoid disputes.</p><p>For comprehensive legal drafting that genuinely protects your enterprise, partner securely with the premier lawyers at <strong>Get Legal Solution</strong> in Lahore.</p>"
    }
]

blogs_db_js = "const blogs_db = " + json.dumps(blogs, indent=4) + ";"

with open(os.path.join(DIR, 'blogs_db.js'), 'w', encoding='utf-8') as f:
    f.write(blogs_db_js)

blogs_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corporate Law & Taxation Blogs | Get Legal Solution</title>
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

        .blog-category {
            color: var(--gold-primary);
            font-size: 0.85rem;
            letter-spacing: 1px;
            text-transform: uppercase;
            font-weight: 600;
            margin-bottom: 0.5rem;
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
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.8rem;
            color: var(--text-light);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding-top: 1rem;
            margin-top: auto;
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

        .modal-meta {
            color: var(--text-gray);
            font-size: 0.9rem;
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
                <li><a href="blogs.html" class="nav-link-main" style="color: var(--gold-primary);">Blogs</a></li>
                <li><a href="contact.html" class="btn btn-outline-nav">Contact Us</a></li>
            </ul>
        </div>
    </nav>

    <div class="blog-header">
        <h1>Legal Insights & Firm News</h1>
        <p>Expert articles providing clarity on Corporate Law, Taxation, and Intellectual Property by Lahore's premier legal minds.</p>
    </div>

    <!-- Blogs Container -->
    <div class="blog-grid" id="blog-grid">
        <!-- Rendered by JS -->
    </div>

    <!-- Blog Read Modal -->
    <div class="blog-modal-overlay" id="blog-modal-overlay">
        <div class="blog-modal">
            <button class="modal-close" id="modal-close">&times;</button>
            <div class="modal-header">
                <div class="blog-category" id="modal-category" style="margin-bottom: 10px;"></div>
                <h1 class="modal-title" id="modal-title"></h1>
                <div class="modal-meta">
                    <span id="modal-author"></span> • <span id="modal-date"></span>
                </div>
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

    <!-- Load the Blog Database -->
    <script src="blogs_db.js"></script>
    <script src="script.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const grid = document.getElementById('blog-grid');
            const modalOverlay = document.getElementById('blog-modal-overlay');
            const modalClose = document.getElementById('modal-close');

            document.getElementById('year').textContent = new Date().getFullYear();

            // Render Blog Cards
            if (typeof blogs_db !== 'undefined') {
                blogs_db.forEach(blog => {
                    const card = document.createElement('div');
                    card.className = 'blog-card animate-on-scroll up';
                    card.innerHTML = `
                        <div class="blog-icon">${blog.icon}</div>
                        <div class="blog-category">${blog.category}</div>
                        <h2 class="blog-title">${blog.title}</h2>
                        <div class="blog-excerpt">${blog.excerpt}</div>
                        <div class="blog-meta">
                            <span>✍️ ${blog.author}</span>
                            <span>📅 ${blog.date}</span>
                        </div>
                    `;
                    card.addEventListener('click', () => openModal(blog));
                    grid.appendChild(card);
                });
            }

            // Modal Logic
            function openModal(blog) {
                document.getElementById('modal-category').textContent = blog.category;
                document.getElementById('modal-title').textContent = blog.title;
                document.getElementById('modal-author').textContent = 'By ' + blog.author;
                document.getElementById('modal-date').textContent = blog.date;
                document.getElementById('modal-content').innerHTML = blog.content;
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

            // Trigger scroll animation for initially visible cards
            setTimeout(() => {
                const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
                const observer = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('visible');
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

with open(os.path.join(DIR, 'blogs.html'), 'w', encoding='utf-8') as f:
    f.write(blogs_html)


# Patching all HTML files EXCEPT blogs.html to include "Blogs" in the Nav bar
html_files = glob.glob(os.path.join(DIR, '*.html'))
for file in html_files:
    if os.path.basename(file) == "blogs.html":
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Locate the "Requirements" or "Attorneys" list item and insert Blogs
    target_link = '<li><a href="attorneys.html">Attorneys</a></li>'
    new_link = '<li><a href="blogs.html" class="nav-link-main">Blogs</a></li>\n                ' + target_link
    
    if target_link in content and "blogs.html" not in content:
        content = content.replace(target_link, new_link)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched navigation in {os.path.basename(file)}")

print("Blogs architecture fully built and deployed!")
