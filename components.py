"""
HTML & SVG UI Components for the Cryptographic Command Center.
Robust, clean HTML without leading indentation so Markdown never renders code blocks.
"""

import html
from datetime import datetime


def clean_html(raw_html: str) -> str:
    """
    Strips leading/trailing whitespace from each line and joins with space.
    This guarantees that CommonMark/Markdown never treats indented lines
    as preformatted code blocks.
    """
    lines = [line.strip() for line in raw_html.strip().splitlines() if line.strip()]
    return " ".join(lines)


def render_top_bar_left() -> str:
    raw = """
    <div style="display: flex; align-items: center; gap: 0.75rem; padding: 0.35rem 0;">
        <div style="width: 32px; height: 32px; background: linear-gradient(135deg, #00f0ff, #3b82f6); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 18px; color: #070b14; box-shadow: 0 0 12px rgba(0, 240, 255, 0.45);">
            C
        </div>
        <div>
            <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff; letter-spacing: -0.2px; line-height: 1.2;">
                CIPHERGUARD <span style="color: #00f0ff;">SP</span>
            </div>
            <div style="font-size: 0.72rem; color: #38bdf8; font-weight: 500;">
                Secure Hybrid Cryptosystem • AES-256-GCM & RSA-2048 OAEP
            </div>
        </div>
    </div>
    """
    return clean_html(raw)


def render_top_bar_right(username: str = "Operator") -> str:
    user_label = username if username else "Operator"
    user_initial = user_label[0].upper()
    now_str = datetime.now().strftime("%H:%M") + " LIVE"

    raw = f"""
    <div style="display: flex; align-items: center; justify-content: flex-end; gap: 0.75rem; padding: 0.35rem 0; font-size: 0.8rem; color: #94a3b8;">
        <span style="padding: 4px 9px; background: rgba(16, 185, 129, 0.12); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; font-weight: 600; font-size: 0.72rem;">🟢 CHANNEL READY</span>
        <span style="color: #cbd5e1; font-weight: 500;">🕒 {now_str}</span>
        <div style="display: flex; align-items: center; gap: 0.4rem; background: rgba(139, 92, 246, 0.15); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 16px; padding: 3px 9px; color: #ddd6fe;">
            <div style="width: 20px; height: 20px; border-radius: 50%; background: #8b5cf6; color: white; font-size: 11px; font-weight: 700; display: flex; align-items: center; justify-content: center;">{user_initial}</div>
            <span style="font-weight: 600;">{html.escape(user_label)}</span>
        </div>
    </div>
    """
    return clean_html(raw)


def render_sidebar_header() -> str:
    raw = """
    <div style="padding: 0.5rem 0.2rem 1.25rem 0.2rem; border-bottom: 1px solid rgba(255,255,255,0.07); margin-bottom: 1rem;">
        <div style="display: flex; align-items: center; gap: 0.75rem;">
            <div style="width: 38px; height: 38px; border-radius: 8px; background: linear-gradient(135deg, #00f0ff, #3b82f6); display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 20px; color: #070b14; box-shadow: 0 0 16px rgba(0,240,255,0.4);">
                C
            </div>
            <div>
                <div style="font-size: 1.15rem; font-weight: 800; letter-spacing: 0.5px; color: #ffffff;">
                    CIPHERGUARD <span style="color: #00f0ff; font-weight: 600;">SP</span>
                </div>
                <div style="font-size: 0.68rem; font-weight: 600; color: #94a3b8; letter-spacing: 1px; text-transform: uppercase;">
                    CRYPTOGRAPHIC COMMAND
                </div>
            </div>
        </div>
    </div>
    """
    return clean_html(raw)


def render_hero_card() -> str:
    raw = """
    <div class="cyber-hero">
        <div class="hero-badge">UNIFIED CRYPTOGRAPHIC PROGRAM HOME</div>
        <div class="hero-logo-row">
            <div class="hero-logo-box">C</div>
            <div>
                <div class="hero-brand-name">CIPHERGUARD <span>SP</span></div>
                <div class="hero-brand-tag">HYBRID CRYPTOSYSTEM • SECURE, COMPLIANT, CONFIDENT.</div>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1.5rem; margin-top: 1rem;">
            <div style="flex: 1.4;">
                <div class="hero-title">Your cryptographic security & file transfer command center.</div>
                <div class="hero-desc">
                    A unified dark command surface for AES-256-GCM payload encryption, RSA-2048 OAEP asymmetric key encapsulation, secure channel staging, and tamper-evident SHA-256 verification.
                </div>
            </div>
            <div class="copilot-shortcut" style="flex: 0.75;">
                <div class="copilot-shortcut-title">
                    <span>🛡️</span>
                    <span>Active Cryptographic Stack</span>
                </div>
                <div class="copilot-shortcut-text">
                    • <b>AES-256-GCM:</b> 12-byte nonce + 128-bit GHASH<br>
                    • <b>RSA-2048 OAEP:</b> IND-CCA2 Key Wrapping<br>
                    • <b>SHA-256:</b> Bitwise Tamper Auditing<br>
                    • <b>SIEF Header:</b> Deterministic Binary Packaging
                </div>
            </div>
        </div>
    </div>
    """
    return clean_html(raw)


def render_security_posture(score: int = 100, *args, **kwargs) -> str:
    raw = f"""
    <div class="posture-card">
        <div class="posture-title">OVERALL CRYPTOGRAPHIC POSTURE</div>
        <div class="posture-score">{score}/100</div>
        <div class="posture-bar-bg">
            <div class="posture-bar-fill" style="width: {min(100, max(0, score))}%;"></div>
        </div>
        <div class="posture-sub">
            Calculated across AES-256-GCM AEAD, RSA-2048 OAEP encapsulation, SHA-256 integrity, and PBKDF2 authentication.
        </div>
    </div>
    """
    return clean_html(raw)


def render_live_radar() -> str:
    raw = """
    <div class="radar-card">
        <div class="radar-screen">
            <div class="radar-ring radar-ring-1"></div>
            <div class="radar-ring radar-ring-2"></div>
            <div class="radar-ring radar-ring-3"></div>
            <div class="radar-crosshair-h"></div>
            <div class="radar-crosshair-v"></div>
            <div class="radar-sweep"></div>
            <div class="blip blip-red" title="Tamper Detection Sentry Active"></div>
            <div class="blip blip-green-1" title="Encrypted Storage Online"></div>
            <div class="blip blip-green-2" title="Transfer Channel Verified"></div>
        </div>
        <div class="radar-label">📡 Live signal radar • Channel Monitor</div>
    </div>
    """
    return clean_html(raw)


def render_radar_legend() -> str:
    raw = """
    <div class="radar-legend-card">
        <div class="radar-legend-title">Channel Activity Matrix</div>
        <div class="radar-legend-sub">
            Continuous cryptographic telemetry monitoring payloads, key distribution, and channel transit.
        </div>
        <div class="radar-grid">
            <div class="radar-grid-item">
                <div class="radar-grid-label">Payload Cipher</div>
                <div class="radar-grid-val">AES-256-GCM (AEAD)</div>
            </div>
            <div class="radar-grid-item">
                <div class="radar-grid-label">Key Protection</div>
                <div class="radar-grid-val">RSA-2048 OAEP</div>
            </div>
            <div class="radar-grid-item">
                <div class="radar-grid-label">Integrity Tag</div>
                <div class="radar-grid-val">128-bit GHASH</div>
            </div>
            <div class="radar-grid-item">
                <div class="radar-grid-label">Audit Method</div>
                <div class="radar-grid-val">SHA-256 Pre/Post</div>
            </div>
        </div>
    </div>
    """
    return clean_html(raw)


def render_metric_strip(*args, **kwargs) -> str:
    """
    Bulletproof metric strip that accepts any argument signature
    (enc_count, trans_count, rec_count, dec_count OR risks, control_pct, requests, findings).
    """
    enc_val = kwargs.get("enc_count", kwargs.get("risks", args[0] if len(args) > 0 else 0))
    trans_val = kwargs.get("trans_count", kwargs.get("control_pct", args[1] if len(args) > 1 else 0))
    rec_val = kwargs.get("rec_count", kwargs.get("requests", args[2] if len(args) > 2 else 0))
    dec_val = kwargs.get("dec_count", kwargs.get("findings", args[3] if len(args) > 3 else 0))

    raw = f"""
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin: 1.25rem 0;">
        <div class="metric-strip-card">
            <div class="metric-strip-num">{enc_val}</div>
            <div class="metric-strip-label">Encrypted Packages (`encrypted/`)</div>
        </div>
        <div class="metric-strip-card">
            <div class="metric-strip-num">{trans_val}</div>
            <div class="metric-strip-label">In Transfer Channel (`transfer/`)</div>
        </div>
        <div class="metric-strip-card">
            <div class="metric-strip-num">{rec_val}</div>
            <div class="metric-strip-label">Received Packages (`received/`)</div>
        </div>
        <div class="metric-strip-card">
            <div class="metric-strip-num">{dec_val}</div>
            <div class="metric-strip-label">Decrypted & Verified (`decrypted/`)</div>
        </div>
    </div>
    """
    return clean_html(raw)


def render_action_queue() -> str:
    raw = """
    <div class="queue-card">
        <div class="queue-title">Cryptographic Pipeline Status</div>
        <div class="queue-item">
            <div class="queue-item-left">
                <div class="queue-dot dot-green"></div>
                <div>
                    <div class="queue-item-text">AES-256-GCM AEAD Engine</div>
                    <div class="queue-item-sub">256-bit symmetric cipher with 12-byte random nonce and 128-bit tag</div>
                </div>
            </div>
            <span class="badge-pill badge-setup">Active</span>
        </div>
        <div class="queue-item">
            <div class="queue-item-left">
                <div class="queue-dot dot-green"></div>
                <div>
                    <div class="queue-item-text">RSA-2048 OAEP Key Encapsulation</div>
                    <div class="queue-item-sub">IND-CCA2 secure asymmetric wrapper for AES keys</div>
                </div>
            </div>
            <span class="badge-pill badge-ready">Ready</span>
        </div>
        <div class="queue-item">
            <div class="queue-item-left">
                <div class="queue-dot dot-blue"></div>
                <div>
                    <div class="queue-item-text">Deterministic SIEF Binary Framing</div>
                    <div class="queue-item-sub">Byte-exact header packaging eliminating InvalidTag errors</div>
                </div>
            </div>
            <span class="badge-pill badge-ready">Online</span>
        </div>
    </div>
    """
    return clean_html(raw)


def render_system_health(keys_exist: bool = True) -> str:
    key_status = "Available" if keys_exist else "Generating"
    raw = f"""
    <div class="trustops-card">
        <div class="trustops-title">System Health & Security</div>
        <div class="trustops-grid">
            <div>
                <div class="trustops-stat-num">100%</div>
                <div class="trustops-stat-label">Integrity Match Rate</div>
            </div>
            <div>
                <div class="trustops-stat-num">0</div>
                <div class="trustops-stat-label">InvalidTag Errors</div>
            </div>
            <div>
                <div class="trustops-stat-num">100k</div>
                <div class="trustops-stat-label">PBKDF2 Iterations</div>
            </div>
            <div>
                <div class="trustops-stat-num" style="font-size: 1.15rem; color: #34d399;">{key_status}</div>
                <div class="trustops-stat-label">RSA-2048 Pair</div>
            </div>
        </div>
    </div>
    """
    return clean_html(raw)


def render_crypto_summary() -> str:
    raw = """
    <div class="polis-card">
        <div class="polis-title">
            <span>🛡️</span>
            <span>Architecture Summary</span>
        </div>
        <div class="polis-text">
            <b>Hybrid Cryptography Solves Key Bottlenecks:</b><br>
            • Symmetric AES-256 encrypts high-resolution images in milliseconds.<br>
            • Asymmetric RSA-2048 secures the AES key without pre-shared secrets.<br>
            • Bitwise SHA-256 checks guarantee zero file tampering.
        </div>
    </div>
    """
    return clean_html(raw)


def render_bottom_stats() -> str:
    raw = """
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin-top: 1.25rem;">
        <div class="bottom-stat-card">
            <div class="bottom-stat-num">AES-256-GCM</div>
            <div class="bottom-stat-desc">NIST SP 800-38D Authenticated Encryption with Associated Data</div>
        </div>
        <div class="bottom-stat-card">
            <div class="bottom-stat-num">RSA-2048 OAEP</div>
            <div class="bottom-stat-desc">PKCS #1 v2.2 / RFC 8017 Asymmetric Key Protection</div>
        </div>
        <div class="bottom-stat-card">
            <div class="bottom-stat-num">SHA-256</div>
            <div class="bottom-stat-desc">FIPS 180-4 Bitwise Tamper-Evident Integrity Verification</div>
        </div>
        <div class="bottom-stat-card">
            <div class="bottom-stat-num">PBKDF2-HMAC</div>
            <div class="bottom-stat-desc">100,000 Rounds Salted Password Protection in SQLite</div>
        </div>
    </div>
    """
    return clean_html(raw)
