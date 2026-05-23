import glob
import re
import os

emoji_to_fa = {
    '👔': '<i class="fa-solid fa-user-tie"></i>',
    '⚖': '<i class="fa-solid fa-scale-balanced"></i>',
    '⚖️': '<i class="fa-solid fa-scale-balanced"></i>',
    '🏛': '<i class="fa-solid fa-landmark"></i>',
    '🏛️': '<i class="fa-solid fa-landmark"></i>',
    '🤝': '<i class="fa-solid fa-handshake"></i>',
    '📄': '<i class="fa-solid fa-file-alt"></i>',
    '📈': '<i class="fa-solid fa-chart-line"></i>',
    '📊': '<i class="fa-solid fa-chart-column"></i>',
    '🏦': '<i class="fa-solid fa-building-columns"></i>',
    '🏢': '<i class="fa-solid fa-building"></i>',
    '📝': '<i class="fa-solid fa-file-signature"></i>',
    '🖋': '<i class="fa-solid fa-pen-nib"></i>',
    '🖋️': '<i class="fa-solid fa-pen-nib"></i>',
    '💡': '<i class="fa-solid fa-lightbulb"></i>',
    '📋': '<i class="fa-solid fa-clipboard-list"></i>',
    '🔍': '<i class="fa-solid fa-magnifying-glass"></i>',
    '📞': '<i class="fa-solid fa-phone"></i>',
    '🛡': '<i class="fa-solid fa-shield-halved"></i>',
    '🛡️': '<i class="fa-solid fa-shield-halved"></i>',
    '💬': '<i class="fa-solid fa-comment-dots"></i>',
    '😊': '<i class="fa-solid fa-face-smile"></i>',
    '📜': '<i class="fa-solid fa-scroll"></i>',
    '👨': '<i class="fa-solid fa-user"></i>',
    '👩': '<i class="fa-solid fa-user"></i>',
    '👧': '<i class="fa-solid fa-user"></i>',
    '🚓': '<i class="fa-solid fa-car-on"></i>',
    '👼': '<i class="fa-solid fa-child"></i>',
    '💼': '<i class="fa-solid fa-briefcase"></i>',
    '📩': '<i class="fa-solid fa-envelope-open-text"></i>',
    '🎒': '<i class="fa-solid fa-school"></i>',
    '📅': '<i class="fa-solid fa-calendar"></i>',
    '✍': '<i class="fa-solid fa-pen"></i>',
    '✍️': '<i class="fa-solid fa-pen"></i>',
    '🚀': '<i class="fa-solid fa-rocket"></i>',
    '🌙': '<i class="fa-solid fa-moon"></i>',
    '📡': '<i class="fa-solid fa-satellite-dish"></i>',
    '⚕': '<i class="fa-solid fa-staff-snake"></i>',
    '⚕️': '<i class="fa-solid fa-staff-snake"></i>',
    '⚙': '<i class="fa-solid fa-gear"></i>',
    '⚙️': '<i class="fa-solid fa-gear"></i>',
    '🌍': '<i class="fa-solid fa-earth-americas"></i>',
    '🏗': '<i class="fa-solid fa-building-user"></i>',
    '🏗️': '<i class="fa-solid fa-building-user"></i>',
    '🛍': '<i class="fa-solid fa-bag-shopping"></i>',
    '🛍️': '<i class="fa-solid fa-bag-shopping"></i>',
    '🔒': '<i class="fa-solid fa-lock"></i>',
    '🖨': '<i class="fa-solid fa-print"></i>',
    '🖨️': '<i class="fa-solid fa-print"></i>',
    '🏆': '<i class="fa-solid fa-trophy"></i>',
    '📍': '<i class="fa-solid fa-location-dot"></i>',
    '🧠': '<i class="fa-solid fa-brain"></i>',
    '💰': '<i class="fa-solid fa-money-bill-wave"></i>',
    '✓': '<i class="fa-solid fa-check"></i>',
    '⚡': '<i class="fa-solid fa-bolt"></i>',
    '📱': '<i class="fa-solid fa-mobile-screen"></i>',
    '🔐': '<i class="fa-solid fa-lock"></i>',
}

files_to_check = glob.glob('*.html') + glob.glob('*.js')

for f in files_to_check:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content
    # Order keys by length descending to match composed emojis like ⚖️ before ⚖
    keys = sorted(emoji_to_fa.keys(), key=len, reverse=True)
    for k in keys:
        if k in new_content:
            new_content = new_content.replace(k, emoji_to_fa[k])
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Replaced emojis in {f}")

print("Emoji replacement complete.")
