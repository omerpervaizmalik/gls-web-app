/**
 * GL Assistant - Smart Legal Search Chatbot
 * This script uses contentDB and lawsDB to answer client questions.
 */

const GLAssistant = {
    isOpen: false,
    chatHistory: [],
    
    // Expanded Knowledge Base for "Beyond Website Info"
    legalLibrary: {
        "domicile": "A Domicile certificate is a document that proves a person is a resident of a specific city or province in Pakistan. It is required for government jobs, admissions in educational institutions, and various other official purposes.",
        "succession certificate": "A Succession Certificate is issued by a civil court (or NADRA in some cases) to the legal heirs of a deceased person to establish their right to inheritance, bank accounts, and other movable assets.",
        "inheritance": "Inheritance laws in Pakistan are generally governed by the personal law of the deceased (e.g., Muslim Personal Law, Christian/Hindu laws). For Muslims, the distribution is based on the Quranic shares and the legal heirs' proximity to the deceased.",
        "will": "A Will (Wasiyat) in Pakistan allows a person to bequeath up to 1/3rd of their property to a non-heir. The remaining 2/3rds must be distributed according to the law of inheritance.",
        "power of attorney": "A Power of Attorney (PoA) is a legal document giving one person the authority to act for another. For property matters (Special PoA), it must be registered with the Sub-Registrar.",
        "nikahnama": "The Nikahnama is an official contract of marriage in Pakistan. It outlines the rights and duties of both spouses, including the Haq Mehr (Dower money).",
        "divorce": "Divorce in Pakistan (Khula or Talaq) is governed by the Muslim Family Laws Ordinance, 1961. It must be registered with the local Union Council to be legally final.",
        "fbr": "The Federal Board of Revenue (FBR) is the official body in Pakistan responsible for tax collection and administration. You can check your ATL status at iris.fbr.gov.pk.",
        "secp": "The Securities and Exchange Commission of Pakistan (SECP) is the regulator for companies, insurers, and the stock market.",
        "nadra": "The National Database and Registration Authority (NADRA) issues CNICs, Family Registration Certificates (FRC), and Succession Certificates."
    },

    init() {
        this.injectHTML();
        this.bindEvents();
        this.addWelcomeMessage();
    },

    injectHTML() {
        const html = `
            <div class="gl-assistant-bubble" id="assistant-bubble">
                <i class="fa-solid fa-headset"></i>
                <div class="gl-assistant-badge">AI</div>
            </div>
            
            <div class="gl-chat-window" id="chat-window">
                <div class="gl-chat-header">
                    <div class="avatar"><i class="fa-solid fa-scale-balanced"></i></div>
                    <div class="gl-chat-header-info">
                        <h4>GLS Assistant</h4>
                        <span>Online | Site Knowledge Base</span>
                    </div>
                    <div class="gl-chat-close" id="chat-close">
                        <i class="fa-solid fa-xmark"></i>
                    </div>
                </div>
                
                <div class="gl-chat-body" id="chat-body"></div>
                
                <div class="gl-chat-input-area">
                    <input type="text" class="gl-chat-input" id="chat-input" placeholder="Ask about services, laws, or requirements...">
                    <button class="gl-chat-send" id="chat-send">
                        <i class="fa-solid fa-paper-plane"></i>
                    </button>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', html);
    },

    bindEvents() {
        const bubble = document.getElementById('assistant-bubble');
        const close = document.getElementById('chat-close');
        const input = document.getElementById('chat-input');
        const send = document.getElementById('chat-send');

        bubble.addEventListener('click', () => this.toggleChat());
        close.addEventListener('click', () => this.toggleChat());
        
        send.addEventListener('click', () => this.handleUserInput());
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.handleUserInput();
        });
    },

    toggleChat() {
        this.isOpen = !this.isOpen;
        document.getElementById('chat-window').classList.toggle('active', this.isOpen);
    },

    addMessage(text, sender = 'bot') {
        const body = document.getElementById('chat-body');
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${sender}`;
        msgDiv.innerHTML = text;
        body.appendChild(msgDiv);
        body.scrollTop = body.scrollHeight;
    },

    addWelcomeMessage() {
        this.addMessage("Hello! I am your <b>Smart Legal Assistant</b>. I can help you with questions about company registration, taxation, legal requirements, and Pakistani laws. What would you like to know today?");
        this.showSuggestions([
            "Company Registration",
            "Tax Filing",
            "Trademarks",
            "Relevant Laws"
        ]);
    },

    showSuggestions(suggestions) {
        const body = document.getElementById('chat-body');
        const sugDiv = document.createElement('div');
        sugDiv.className = 'gl-chat-suggestions';
        
        suggestions.forEach(s => {
            const chip = document.createElement('div');
            chip.className = 'suggestion-chip';
            chip.textContent = s;
            chip.onclick = () => {
                document.getElementById('chat-input').value = s;
                this.handleUserInput();
            };
            sugDiv.appendChild(chip);
        });
        
        body.appendChild(sugDiv);
        body.scrollTop = body.scrollHeight;
    },

    handleUserInput() {
        const input = document.getElementById('chat-input');
        const query = input.value.trim();
        if (!query) return;

        this.addMessage(query, 'user');
        input.value = '';

        setTimeout(() => {
            const response = this.searchKnowledgeBase(query);
            this.addMessage(response);
        }, 600);
    },

    searchKnowledgeBase(query) {
        const q = query.toLowerCase();
        let bestMatch = null;
        let highestScore = 0;

        // Special Case: List all uploaded laws
        if (q.includes('list') && q.includes('law') || q.includes('all laws') || q.includes('uploaded laws')) {
            if (typeof lawsDB !== 'undefined') {
                let lawList = "Our library currently includes the following statutory laws:<br><br><ul>";
                Object.values(lawsDB).flat().forEach(law => {
                    lawList += `<li><b>${law.title}</b></li>`;
                });
                lawList += "</ul><br>You can read the full text of any of these in our <a href='relevant-laws.html'>Relevant Laws</a> portal.";
                return `<b>Assistant Response:</b><br><br>${lawList}<br><br>Need a specific section? Ask me about the law's content!`;
            }
        }

        // Search Documentary Requirements (New)
        if (typeof requirementsDB !== 'undefined') {
            for (let title in requirementsDB) {
                const score = this.calculateScore(q, title, title);
                if (score > highestScore) {
                    const items = requirementsDB[title].map(item => `<li>${item}</li>`).join('');
                    highestScore = score * 1.5; // Weight requirements highly
                    bestMatch = { 
                        text: `The documentary requirements for <b>${title}</b> are:<br><br><ul>${items}</ul>`, 
                        source: "Documentary Requirements Portal" 
                    };
                }
            }
        }

        // Search ContentDB
        if (typeof contentDB !== 'undefined') {
            for (let section in contentDB) {
                for (let key in contentDB[section]) {
                    const content = contentDB[section][key];
                    if (typeof content === 'string') {
                        const score = this.calculateScore(q, content, key);
                        if (score > highestScore) {
                            highestScore = score;
                            bestMatch = { text: content, source: key };
                        }
                    } else if (typeof content === 'object') {
                        // Nested search
                        for (let subKey in content) {
                            const subContent = content[subKey];
                            const score = this.calculateScore(q, subContent, subKey);
                            if (score > highestScore) {
                                highestScore = score;
                                bestMatch = { text: subContent, source: subKey };
                            }
                        }
                    }
                }
            }
        }

        // Search LawsDB
        if (typeof lawsDB !== 'undefined') {
            Object.values(lawsDB).flat().forEach(law => {
                const lawInfo = `${law.title} ${law.features.join(' ')}`;
                const score = this.calculateScore(q, lawInfo, law.title);
                if (score > highestScore) {
                    highestScore = score;
                    bestMatch = { 
                        text: `<b>${law.title}</b> covers: ${law.features.join(', ')}. <br><br>You can find the full text in our <a href="relevant-laws.html">Statutory Laws Portal</a>.`,
                        source: law.title 
                    };
                }
            });
        }

        // Search Expanded Legal Library (Beyond Website Info)
        for (let topic in this.legalLibrary) {
            if (q.includes(topic)) {
                highestScore = 2; // High priority for direct topics
                bestMatch = { text: this.legalLibrary[topic], source: "General Legal Knowledge" };
                break;
            }
        }

        if (highestScore > 0.05) {
            let responseText = bestMatch.text;
            return `<b>Assistant Response:</b><br><br>${responseText}<br><br><i>Source: ${bestMatch.source || 'Firm Database'}</i><br><br>Need more details? Connect with <b>Omer Pervaiz Malik</b> on <a href="https://wa.me/923014991700" target="_blank">WhatsApp</a>.`;
        }

        return "I couldn't find a specific answer in our database. However, I can still help!<br><br>I have access to the full text of <b>Income Tax</b>, <b>Sales Tax</b>, <b>CPC</b>, <b>CrPC</b>, <b>PPC</b>, <b>Police Order</b>, and <b>Qanun-e-Shahadat</b>. You can also search for official gazettes on the <b><a href='http://www.pakistan.gov.pk/' target='_blank'>Government of Pakistan Portal</a></b> or speak directly with <b>Omer Pervaiz Malik</b> on <a href='https://wa.me/923014991700' target='_blank'>WhatsApp (0301-4991700)</a> for expert counsel.";
    },

    calculateScore(query, text, key) {
        let score = 0;
        const words = query.split(/\W+/).filter(w => w.length > 2);
        const lowerText = text.toLowerCase();
        const lowerKey = key.toLowerCase();

        words.forEach(word => {
            if (lowerKey.includes(word)) score += 0.5;
            if (lowerText.includes(word)) score += 0.1;
            
            // Exact phrase match bonus
            if (lowerText.includes(query)) score += 1;
        });

        return score;
    }
};

// Start Assistant
document.addEventListener('DOMContentLoaded', () => {
    // Wait a bit to ensure databases are loaded
    setTimeout(() => {
        GLAssistant.init();
    }, 1000);
});
