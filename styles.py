"""
Styles and CSS Theme for CISOPOLIS SP Cyber Command Center
Matches the high-end dark cybersecurity GRC & Intelligence platform aesthetic.
"""

def get_cyber_theme_css() -> str:
    return """
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* Global Root Variables */
    :root {
        --bg-main: #070b14;
        --bg-surface: #0c1427;
        --bg-surface-elevated: #111b33;
        --bg-sidebar: #060912;
        --border-subtle: rgba(255, 255, 255, 0.07);
        --border-glow: rgba(56, 189, 248, 0.25);
        --accent-cyan: #00f0ff;
        --accent-sky: #38bdf8;
        --accent-purple: #8b5cf6;
        --accent-indigo: #6366f1;
        --accent-green: #10b981;
        --accent-red: #ef4444;
        --accent-amber: #f59e0b;
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --text-muted: #64748b;
    }

    /* Core Streamlit Overrides */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--bg-main) !important;
        color: var(--text-primary) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    [data-testid="stHeader"] {
        background-color: rgba(7, 11, 20, 0.8) !important;
        backdrop-filter: blur(12px) !important;
        border-bottom: 1px solid var(--border-subtle) !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: var(--bg-sidebar) !important;
        border-right: 1px solid var(--border-subtle) !important;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: var(--text-secondary);
        font-size: 0.85rem;
    }

    /* Remove Streamlit default top padding */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
    }

    /* Custom Scrollbars */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    ::-webkit-scrollbar-track {
        background: var(--bg-main);
    }
    ::-webkit-scrollbar-thumb {
        background: #1e293b;
        border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: var(--accent-sky);
    }

    /* Streamlit Containers & Cards */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: var(--bg-surface) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: 14px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4) !important;
        transition: border-color 0.2s ease, transform 0.2s ease;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(56, 189, 248, 0.22) !important;
    }

    /* Buttons */
    .stButton>button {
        background: #111b33 !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 20px !important;
        padding: 0.45rem 1.25rem !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        transition: all 0.2s ease !important;
    }
    .stButton>button:hover {
        border-color: var(--accent-cyan) !important;
        color: #ffffff !important;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.25) !important;
        transform: translateY(-1px);
    }
    .stButton>button[kind="primary"], .stButton>button:focus {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #06b6d4 100%) !important;
        border: none !important;
        color: #ffffff !important;
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.4) !important;
    }

    /* Download Buttons */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #0284c7 0%, #06b6d4 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 20px !important;
        font-weight: 600 !important;
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.35) !important;
    }

    /* Section headers in sidebar */
    .sidebar-section-header {
        font-size: 0.72rem !important;
        font-weight: 700 !important;
        letter-spacing: 1.2px !important;
        text-transform: uppercase !important;
        color: #64748b !important;
        margin: 1.1rem 0 0.4rem 0.6rem !important;
        display: flex !important;
        align-items: center !important;
        gap: 0.4rem !important;
    }
    .sidebar-section-header::before {
        content: "•";
        color: #38bdf8;
        font-size: 1rem;
    }

    /* Full-width sidebar button navigation */
    [data-testid="stSidebar"] .stButton>button {
        width: 100% !important;
        text-align: left !important;
        justify-content: flex-start !important;
        background: transparent !important;
        border: 1px solid transparent !important;
        border-radius: 8px !important;
        color: #94a3b8 !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        padding: 0.45rem 0.85rem !important;
        margin-bottom: 2px !important;
        box-shadow: none !important;
    }
    [data-testid="stSidebar"] .stButton>button:hover {
        background: rgba(255, 255, 255, 0.05) !important;
        color: #f8fafc !important;
        border-color: rgba(255, 255, 255, 0.08) !important;
        transform: none !important;
    }
    [data-testid="stSidebar"] .stButton>button[kind="primary"] {
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 45%, #06b6d4 100%) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        box-shadow: 0 0 16px rgba(124, 58, 237, 0.45) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
    }

    /* Inputs, Selectboxes & Text areas */
    .stTextInput input, .stSelectbox [data-baseweb="select"] {
        background-color: #0b1326 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        color: #f1f5f9 !important;
    }
    .stTextInput input:focus, .stSelectbox [data-baseweb="select"]:focus-within {
        border-color: var(--accent-cyan) !important;
        box-shadow: 0 0 12px rgba(0, 240, 255, 0.3) !important;
    }

    /* Code blocks */
    code, pre {
        background-color: #080e1c !important;
        color: #38bdf8 !important;
        font-family: 'JetBrains Mono', monospace !important;
        border: 1px solid rgba(56, 189, 248, 0.2) !important;
        border-radius: 8px !important;
    }

    /* File Uploader */
    [data-testid="stFileUploader"] section {
        background-color: #091020 !important;
        border: 1px dashed rgba(56, 189, 248, 0.3) !important;
        border-radius: 12px !important;
    }

    /* Metrics */
    [data-testid="stMetricValue"] {
        font-family: 'Inter', sans-serif !important;
        font-weight: 800 !important;
        color: #ffffff !important;
    }
    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        font-size: 0.85rem !important;
    }

    /* ====================================================================
       CUSTOM PLATFORM HTML COMPONENTS
       ==================================================================== */

    .cyber-top-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.6rem 1.2rem;
        background: rgba(11, 19, 39, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        margin-bottom: 1.25rem;
        backdrop-filter: blur(10px);
    }
    .top-bar-left {
        display: flex;
        align-items: center;
        gap: 1.2rem;
    }
    .top-bar-logo {
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }
    .top-bar-logo-icon {
        width: 28px;
        height: 28px;
        background: linear-gradient(135deg, #00f0ff, #3b82f6);
        border-radius: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #050b18;
        font-weight: 800;
        font-size: 16px;
        box-shadow: 0 0 12px rgba(0, 240, 255, 0.4);
    }
    .top-bar-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: -0.3px;
    }
    .top-bar-subtitle {
        font-size: 0.75rem;
        color: var(--accent-sky);
        font-weight: 500;
    }
    .top-bar-search {
        display: flex;
        align-items: center;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 0.35rem 1rem;
        width: 380px;
        color: #cbd5e1;
        font-size: 0.82rem;
    }
    .top-bar-right {
        display: flex;
        align-items: center;
        gap: 1rem;
        font-size: 0.82rem;
        color: #94a3b8;
    }
    .user-pill {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(139, 92, 246, 0.12);
        border: 1px solid rgba(139, 92, 246, 0.25);
        border-radius: 20px;
        padding: 0.25rem 0.75rem;
        color: #ddd6fe;
        font-size: 0.82rem;
    }
    .user-avatar {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: #8b5cf6;
        color: white;
        font-size: 11px;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .ask-polis-btn {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: #ffffff;
        padding: 0.35rem 0.95rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.8rem;
        box-shadow: 0 0 14px rgba(168, 85, 247, 0.4);
        display: flex;
        align-items: center;
        gap: 0.4rem;
        text-decoration: none;
    }

    /* Hero Banner Card */
    .cyber-hero {
        background: linear-gradient(135deg, #0b1328 0%, #070e1e 100%);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 16px;
        padding: 1.75rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        position: relative;
        overflow: hidden;
    }
    .cyber-hero::before {
        content: '';
        position: absolute;
        top: -60px;
        left: -60px;
        width: 220px;
        height: 220px;
        background: radial-gradient(circle, rgba(0, 240, 255, 0.12) 0%, transparent 70%);
        pointer-events: none;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(0, 240, 255, 0.1);
        border: 1px solid rgba(0, 240, 255, 0.35);
        color: #00f0ff;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        margin-bottom: 0.85rem;
    }
    .hero-logo-row {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.5rem;
    }
    .hero-logo-box {
        width: 44px;
        height: 44px;
        background: linear-gradient(135deg, #06b6d4, #3b82f6);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: 900;
        color: #050b18;
        box-shadow: 0 0 20px rgba(6, 182, 212, 0.45);
    }
    .hero-brand-name {
        font-size: 1.6rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: 0.5px;
    }
    .hero-brand-name span {
        color: #00f0ff;
        font-weight: 600;
    }
    .hero-brand-tag {
        font-size: 0.75rem;
        font-weight: 600;
        color: #94a3b8;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    .hero-title {
        font-size: 1.85rem;
        font-weight: 800;
        color: #ffffff;
        margin: 1rem 0 0.5rem 0;
        line-height: 1.25;
        letter-spacing: -0.5px;
    }
    .hero-desc {
        font-size: 0.92rem;
        color: #94a3b8;
        max-width: 680px;
        line-height: 1.55;
        margin-bottom: 1.25rem;
    }
    .hero-actions {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-bottom: 1.25rem;
    }
    .hero-btn {
        background: #111a33;
        border: 1px solid rgba(255, 255, 255, 0.12);
        color: #e2e8f0;
        font-size: 0.82rem;
        font-weight: 600;
        padding: 0.45rem 1rem;
        border-radius: 20px;
        cursor: pointer;
        transition: all 0.2s ease;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
    }
    .hero-btn:hover {
        border-color: var(--accent-cyan);
        color: #ffffff;
        box-shadow: 0 0 14px rgba(0, 240, 255, 0.25);
    }
    .hero-btn.primary {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #06b6d4 100%);
        border: none;
        color: #ffffff;
        box-shadow: 0 0 18px rgba(99, 102, 241, 0.4);
    }

    /* Copilot Shortcut Box inside Hero */
    .copilot-shortcut {
        background: rgba(14, 23, 48, 0.8);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 12px;
        padding: 1rem;
        max-width: 340px;
        margin-left: auto;
    }
    .copilot-shortcut-title {
        font-size: 0.85rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.35rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }
    .copilot-shortcut-text {
        font-size: 0.78rem;
        color: #94a3b8;
        line-height: 1.4;
        margin-bottom: 0.75rem;
    }

    /* Security Posture Card */
    .posture-card {
        background: #0b1328;
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 14px;
        padding: 1.25rem;
        margin-bottom: 1rem;
    }
    .posture-title {
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        color: #38bdf8;
        margin-bottom: 0.5rem;
    }
    .posture-score {
        font-size: 2.8rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1;
        margin-bottom: 0.6rem;
    }
    .posture-bar-bg {
        width: 100%;
        height: 8px;
        background: #172544;
        border-radius: 4px;
        overflow: hidden;
        margin-bottom: 0.6rem;
    }
    .posture-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #0284c7 0%, #00f0ff 100%);
        border-radius: 4px;
        box-shadow: 0 0 12px rgba(0, 240, 255, 0.6);
    }
    .posture-sub {
        font-size: 0.74rem;
        color: #64748b;
        line-height: 1.4;
    }

    /* Radar Container */
    .radar-card {
        background: #0b1328;
        border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 14px;
        padding: 1.25rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 1rem;
        position: relative;
    }
    .radar-screen {
        width: 190px;
        height: 190px;
        border-radius: 50%;
        background: radial-gradient(circle, #051a14 0%, #030d0a 100%);
        border: 2px solid rgba(16, 185, 129, 0.35);
        box-shadow: 0 0 25px rgba(16, 185, 129, 0.15), inset 0 0 20px rgba(16, 185, 129, 0.1);
        position: relative;
        overflow: hidden;
        margin-bottom: 0.75rem;
    }
    /* Radar rings */
    .radar-ring {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 50%;
        pointer-events: none;
    }
    .radar-ring-1 { width: 33%; height: 33%; }
    .radar-ring-2 { width: 66%; height: 66%; }
    .radar-ring-3 { width: 95%; height: 95%; }

    /* Radar crosshairs */
    .radar-crosshair-h {
        position: absolute;
        top: 50%;
        left: 0;
        width: 100%;
        height: 1px;
        background: rgba(16, 185, 129, 0.2);
    }
    .radar-crosshair-v {
        position: absolute;
        top: 0;
        left: 50%;
        width: 1px;
        height: 100%;
        background: rgba(16, 185, 129, 0.2);
    }

    /* Radar rotating sweep */
    .radar-sweep {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: conic-gradient(from 0deg, rgba(16, 185, 129, 0.45) 0deg, rgba(16, 185, 129, 0.08) 45deg, transparent 60deg);
        animation: radar-sweep-anim 4s linear infinite;
        pointer-events: none;
    }
    @keyframes radar-sweep-anim {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    /* Blips */
    .blip {
        position: absolute;
        width: 9px;
        height: 9px;
        border-radius: 50%;
    }
    .blip-red {
        top: 28%;
        right: 25%;
        background: #ef4444;
        box-shadow: 0 0 10px #ef4444;
        animation: blip-pulse-red 2s infinite ease-in-out;
    }
    .blip-green-1 {
        bottom: 35%;
        left: 30%;
        background: #22c55e;
        box-shadow: 0 0 10px #22c55e;
        animation: blip-pulse-green 2.5s infinite ease-in-out;
    }
    .blip-green-2 {
        bottom: 25%;
        right: 25%;
        background: #84cc16;
        box-shadow: 0 0 14px #84cc16;
        animation: blip-pulse-green 3s infinite ease-in-out;
    }
    @keyframes blip-pulse-red {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.6); opacity: 0.6; }
    }
    @keyframes blip-pulse-green {
        0%, 100% { transform: scale(1); opacity: 0.9; }
        50% { transform: scale(1.5); opacity: 0.4; }
    }

    .radar-label {
        font-size: 0.75rem;
        font-weight: 600;
        color: #10b981;
        letter-spacing: 0.5px;
    }

    /* What the radar shows table card */
    .radar-legend-card {
        background: #0b1328;
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 14px;
        padding: 1.1rem;
        margin-bottom: 1rem;
    }
    .radar-legend-title {
        font-size: 0.85rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.35rem;
    }
    .radar-legend-sub {
        font-size: 0.72rem;
        color: #64748b;
        margin-bottom: 0.75rem;
        line-height: 1.35;
    }
    .radar-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.6rem;
    }
    .radar-grid-item {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        padding: 0.5rem;
    }
    .radar-grid-label {
        font-size: 0.68rem;
        font-weight: 700;
        color: #38bdf8;
        text-transform: uppercase;
        margin-bottom: 0.2rem;
    }
    .radar-grid-val {
        font-size: 0.74rem;
        color: #94a3b8;
    }

    /* Metrics Strip Cards */
    .metric-strip-card {
        background: #0b1328;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1rem 1.25rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .metric-strip-card:hover {
        transform: translateY(-2px);
        border-color: rgba(56, 189, 248, 0.3);
    }
    .metric-strip-num {
        font-size: 1.9rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1.1;
    }
    .metric-strip-label {
        font-size: 0.78rem;
        color: #94a3b8;
        margin-top: 0.25rem;
    }

    /* Priority Action Queue */
    .queue-card {
        background: #0b1328;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 1.25rem;
        height: 100%;
    }
    .queue-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1rem;
    }
    .queue-item {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        padding: 0.65rem 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    .queue-item:last-child {
        border-bottom: none;
    }
    .queue-item-left {
        display: flex;
        align-items: flex-start;
        gap: 0.6rem;
    }
    .queue-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        margin-top: 5px;
    }
    .dot-red { background: #ef4444; box-shadow: 0 0 6px #ef4444; }
    .dot-green { background: #10b981; box-shadow: 0 0 6px #10b981; }
    .dot-blue { background: #38bdf8; box-shadow: 0 0 6px #38bdf8; }
    .queue-item-text {
        font-size: 0.82rem;
        font-weight: 600;
        color: #e2e8f0;
    }
    .queue-item-sub {
        font-size: 0.72rem;
        color: #64748b;
        margin-top: 2px;
    }
    .badge-pill {
        font-size: 0.7rem;
        font-weight: 700;
        padding: 0.2rem 0.55rem;
        border-radius: 12px;
    }
    .badge-high {
        background: rgba(239, 68, 68, 0.15);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    .badge-setup {
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    .badge-ready {
        background: rgba(56, 189, 248, 0.15);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.3);
    }

    /* TrustOps Readiness Card */
    .trustops-card {
        background: #0b1328;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 1.25rem;
        height: 100%;
    }
    .trustops-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1rem;
    }
    .trustops-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.85rem;
    }
    .trustops-stat-num {
        font-size: 1.5rem;
        font-weight: 800;
        color: #ffffff;
    }
    .trustops-stat-label {
        font-size: 0.74rem;
        color: #94a3b8;
    }

    /* Polis Summary Card */
    .polis-card {
        background: #0b1328;
        border: 1px solid rgba(139, 92, 246, 0.25);
        border-radius: 14px;
        padding: 1.25rem;
        height: 100%;
    }
    .polis-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .polis-text {
        font-size: 0.82rem;
        color: #94a3b8;
        line-height: 1.55;
    }

    /* Bottom Catalog Row Cards */
    .bottom-stat-card {
        background: #091020;
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 1rem;
        height: 100%;
    }
    .bottom-stat-num {
        font-size: 1.4rem;
        font-weight: 800;
        color: #ffffff;
    }
    .bottom-stat-desc {
        font-size: 0.74rem;
        color: #64748b;
        margin-top: 0.25rem;
        line-height: 1.35;
    }

    /* Bottom Floating Bar */
    .floating-copilot-bar {
        background: rgba(11, 19, 39, 0.9);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 30px;
        padding: 0.5rem 1.2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 2rem;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
    }
    .copilot-input-pill {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        color: #94a3b8;
        font-size: 0.88rem;
    }
</style>
"""
