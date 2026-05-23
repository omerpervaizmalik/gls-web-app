/* 
   Tidio Chat Configuration - AGGRESSIVE MOVE
   Forces the Lyro/Tidio chatbot to the bottom-left corner
*/
(function() {
    function forceTidioLeft() {
        if (window.tidioChatApi) {
            try {
                window.tidioChatApi.setSide('left');
                // Also try to direct the widget specifically if possible
                if (window.tidioChatApi.on) {
                    window.tidioChatApi.on('ready', function() {
                        window.tidioChatApi.setSide('left');
                    });
                }
            } catch (e) {
                console.log('Tidio API not fully ready or restricted');
            }
        }
    }

    // Attempt moving every 500ms for 10 seconds to catch all lazy-loading cycles
    let attempts = 0;
    const interval = setInterval(() => {
        forceTidioLeft();
        attempts++;
        if (attempts > 20) clearInterval(interval);
    }, 500);

    // Also listen for the specific Tidio ready event
    document.addEventListener('tidioChat-ready', forceTidioLeft);
    
    // Fallback: If API fails, we rely on the aggressive CSS injected via styles.css
})();
