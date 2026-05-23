with open('d:/Anti gravity/get-legal-solution/styles.css', 'a', encoding='utf-8') as f:
    f.write("""

/* Law Directory Split-Layout */
.laws-container {
    display: flex;
    gap: 2rem;
    height: 80vh;
    margin-top: 2rem;
}

.laws-sidebar {
    flex: 0 0 320px;
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    padding: 1.5rem;
    overflow-y: auto;
    backdrop-filter: blur(10px);
}

.laws-content {
    flex: 1;
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    padding: 0;
    overflow-y: auto;
    backdrop-filter: blur(10px);
    display: flex;
    flex-direction: column;
}

.laws-sidebar::-webkit-scrollbar,
.laws-content::-webkit-scrollbar {
    width: 6px;
}

.laws-sidebar::-webkit-scrollbar-thumb,
.laws-content::-webkit-scrollbar-thumb {
    background: var(--gold-dim);
    border-radius: 10px;
}

.sidebar-category {
    margin-bottom: 2rem;
}

.sidebar-category-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    font-family: 'Cinzel', serif;
    color: var(--gold-primary);
    font-size: 0.9rem;
    border-bottom: 1px solid var(--glass-border);
    padding-bottom: 8px;
    margin-bottom: 1rem;
}

.sidebar-category-header.active .chevron {
    transform: rotate(180deg);
}

.sidebar-law-list {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.sidebar-law-list.collapsed {
    display: none;
}

.sidebar-law-item {
    padding: 10px 15px;
    border-radius: 6px;
    font-size: 0.85rem;
    color: var(--text-light);
    cursor: pointer;
    transition: all 0.2s;
    border: 1px solid transparent;
}

.sidebar-law-item:hover {
    background: var(--gold-dim);
    color: var(--gold-primary);
}

.sidebar-law-item.active {
    background: var(--gold-primary);
    color: var(--bg-darker);
    font-weight: 700;
}

.viewer-header {
    background: rgba(10, 10, 10, 0.8);
    padding: 1.5rem 2.5rem;
    border-bottom: 2px solid var(--gold-primary);
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 10;
    backdrop-filter: blur(15px);
}

.viewer-header h2 {
    font-family: 'Cinzel', serif;
    color: var(--gold-primary);
    font-size: 1.4rem;
    margin: 0;
}

.viewer-body {
    padding: 3rem;
    flex: 1;
}

.viewer-badge {
    display: inline-block;
    padding: 5px 12px;
    background: var(--gold-primary);
    color: #000;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 800;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}

.viewer-desc {
    font-size: 1.2rem;
    line-height: 1.8;
    color: var(--text-white);
    font-family: 'Inter', sans-serif;
    font-weight: 300;
    white-space: pre-wrap;
}

@media (max-width: 1024px) {
    .laws-container {
        flex-direction: column;
        height: auto;
    }
    .laws-sidebar {
        flex: none;
        max-height: 350px;
    }
    .laws-content {
        height: 600px;
    }
}
""")
