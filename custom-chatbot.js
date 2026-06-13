document.addEventListener('DOMContentLoaded', () => {
    // Inject HTML Structure
    const chatHTML = `
        <div id="gls-chat-widget-container">
            <div id="gls-chat-window">
                <div id="gls-chat-header">
                    <div id="gls-chat-header-info">
                        <img src="images/logo.png" alt="GLS Logo" onerror="this.src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png'">
                        <div>
                            <p id="gls-chat-header-title">Get Legal Solution AI</p>
                            <p id="gls-chat-header-status">Online</p>
                        </div>
                    </div>
                    <button id="gls-chat-close">✖</button>
                </div>
                <div id="gls-chat-messages">
                    <div class="gls-message bot">
                        <p>Hello! I am the Get Legal Solution AI Assistant. How can I help you with your legal needs today?</p>
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

    // Toggle Chat Window
    chatBtn.addEventListener('click', () => {
        chatWindow.classList.add('open');
        chatBtn.style.display = 'none';
        chatInput.focus();
    });

    closeBtn.addEventListener('click', () => {
        chatWindow.classList.remove('open');
        setTimeout(() => { chatBtn.style.display = 'flex'; }, 300);
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
        msgDiv.className = `gls-message ${sender}`;
        msgDiv.innerHTML = `<p>${formatText(text)}</p>`;
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
                body: JSON.stringify({ message: text })
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
});
