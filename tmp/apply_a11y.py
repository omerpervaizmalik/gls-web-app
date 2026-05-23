import os
import glob
import re

DIR = 'd:/Anti gravity/get-legal-solution'

CSS_A11Y = """
/* ==========================================================================
   A11Y (Accessibility) OVERRIDES & THEMES
   ========================================================================== */

/* Focus Styles - highly visible outline for keyboard navigation */
*:focus-visible {
    outline: 3px solid var(--gold-primary) !important;
    outline-offset: 4px !important;
    box-shadow: 0 0 10px rgba(255, 204, 0, 0.8) !important;
}

/* High Contrast Mode */
body.a11y-high-contrast, 
body.a11y-high-contrast * {
    background-color: #000000 !important;
    background-image: none !important;
    color: #FFFF00 !important;
    border-color: #FFFF00 !important;
    box-shadow: none !important;
    text-shadow: none !important;
}
body.a11y-high-contrast img {
    filter: contrast(120%) !important;
}
body.a11y-high-contrast a, 
body.a11y-high-contrast button {
    text-decoration: underline !important;
    color: #FFFFFF !important;
}

/* Highlight Links */
body.a11y-highlight-links a {
    text-decoration: underline !important;
    text-decoration-thickness: 3px !important;
    text-underline-offset: 3px !important;
    background-color: rgba(255, 255, 0, 0.1) !important;
    color: var(--gold-primary) !important;
}

/* Dyslexia Friendly / Readable Font */
body.a11y-readable-font * {
    font-family: 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    letter-spacing: 1px !important;
    word-spacing: 2px !important;
    line-height: 1.8 !important;
}

/* Text Scaling */
html.a11y-text-large { font-size: 115% !important; }
html.a11y-text-xlarge { font-size: 130% !important; }

/* Reduced Motion */
body.a11y-reduced-motion,
body.a11y-reduced-motion * {
    animation: none !important;
    transition: none !important;
    scroll-behavior: auto !important;
}

/* -----------------------------------------------------------
   A11Y WIDGET STYLES
   ----------------------------------------------------------- */
.a11y-widget-btn {
    position: fixed;
    bottom: 20px;
    left: 20px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background-color: #005A9C;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    cursor: pointer;
    z-index: 10000;
    transition: transform 0.3s ease;
    border: 2px solid white;
}
.a11y-widget-btn:hover {
    transform: scale(1.1);
}
.a11y-widget-btn svg {
    width: 35px;
    height: 35px;
    fill: currentColor;
}

.a11y-panel {
    position: fixed;
    bottom: 90px;
    left: 20px;
    width: 320px;
    background: #020409;
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.8);
    z-index: 9999;
    padding: 1.5rem;
    transform: translateY(20px);
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
}
.a11y-panel.open {
    transform: translateY(0);
    opacity: 1;
    visibility: visible;
}
.a11y-panel-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--glass-border);
    padding-bottom: 1rem;
    margin-bottom: 1rem;
}
.a11y-panel-header h3 {
    font-size: 1.1rem;
    color: var(--text-white);
    margin: 0;
    font-family: 'Inter', sans-serif;
}
.a11y-close {
    background: none;
    border: none;
    color: var(--text-light);
    font-size: 1.5rem;
    cursor: pointer;
}
.a11y-controls {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}
.a11y-setting-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.a11y-setting-label {
    font-size: 0.95rem;
    color: var(--text-light);
}
.a11y-toggle-btn {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    color: var(--text-white);
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s;
    font-size: 0.85rem;
}
.a11y-toggle-btn.active {
    background: var(--gold-primary);
    color: #000;
    border-color: var(--gold-primary);
}
.a11y-btn-group {
    display: flex;
    gap: 5px;
}
.a11y-btn-group button {
    flex: 1;
}
"""

JS_A11Y = """
// ==========================================================================
// A11Y (ACCESSIBILITY) WIDGET INJECTION & LOGIC
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
    // Inject HTML
    const a11yHTML = `
    <button class="a11y-widget-btn" id="a11y-widget-btn" aria-label="Open Accessibility Menu" aria-haspopup="true" aria-expanded="false">
        <svg viewBox="0 0 24 24">
            <path d="M12 2c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm9 7h-6v13h-2v-6h-2v6H9V9H3V7h18v2z"/>
        </svg>
    </button>
    
    <div class="a11y-panel" id="a11y-panel" role="dialog" aria-modal="true" aria-labelledby="a11y-title">
        <div class="a11y-panel-header">
            <h3 id="a11y-title">Accessibility Tools</h3>
            <button class="a11y-close" id="a11y-close" aria-label="Close Accessibility Menu">&times;</button>
        </div>
        <div class="a11y-controls">
            
            <div class="a11y-setting-row">
                <span class="a11y-setting-label">Text Size</span>
                <div class="a11y-btn-group">
                    <button class="a11y-toggle-btn" id="btn-text-decrease" aria-label="Decrease text size">A-</button>
                    <button class="a11y-toggle-btn" id="btn-text-reset" aria-label="Default text size">A</button>
                    <button class="a11y-toggle-btn" id="btn-text-increase" aria-label="Increase text size">A+</button>
                </div>
            </div>
            
            <div class="a11y-setting-row">
                <span class="a11y-setting-label">High Contrast</span>
                <button class="a11y-toggle-btn" id="tgl-contrast" aria-pressed="false">Toggle</button>
            </div>
            
            <div class="a11y-setting-row">
                <span class="a11y-setting-label">Highlight Links</span>
                <button class="a11y-toggle-btn" id="tgl-links" aria-pressed="false">Toggle</button>
            </div>
            
            <div class="a11y-setting-row">
                <span class="a11y-setting-label">Readable Font</span>
                <button class="a11y-toggle-btn" id="tgl-font" aria-pressed="false">Toggle</button>
            </div>
            
            <div class="a11y-setting-row">
                <span class="a11y-setting-label">Pause Animations</span>
                <button class="a11y-toggle-btn" id="tgl-motion" aria-pressed="false">Toggle</button>
            </div>

            <div class="a11y-setting-row" style="justify-content: center; margin-top: 10px;">
                <button class="a11y-toggle-btn" id="btn-a11y-reset" style="width: 100%;">Reset All Settings</button>
            </div>
        </div>
    </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', a11yHTML);

    // DOM Elements
    const widgetBtn = document.getElementById('a11y-widget-btn');
    const panel = document.getElementById('a11y-panel');
    const closeBtn = document.getElementById('a11y-close');
    
    const tglContrast = document.getElementById('tgl-contrast');
    const tglLinks = document.getElementById('tgl-links');
    const tglFont = document.getElementById('tgl-font');
    const tglMotion = document.getElementById('tgl-motion');
    const btnIncrease = document.getElementById('btn-text-increase');
    const btnDecrease = document.getElementById('btn-text-decrease');
    const btnReset = document.getElementById('btn-text-reset');
    const btnResetAll = document.getElementById('btn-a11y-reset');

    // State Default
    let a11yState = {
        contrast: false,
        links: false,
        font: false,
        motion: false,
        textSize: 0 // 0: normal, 1: large, 2: xlarge
    };

    // Load from LocalStorage
    const savedState = localStorage.getItem('gls_a11y_state');
    if (savedState) {
        try {
            a11yState = JSON.parse(savedState);
            applyState();
        } catch(e) {}
    }

    function saveState() {
        localStorage.setItem('gls_a11y_state', JSON.stringify(a11yState));
    }

    // Toggle Panel
    const togglePanel = () => {
        const isOpen = panel.classList.contains('open');
        if (isOpen) {
            panel.classList.remove('open');
            widgetBtn.setAttribute('aria-expanded', 'false');
        } else {
            panel.classList.add('open');
            widgetBtn.setAttribute('aria-expanded', 'true');
        }
    };

    widgetBtn.addEventListener('click', togglePanel);
    closeBtn.addEventListener('click', togglePanel);

    // Applying Classes and updating buttons
    function applyState() {
        const bd = document.body;
        const hl = document.documentElement;

        // Contrast
        if(a11yState.contrast) { bd.classList.add('a11y-high-contrast'); tglContrast.classList.add('active'); tglContrast.setAttribute('aria-pressed', 'true'); }
        else { bd.classList.remove('a11y-high-contrast'); tglContrast.classList.remove('active'); tglContrast.setAttribute('aria-pressed', 'false'); }

        // Links
        if(a11yState.links) { bd.classList.add('a11y-highlight-links'); tglLinks.classList.add('active'); tglLinks.setAttribute('aria-pressed', 'true'); }
        else { bd.classList.remove('a11y-highlight-links'); tglLinks.classList.remove('active'); tglLinks.setAttribute('aria-pressed', 'false'); }

        // Font
        if(a11yState.font) { bd.classList.add('a11y-readable-font'); tglFont.classList.add('active'); tglFont.setAttribute('aria-pressed', 'true'); }
        else { bd.classList.remove('a11y-readable-font'); tglFont.classList.remove('active'); tglFont.setAttribute('aria-pressed', 'false'); }

        // Motion
        if(a11yState.motion) { bd.classList.add('a11y-reduced-motion'); tglMotion.classList.add('active'); tglMotion.setAttribute('aria-pressed', 'true'); }
        else { bd.classList.remove('a11y-reduced-motion'); tglMotion.classList.remove('active'); tglMotion.setAttribute('aria-pressed', 'false'); }

        // Text Size
        hl.classList.remove('a11y-text-large', 'a11y-text-xlarge');
        btnIncrease.classList.remove('active');
        btnDecrease.classList.remove('active');
        btnReset.classList.remove('active');
        
        if (a11yState.textSize === 1) { hl.classList.add('a11y-text-large'); btnIncrease.classList.add('active'); }
        else if (a11yState.textSize === 2) { hl.classList.add('a11y-text-xlarge'); btnIncrease.classList.add('active'); } // Reuse active or style specifically
        else if (a11yState.textSize === -1) { /* Assuming decrease reduces size if we implement it, but for standard a11y we just reset */ }
        else { btnReset.classList.add('active'); }
    }

    // Listeners
    tglContrast.addEventListener('click', () => { a11yState.contrast = !a11yState.contrast; applyState(); saveState(); });
    tglLinks.addEventListener('click', () => { a11yState.links = !a11yState.links; applyState(); saveState(); });
    tglFont.addEventListener('click', () => { a11yState.font = !a11yState.font; applyState(); saveState(); });
    tglMotion.addEventListener('click', () => { a11yState.motion = !a11yState.motion; applyState(); saveState(); });

    btnIncrease.addEventListener('click', () => {
        if(a11yState.textSize < 2) a11yState.textSize++;
        applyState(); saveState();
    });
    btnDecrease.addEventListener('click', () => {
        if(a11yState.textSize > 0) a11yState.textSize--;
        applyState(); saveState();
    });
    btnReset.addEventListener('click', () => {
        a11yState.textSize = 0;
        applyState(); saveState();
    });
    btnResetAll.addEventListener('click', () => {
        a11yState = { contrast: false, links: false, font: false, motion: false, textSize: 0 };
        applyState(); saveState();
    });

});
"""

def main():
    css_file = os.path.join(DIR, 'styles.css')
    js_file = os.path.join(DIR, 'script.js')

    # Add to CSS if not present
    with open(css_file, 'r', encoding='utf-8') as f:
        curr_css = f.read()
    if 'a11y-high-contrast' not in curr_css:
        with open(css_file, 'a', encoding='utf-8') as f:
            f.write(CSS_A11Y)
        print("Updated styles.css")

    # Add to JS if not present
    with open(js_file, 'r', encoding='utf-8') as f:
        curr_js = f.read()
    if 'A11Y WIDGET INJECTION' not in curr_js:
        with open(js_file, 'a', encoding='utf-8') as f:
            f.write(JS_A11Y)
        print("Updated script.js")

    # Update HTML semantic tags
    html_files = glob.glob(os.path.join(DIR, '*.html'))
    for h_file in html_files:
        with open(h_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changed = False

        # 1. Menu button needs aria-label
        if '<button class="menu-btn" id="menu-btn">' in content:
            content = content.replace('<button class="menu-btn" id="menu-btn">', '<button class="menu-btn" id="menu-btn" aria-label="Toggle navigation menu" aria-expanded="false">')
            changed = True

        # Write back if changed
        if changed:
            with open(h_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Patched HTML semantics in {os.path.basename(h_file)}")

if __name__ == '__main__':
    main()
