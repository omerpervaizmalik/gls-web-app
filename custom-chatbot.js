function initChatbot() {
    // Inject HTML Structure
    const chatHTML = `
        <div id="gls-chat-widget-container">
            <div id="gls-chat-window">
                <div id="gls-chat-header">
                    <div id="gls-chat-header-info">
                        <img src="logo.png" alt="GLS Logo" onerror="this.src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png'">
                        <div class="gls-header-text">
                            <p id="gls-chat-header-title">Support Assistant</p>
                            <p id="gls-chat-header-status">Online now</p>
                        </div>
                    </div>
                    <button id="gls-chat-close">✖</button>
                </div>
                
                <div id="gls-views-container">
                    
                    <!-- HOME VIEW -->
                    <div id="gls-home-view" class="gls-view">
                        <h2 class="gls-welcome-title">Welcome to AI Support Agent</h2>
                        <h3 class="gls-welcome-title" style="font-size:22px; margin-bottom:16px;">How can we help you today?</h3>
                        <p class="gls-welcome-subtitle">We'll answer any questions or queries related to Support Assistant within seconds. Start chatting now.</p>
                        
                        <div class="gls-main-action-btn" id="gls-start-chat-btn">
                            <div class="gls-main-action-icon">✨</div>
                            <div class="gls-main-action-text">
                                <h4>What's on your mind?</h4>
                                <p>Talk to Support Assistant</p>
                            </div>
                            <div class="gls-main-action-arrow">↗</div>
                        </div>

                        <p class="gls-quick-paths-title">QUICK PATHS</p>
                        <button class="gls-quick-path" data-query="I have a question">I have a question <span class="arrow">↗</span></button>
                        <button class="gls-quick-path" data-query="I'd like a quote">I'd like a quote <span class="arrow">↗</span></button>
                        <button class="gls-quick-path" data-query="Tell me about your services">Tell me about your services <span class="arrow">↗</span></button>
                        <button class="gls-quick-path" data-query="I need to talk to a human expert">Something else <span class="arrow">↗</span></button>
                    </div>

                    <!-- LEAD CAPTURE VIEW -->
                    <div id="gls-lead-view" class="gls-view">
                        <h2 class="gls-form-title">Before we start...</h2>
                        <p class="gls-form-desc">Please provide your details so our human experts can follow up if needed.</p>
                        
                        <div class="gls-input-group">
                            <label>Full Name</label>
                            <input type="text" id="gls-lead-name" class="gls-input" placeholder="John Doe">
                        </div>
                        <div class="gls-input-group">
                            <label>WhatsApp Number</label>
                            <input type="tel" id="gls-lead-phone" class="gls-input" placeholder="+92 300 1234567">
                        </div>
                        <button id="gls-submit-lead-btn" class="gls-submit-btn">Start Chat</button>
                    </div>

                    <!-- CHAT VIEW -->
                    <div id="gls-chat-view" class="gls-view">
                        <div id="gls-chat-messages">
                            <div class="gls-message bot">
                                <p>Hello! I am the Get Legal Solution AI Assistant. How can I help you today?</p>
                            </div>
                        </div>
                        <div id="gls-chat-input-area">
                            <input type="text" id="gls-chat-input" placeholder="Type your message..." autocomplete="off">
                            <button id="gls-chat-send">
                                <svg viewBox="0 0 24 24">
                                    <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"></path>
                                </svg>
                            </button>
                        </div>
                    </div>

                </div>

                <!-- BOTTOM NAV -->
                <div id="gls-bottom-nav">
                    <button class="gls-nav-btn active" id="gls-nav-home">
                        <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
                        Home
                    </button>
                    <button class="gls-nav-btn" id="gls-nav-messages">
                        <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z"/></svg>
                        Messages
                    </button>
                    <button class="gls-nav-btn" id="gls-nav-help">
                        <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"/></svg>
                        Help
                    </button>
                </div>
                <div class="gls-powered-by">Powered by <span>Get Legal Solution</span></div>

            </div>
            <button id="gls-chat-button">
                <svg viewBox="0 0 24 24">
                    <path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"></path>
                </svg>
            </button>
        </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', chatHTML);

    const chatBtn = document.getElementById('gls-chat-button');
    const chatWindow = document.getElementById('gls-chat-window');
    const closeBtn = document.getElementById('gls-chat-close');
    const sendBtn = document.getElementById('gls-chat-send');
    const chatInput = document.getElementById('gls-chat-input');
    const messagesContainer = document.getElementById('gls-chat-messages');

    // Views
    const homeView = document.getElementById('gls-home-view');
    const leadView = document.getElementById('gls-lead-view');
    const chatView = document.getElementById('gls-chat-view');

    // Nav Buttons
    const navHome = document.getElementById('gls-nav-home');
    const navMessages = document.getElementById('gls-nav-messages');

    // State
    let userDetails = null; // { name, phone }
    let pendingQuery = null;
    let sessionId = 'chat-' + Math.random().toString(36).substr(2, 9);

    // View Management
    function showView(viewId) {
        homeView.classList.remove('hidden', 'active');
        leadView.classList.remove('hidden', 'active');
        chatView.classList.remove('hidden', 'active');
        
        navHome.classList.remove('active');
        navMessages.classList.remove('active');

        if (viewId === 'home') {
            homeView.classList.add('active');
            navHome.classList.add('active');
        } else if (viewId === 'lead') {
            homeView.classList.add('hidden'); // slide left
            leadView.classList.add('active');
            navMessages.classList.add('active');
        } else if (viewId === 'chat') {
            homeView.classList.add('hidden');
            leadView.classList.add('hidden');
            chatView.classList.add('active');
            navMessages.classList.add('active');
        }
    }

    // Toggle Chat Window
    chatBtn.addEventListener('click', () => {
        chatWindow.classList.add('open');
        chatBtn.style.display = 'none';
        if (userDetails) {
            showView('chat');
        } else {
            showView('home');
        }
    });

    closeBtn.addEventListener('click', () => {
        chatWindow.classList.remove('open');
        setTimeout(() => { chatBtn.style.display = 'flex'; }, 300);
    });

    navHome.addEventListener('click', () => showView('home'));
    navMessages.addEventListener('click', () => {
        if (userDetails) showView('chat');
        else showView('lead');
    });

    // Start Chat / Quick Paths
    document.getElementById('gls-start-chat-btn').addEventListener('click', () => {
        showView('lead');
    });

    document.querySelectorAll('.gls-quick-path').forEach(btn => {
        btn.addEventListener('click', (e) => {
            pendingQuery = e.currentTarget.getAttribute('data-query');
            showView('lead');
        });
    });

    // Submit Lead Form
    document.getElementById('gls-submit-lead-btn').addEventListener('click', () => {
        const name = document.getElementById('gls-lead-name').value.trim();
        const phone = document.getElementById('gls-lead-phone').value.trim();
        
        if (!name || !phone) {
            alert("Please enter both your name and phone number.");
            return;
        }
        
        userDetails = { name, phone };
        showView('chat');

        if (pendingQuery) {
            chatInput.value = pendingQuery;
            sendMessage();
            pendingQuery = null;
        }
    });

    // Helper: format basic markdown (bold, newlines)
    function formatText(text) {
        return text
            .replace(/\\n/g, '<br>')
            .replace(/\n/g, '<br>')
            .replace(/\*(.*?)\*/g, '<strong>$1</strong>');
    }

    function appendMessage(text, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'gls-message ' + sender;
        msgDiv.innerHTML = '<p>' + formatText(text) + '</p>';
        messagesContainer.appendChild(msgDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function showTyping() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'gls-typing-indicator';
        typingDiv.id = 'gls-typing';
        typingDiv.innerHTML = '<div class="gls-typing-dot"></div><div class="gls-typing-dot"></div><div class="gls-typing-dot"></div>';
        messagesContainer.appendChild(typingDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function removeTyping() {
        const typingDiv = document.getElementById('gls-typing');
        if (typingDiv) typingDiv.remove();
    }

    async function sendMessage() {
        const text = chatInput.value.trim();
        if (!text) return;

        appendMessage(text, 'user');
        chatInput.value = '';
        showTyping();

        try {
            // Call Vercel Backend
            const response = await fetch('https://gls-rag-module.vercel.app/api/webchat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 
                    message: text,
                    sessionId: sessionId,
                    user: userDetails
                })
            });

            const data = await response.json();
            removeTyping();

            if (response.ok && data.response) {
                appendMessage(data.response, 'bot');
            } else {
                appendMessage("Sorry, I am having trouble connecting to my database right now. Please try again later.", 'bot');
            }
        } catch (error) {
            console.error("Chat Error:", error);
            removeTyping();
            appendMessage("An error occurred while connecting. Please check your internet connection.", 'bot');
        }
    }

    sendBtn.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChatbot);
} else {
    initChatbot();
}
