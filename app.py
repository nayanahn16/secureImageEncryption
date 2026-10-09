"""
Secure Image Encryption and File Transfer System
Using Python, AES-256-GCM, RSA-2048 OAEP, and SHA-256 Integrity Verification.
Styled with the Dark Cyber Command Center Aesthetic.
"""

import os
import mimetypes
import hashlib
from datetime import datetime
import streamlit as st

# Custom Theme and Streamlined Components
from styles import get_cyber_theme_css
import components
import importlib
importlib.reload(components)

# Cryptographic and Application Modules
from authentication.register import register_user
from authentication.login import login_user
from encryption.rsa_keys import ensure_keys_exist, load_public_key, load_private_key
from encryption.aes_encrypt import encrypt_file, calculate_sha256
from encryption.aes_decrypt import decrypt_file, InvalidTagError, DecryptionError
from encryption.des_demo import des_encrypt_text, des_decrypt_text, get_algorithm_comparison
from transfer.send_file import send_file, list_transfer_files
from transfer.receive_file import receive_file, list_received_files


# ==============================================================================
# 1. DIRECTORY INITIALIZATION
# ==============================================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIRS = {
    "uploads": os.path.join(BASE_DIR, "uploads"),
    "encrypted": os.path.join(BASE_DIR, "encrypted"),
    "transfer": os.path.join(BASE_DIR, "transfer"),
    "received": os.path.join(BASE_DIR, "received"),
    "decrypted": os.path.join(BASE_DIR, "decrypted"),
    "keys": os.path.join(BASE_DIR, "keys"),
    "auth": os.path.join(BASE_DIR, "authentication"),
}

for d in DIRS.values():
    os.makedirs(d, exist_ok=True)

# Ensure RSA key pair exists on initial load
ensure_keys_exist(
    private_path=os.path.join(DIRS["keys"], "private_key.pem"),
    public_path=os.path.join(DIRS["keys"], "public_key.pem")
)


# ==============================================================================
# 2. PAGE CONFIGURATION & THEME
# ==============================================================================
st.set_page_config(
    page_title="CipherGuard SP - Cryptographic Command Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject dark cybersecurity stylesheet
st.markdown(get_cyber_theme_css(), unsafe_allow_html=True)


# ==============================================================================
# 3. SESSION STATE MANAGEMENT
# ==============================================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True
if "username" not in st.session_state:
    st.session_state.username = "Operator"
if "current_view" not in st.session_state:
    st.session_state.current_view = "Dashboard"


def set_page(page_name: str):
    st.session_state.current_view = page_name


# ==============================================================================
# 4. STREAMLINED SIDEBAR NAVIGATION
# ==============================================================================
with st.sidebar:
    st.markdown(components.render_sidebar_header(), unsafe_allow_html=True)

    def render_nav_button(label: str, target: str):
        is_active = (st.session_state.current_view == target)
        btn_type = "primary" if is_active else "secondary"
        if st.button(label, type=btn_type, key=f"nav_{target}", use_container_width=True):
            set_page(target)
            st.rerun()

    # Core Project Pages
    render_nav_button("🏠  Dashboard", "Dashboard")
    render_nav_button("🔐  Encrypt File", "Encrypt File")
    render_nav_button("📤  Transfer Channel", "Transfer Channel")
    render_nav_button("📥  Receive Inbox", "Receive Inbox")
    render_nav_button("🔓  Decrypt & Verify", "Decrypt & Verify")
    render_nav_button("🧪  DES Demonstration", "DES Demonstration")
    render_nav_button("🛡️  Security Specs & Keys", "Security Specs & Keys")
    render_nav_button("🪪  User Authentication", "User Authentication")

    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

    # Active Engine Telemetry in Sidebar
    with st.container(border=True):
        st.markdown("""
        <div style="font-size: 0.75rem; color: #94a3b8; line-height: 1.6;">
            <div style="color: #38bdf8; font-weight: 700; margin-bottom: 4px;">ACTIVE CRYPTO ENGINE</div>
            <div>• AES-256-GCM (Payload)</div>
            <div>• RSA-2048 OAEP (Key Wrap)</div>
            <div>• SHA-256 (Bitwise Match)</div>
            <div>• SQLite (PBKDF2 Auth)</div>
        </div>
        """, unsafe_allow_html=True)


# ==============================================================================
# 5. GLOBAL INTERACTIVE TOP BAR & WORKING SEARCH
# ==============================================================================
top_col1, top_col2, top_col3 = st.columns([1.2, 1.8, 1.2], gap="small")
with top_col1:
    st.markdown(components.render_top_bar_left(), unsafe_allow_html=True)
with top_col2:
    search_query = st.text_input(
        "Search input",
        placeholder="🔍 Search encrypted files, hashes, algorithms, keys...",
        label_visibility="collapsed",
        key="global_search_input"
    )
with top_col3:
    st.markdown(components.render_top_bar_right(username=st.session_state.username), unsafe_allow_html=True)

st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)


# ==============================================================================
# 6. SEARCH HANDLER OR ROUTED VIEWS
# ==============================================================================
search_active = bool(search_query and search_query.strip())

if search_active:
    q = search_query.strip().lower()
    st.markdown(f"### 🔍 Search Results for: `{search_query.strip()}`")

    results_found = False

    # 1. Cryptographic concept search
    algo_matches = {
        "aes": ("AES-256-GCM (AEAD Cipher)", "Authenticated 256-bit symmetric cipher producing 128-bit GHASH tag. Encrypts multimedia payloads.", "Encrypt File"),
        "rsa": ("RSA-2048 OAEP (Key Wrapper)", "PKCS #1 v2.2 / RFC 8017 Optimal Asymmetric Encryption Padding. Wraps the 256-bit AES key.", "Security Specs & Keys"),
        "sha": ("SHA-256 (Integrity Verifier)", "FIPS 180-4 cryptographic hash for bitwise tamper auditing before and after transmission.", "Decrypt & Verify"),
        "des": ("Triple-DES (Feistel Demo)", "Legacy 56-bit Feistel cipher demonstrated for educational vulnerability evaluation.", "DES Demonstration"),
        "pbkdf2": ("PBKDF2-HMAC-SHA256 (User Auth)", "Salted 100,000 iterations key derivation function for password security in SQLite.", "User Authentication"),
        "gcm": ("Galois/Counter Mode (GCM)", "AEAD mode providing confidentiality and integrity simultaneously.", "Encrypt File"),
        "key": ("RSA Public & Private Key Infrastructure", "2048-bit key pair stored in keys/ directory used for symmetric key exchange.", "Security Specs & Keys"),
        "nonce": ("12-Byte Cryptographic Nonce", "Unique 96-bit random initialization vector per encryption to prevent replay attacks.", "Encrypt File"),
    }
    for k, (title, desc, target_page) in algo_matches.items():
        if k in q:
            results_found = True
            with st.container(border=True):
                ca, cb = st.columns([3, 1])
                with ca:
                    st.markdown(f"⚡ **`{title}`**")
                    st.caption(desc)
                with cb:
                    if st.button(f"Go to {target_page}", key=f"algo_btn_{k}"):
                        set_page(target_page)
                        st.session_state["global_search_input"] = ""
                        st.rerun()

    # 2. File search across all directories
    folder_mappings = [
        ("encrypted", "🔐 Encrypted Packages", "Transfer Channel"),
        ("transfer", "📤 Transfer Channel", "Receive Inbox"),
        ("received", "📥 Received Inbox", "Decrypt & Verify"),
        ("decrypted", "🔓 Decrypted & Verified", "Decrypt & Verify"),
        ("uploads", "📄 Source Uploads", "Encrypt File"),
        ("keys", "🔑 RSA Keys", "Security Specs & Keys"),
    ]

    file_matches = []
    for folder_key, folder_label, target_page in folder_mappings:
        f_dir = DIRS.get(folder_key)
        if f_dir and os.path.exists(f_dir):
            for fname in os.listdir(f_dir):
                if q in fname.lower():
                    file_matches.append((folder_label, fname, os.path.join(f_dir, fname), target_page))

    if file_matches:
        results_found = True
        st.write(f"**Found {len(file_matches)} matching file(s):**")
        for folder_label, fname, full_path, target_page in file_matches:
            with st.container(border=True):
                c1, c2, c3 = st.columns([2.2, 1, 1])
                with c1:
                    st.markdown(f"📦 **`{fname}`**")
                    st.caption(f"Location: `{folder_label}`")
                with c2:
                    st.write(f"{os.path.getsize(full_path):,} bytes")
                with c3:
                    if st.button(f"Manage in {target_page}", key=f"fmatch_{fname}_{folder_label}"):
                        set_page(target_page)
                        st.session_state["global_search_input"] = ""
                        st.rerun()

    if not results_found:
        st.info(f"No files or algorithms matching '{search_query}'. Try searching for 'test', 'image', 'enc', 'aes', 'rsa', 'sha', or 'key'.")

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    if st.button("⬅️ Clear Search & Return to Dashboard", type="primary"):
        st.session_state["global_search_input"] = ""
        st.rerun()

# ------------------------------------------------------------------------------
# VIEW: DASHBOARD (CYBER COMMAND CENTER)
# ------------------------------------------------------------------------------
elif st.session_state.current_view == "Dashboard":
    col_hero, col_right = st.columns([1.65, 1], gap="medium")

    with col_hero:
        # Hero Banner
        st.markdown(components.render_hero_card(), unsafe_allow_html=True)

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

        # 4 Core Quick Action Buttons
        act1, act2, act3, act4 = st.columns(4)
        with act1:
            if st.button("🔐 Encrypt File", use_container_width=True, type="primary"):
                set_page("Encrypt File")
                st.rerun()
        with act2:
            if st.button("📤 Transfer Channel", use_container_width=True):
                set_page("Transfer Channel")
                st.rerun()
        with act3:
            if st.button("📥 Receive Inbox", use_container_width=True):
                set_page("Receive Inbox")
                st.rerun()
        with act4:
            if st.button("🔓 Decrypt & Verify", use_container_width=True):
                set_page("Decrypt & Verify")
                st.rerun()

    with col_right:
        # Security Posture Gauge, Live Signal Radar, and Matrix
        st.markdown(components.render_security_posture(score=100), unsafe_allow_html=True)
        st.markdown(components.render_live_radar(), unsafe_allow_html=True)
        st.markdown(components.render_radar_legend(), unsafe_allow_html=True)

    # 4-Metric Strip showing real-time project storage
    enc_count = len([f for f in os.listdir(DIRS["encrypted"]) if f.endswith(".enc")])
    trans_count = len(list_transfer_files())
    rec_count = len(list_received_files())
    dec_count = len(os.listdir(DIRS["decrypted"]))

    st.markdown(
        components.render_metric_strip(
            enc_count=enc_count,
            trans_count=trans_count,
            rec_count=rec_count,
            dec_count=dec_count
        ),
        unsafe_allow_html=True
    )

    # Lower 3 Cards: Pipeline Status, Health, and Architecture Summary
    c1, c2, c3 = st.columns([1.1, 1, 1], gap="medium")
    with c1:
        st.markdown(components.render_action_queue(), unsafe_allow_html=True)
    with c2:
        pub_exists = os.path.exists(os.path.join(DIRS["keys"], "public_key.pem"))
        st.markdown(components.render_system_health(keys_exist=pub_exists), unsafe_allow_html=True)
    with c3:
        st.markdown(components.render_crypto_summary(), unsafe_allow_html=True)

    # Bottom Standards Row
    st.markdown(components.render_bottom_stats(), unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# VIEW: ENCRYPT FILE (AES-256-GCM + RSA-2048 OAEP)
# ------------------------------------------------------------------------------
elif st.session_state.current_view == "Encrypt File":
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <h2 style="color: #ffffff; margin-bottom: 0.25rem;">🔐 File Encryption: AES-256-GCM & RSA-2048 OAEP</h2>
        <div style="color: #94a3b8; font-size: 0.9rem;">
            Symmetric bulk file encryption encapsulated by asymmetric RSA-2048 key exchange
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Sample file loader
    sample_path = os.path.join(DIRS["uploads"], "test_image.jpg")
    use_sample = False
    if os.path.exists(sample_path):
        if st.button("🖼️ Or Click to Quick-Load Sample Image (`test_image.jpg`)"):
            use_sample = True

    uploaded_file = st.file_uploader(
        "Upload image or document to encrypt (JPG, JPEG, PNG, PDF, TXT, DOCX)",
        type=["jpg", "jpeg", "png", "pdf", "txt", "docx"]
    )

    data_to_encrypt = None
    orig_filename = None

    if uploaded_file is not None:
        data_to_encrypt = uploaded_file.getvalue()
        orig_filename = os.path.basename(uploaded_file.name)
    elif use_sample:
        with open(sample_path, "rb") as f:
            data_to_encrypt = f.read()
        orig_filename = "test_image.jpg"

    if data_to_encrypt is not None:
        orig_sha = calculate_sha256(data_to_encrypt)

        col1, col2 = st.columns([1.1, 1], gap="medium")
        with col1:
            with st.container(border=True):
                st.subheader("📄 Original File Telemetry")
                st.write(f"**Filename:** `{orig_filename}`")
                st.write(f"**Size:** {len(data_to_encrypt):,} bytes ({len(data_to_encrypt)/1024:.2f} KB)")
                st.write("**Pre-Encryption SHA-256 Hash:**")
                st.code(orig_sha, language="text")

                if orig_filename.lower().endswith((".jpg", ".jpeg", ".png")):
                    st.image(data_to_encrypt, caption="File Preview", width=320)

        with col2:
            with st.container(border=True):
                st.subheader("⚙️ Hybrid Encryption Execution")
                st.markdown("""
                Executing this operation will:
                1. Generate an ephemeral **256-bit AES key** and **12-byte random nonce**.
                2. Encrypt the file using **AES-256-GCM** (producing 128-bit GHASH tag).
                3. Wrap the AES key using **RSA-2048 OAEP (SHA-256)**.
                4. Create a self-contained **`.enc` binary package**.
                """)

                if st.button("🔐 Execute Hybrid Encryption", use_container_width=True, type="primary"):
                    try:
                        with st.spinner("Encrypting payload and encapsulating key..."):
                            public_key = load_public_key()
                            pkg_bytes, out_path, meta = encrypt_file(
                                file_input=data_to_encrypt,
                                original_filename=orig_filename,
                                public_key=public_key
                            )

                        st.success("🎉 File encrypted successfully!")
                        st.info(f"Encrypted package stored in: `{out_path}`")

                        # Download button
                        st.download_button(
                            label=f"⬇️ Download {orig_filename}.enc Package",
                            data=pkg_bytes,
                            file_name=f"{orig_filename}.enc",
                            mime="application/octet-stream",
                            use_container_width=True
                        )

                        # Transfer directly
                        if st.button("📤 Push Directly to Transfer Channel Now", use_container_width=True):
                            s_ok, _, s_msg = send_file(out_path)
                            if s_ok:
                                st.success("🎉 Package transferred to channel!")
                                set_page("Transfer Channel")
                                st.rerun()

                    except Exception as e:
                        st.error(f"❌ Encryption failed: {str(e)}")


# ------------------------------------------------------------------------------
# VIEW: TRANSFER CHANNEL
# ------------------------------------------------------------------------------
elif st.session_state.current_view == "Transfer Channel":
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <h2 style="color: #ffffff; margin-bottom: 0.25rem;">📤 Secure Transmission Channel Simulation</h2>
        <div style="color: #94a3b8; font-size: 0.9rem;">
            Staging channel ensuring only encrypted ciphertext (.enc) packages are transmitted
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("**Transmission Pipeline Flow:** `Sender (encrypted/)` ──► `Channel (transfer/)` ──► `Receiver (received/)`")

    enc_files = [f for f in os.listdir(DIRS["encrypted"]) if f.endswith(".enc")]

    col1, col2 = st.columns([1, 1], gap="medium")
    with col1:
        with st.container(border=True):
            st.subheader("Select from Encrypted Storage")
            if enc_files:
                chosen_file = st.selectbox("Select encrypted package (.enc):", enc_files)
                if st.button("📤 Dispatch to Transfer Channel", use_container_width=True, type="primary"):
                    src = os.path.join(DIRS["encrypted"], chosen_file)
                    ok, dest, msg = send_file(src)
                    if ok:
                        st.success("🎉 File transferred successfully!")
                        st.info(f"Target location: `{dest}`")
                    else:
                        st.error(f"❌ {msg}")
            else:
                st.info("No encrypted files in `encrypted/`. Encrypt a file first.")

    with col2:
        with st.container(border=True):
            st.subheader("Or Upload External .enc Package")
            uploaded_enc = st.file_uploader("Upload .enc file to transfer", type=["enc"], key="tr_enc_box")
            if uploaded_enc is not None:
                if st.button("📤 Inject into Channel", use_container_width=True, type="primary"):
                    ok, dest, msg = send_file(uploaded_enc.getvalue(), filename=uploaded_enc.name)
                    if ok:
                        st.success("🎉 Package transferred to channel!")
                    else:
                        st.error(f"❌ {msg}")

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.subheader("Files Currently in Transfer Channel (`transfer/`):")
        transfers = list_transfer_files()
        if transfers:
            for t in transfers:
                st.write(f"📦 `{t}` ({os.path.getsize(os.path.join(DIRS['transfer'], t)):,} bytes)")
        else:
            st.caption("No files currently in the transfer channel.")


# ------------------------------------------------------------------------------
# VIEW: RECEIVE INBOX
# ------------------------------------------------------------------------------
elif st.session_state.current_view == "Receive Inbox":
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <h2 style="color: #ffffff; margin-bottom: 0.25rem;">📥 Ingress Verification & Receive Inbox</h2>
        <div style="color: #94a3b8; font-size: 0.9rem;">
            Retrieve ciphertext packages from the transmission channel into receiver storage
        </div>
    </div>
    """, unsafe_allow_html=True)

    transfer_files = list_transfer_files()

    if transfer_files:
        with st.container(border=True):
            st.subheader("Available Packages in Transfer Channel")
            target_to_receive = st.selectbox("Select package to ingest:", transfer_files)

            col1, col2 = st.columns([1, 1], gap="medium")
            with col1:
                if st.button("📥 Ingest Package to Receiver", use_container_width=True, type="primary"):
                    ok, rec_path, msg = receive_file(target_to_receive)
                    if ok:
                        st.success("🎉 File received successfully!")
                        st.info(f"Stored in: `{rec_path}`")
                    else:
                        st.error(f"❌ {msg}")
            with col2:
                if st.button("Proceed to Decryption & Audit ➔", use_container_width=True):
                    set_page("Decrypt & Verify")
                    st.rerun()
    else:
        st.info("ℹ️ No packages currently pending in the transfer channel.")

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.subheader("Receiver Inbox Storage (`received/`):")
        received = list_received_files()
        if received:
            for r in received:
                st.write(f"📥 `{r}` ({os.path.getsize(os.path.join(DIRS['received'], r)):,} bytes)")
        else:
            st.caption("Receiver inbox is currently empty.")


# ------------------------------------------------------------------------------
# VIEW: DECRYPT & VERIFY (TAMPER DETECTION & SHA-256 AUDIT)
# ------------------------------------------------------------------------------
elif st.session_state.current_view == "Decrypt & Verify":
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <h2 style="color: #ffffff; margin-bottom: 0.25rem;">🔓 Decrypt File & SHA-256 Integrity Verification</h2>
        <div style="color: #94a3b8; font-size: 0.9rem;">
            RSA-2048 OAEP private key unwrapping, AES-256-GCM authentication verification, and bitwise SHA-256 auditing
        </div>
    </div>
    """, unsafe_allow_html=True)

    received_list = list_received_files()
    col1, col2 = st.columns([1, 1], gap="medium")

    pkg_bytes = None
    pkg_name = None

    with col1:
        with st.container(border=True):
            st.subheader("Option 1: Select From Received Inbox")
            if received_list:
                sel_pkg = st.selectbox("Choose received package:", received_list)
                if sel_pkg:
                    with open(os.path.join(DIRS["received"], sel_pkg), "rb") as f:
                        pkg_bytes = f.read()
                    pkg_name = sel_pkg
            else:
                st.info("No files in received inbox.")

    with col2:
        with st.container(border=True):
            st.subheader("Option 2: Upload External .enc Package")
            up_pkg = st.file_uploader("Upload ciphertext package", type=["enc"], key="dec_pkg_uploader_box")
            if up_pkg is not None:
                pkg_bytes = up_pkg.getvalue()
                pkg_name = up_pkg.name

    if pkg_bytes is not None:
        st.markdown(f"**Target Package:** `{pkg_name}` ({len(pkg_bytes):,} bytes)")

        if st.button("🔓 Decrypt & Verify Bitwise Integrity", use_container_width=True, type="primary"):
            try:
                with st.spinner("Unwrapping AES key with RSA private key and verifying GHASH tag..."):
                    private_key = load_private_key()
                    dec_bytes, rec_filename, meta = decrypt_file(
                        file_input=pkg_bytes,
                        private_key=private_key,
                        output_folder=DIRS["decrypted"]
                    )

                st.success("🎉 Package decrypted successfully!")

                orig_hash = meta.get("original_sha256")
                dec_hash = meta.get("decrypted_sha256")
                status = meta.get("integrity_status")

                if status == "MATCH":
                    st.success("✅ **Integrity Status: BITWISE MATCH CONFIRMED** (Decrypted file is 100% bitwise identical to the original)")
                else:
                    st.error("❌ **Integrity Status: HASH MISMATCH DETECTED**")

                col_a, col_b = st.columns([1.1, 1], gap="medium")
                with col_a:
                    with st.container(border=True):
                        st.subheader("🔍 SHA-256 Hash Verification")
                        if orig_hash:
                            st.write("**Pre-Encryption SHA-256:**")
                            st.code(orig_hash, language="text")
                        st.write("**Post-Decryption SHA-256:**")
                        st.code(dec_hash, language="text")
                        st.write(f"**Integrity Status:** `{status}`")

                with col_b:
                    with st.container(border=True):
                        st.subheader("🖼️ Recovered File Telemetry")
                        st.write(f"**Recovered Filename:** `{rec_filename}`")
                        st.write(f"**Size:** {len(dec_bytes):,} bytes")

                        mime, _ = mimetypes.guess_type(rec_filename)
                        if (mime and mime.startswith("image/")) or rec_filename.lower().endswith((".jpg", ".jpeg", ".png")):
                            st.image(dec_bytes, caption="Recovered Image", width=320)
                        elif rec_filename.endswith(".txt"):
                            try:
                                st.text_area("Decrypted Text", dec_bytes.decode("utf-8")[:1000], height=120)
                            except Exception:
                                st.write("Binary content.")

                        st.download_button(
                            label=f"⬇️ Download Recovered {rec_filename}",
                            data=dec_bytes,
                            file_name=rec_filename,
                            mime=mime or "application/octet-stream",
                            use_container_width=True
                        )

            except InvalidTagError:
                st.error("❌ GHASH Verification Failed: The encrypted file has been tampered with, corrupted, or the cryptographic key is invalid.")
            except DecryptionError as de:
                st.error(f"❌ Decryption Error: {str(de)}")
            except Exception as e:
                st.error(f"❌ Decryption Failed: {str(e)}")


# ------------------------------------------------------------------------------
# VIEW: DES DEMONSTRATION (EDUCATIONAL FEISTEL COMPARISON)
# ------------------------------------------------------------------------------
elif st.session_state.current_view == "DES Demonstration":
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <h2 style="color: #ffffff; margin-bottom: 0.25rem;">🧪 DES Demonstration: Legacy Feistel vs Modern AES</h2>
        <div style="color: #94a3b8; font-size: 0.9rem;">
            Comparative analysis of legacy 56-bit DES vulnerabilities versus modern 256-bit Galois/Counter Mode
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):
        st.warning("""
        ⚠️ **Notice:** DES (Data Encryption Standard) is an obsolete 1977 cipher with a 56-bit key susceptible to brute-force attacks.
        It is demonstrated here strictly for educational comparison and viva evaluation.
        **AES-256-GCM is used for actual secure file encryption in this project.**
        """)

    col1, col2 = st.columns([1, 1], gap="medium")
    with col1:
        with st.container(border=True):
            st.subheader("🔬 Interactive Triple-DES Sandbox")
            sample_text = st.text_input("Enter text to encrypt with Triple-DES:", "Major Project DES Demonstration")

            if st.button("Encrypt with Triple-DES", use_container_width=True, type="primary"):
                ct_b64, iv_b64, key_bytes, iv_bytes = des_encrypt_text(sample_text)
                st.session_state["des_ct"] = ct_b64
                st.session_state["des_key"] = key_bytes.hex()
                st.session_state["des_iv"] = iv_b64

            if "des_ct" in st.session_state:
                st.write(f"**Triple-DES Key (Hex):** `{st.session_state['des_key']}`")
                st.write(f"**Initialization Vector (Base64):** `{st.session_state['des_iv']}`")
                st.write("**Ciphertext (Base64):**")
                st.code(st.session_state["des_ct"], language="text")

                if st.button("Decrypt Triple-DES Ciphertext", use_container_width=True):
                    recovered = des_decrypt_text(
                        st.session_state["des_ct"],
                        bytes.fromhex(st.session_state["des_key"]),
                        st.session_state["des_iv"]
                    )
                    st.success(f"🎉 Decrypted Plaintext: **{recovered}**")

    with col2:
        with st.container(border=True):
            st.subheader("📊 Algorithm Comparison Matrix")
            st.table(get_algorithm_comparison())


# ------------------------------------------------------------------------------
# VIEW: SECURITY SPECS & KEYS
# ------------------------------------------------------------------------------
elif st.session_state.current_view == "Security Specs & Keys":
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <h2 style="color: #ffffff; margin-bottom: 0.25rem;">🛡️ Cryptographic Specifications & RSA Key Center</h2>
        <div style="color: #94a3b8; font-size: 0.9rem;">
            Technical architecture reference for Hybrid Cryptography (AES-256-GCM + RSA-2048 OAEP)
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="medium")
    with col1:
        with st.container(border=True):
            st.subheader("🏛️ Why Hybrid Encryption?")
            st.markdown("""
            - **RSA is too slow for bulk media:** RSA-2048 can only encrypt $\\approx 190$ bytes per operation. Directly encrypting whole images causes severe computational bottlenecks.
            - **AES-GCM for High Throughput:** AES-256 encrypts large files in milliseconds with hardware acceleration.
            - **RSA-OAEP for Key Wrapping:** RSA is used exclusively to wrap the 256-bit AES key.
            - **Result:** Best of both worlds — symmetric speed combined with asymmetric key distribution.
            """)

    with col2:
        with st.container(border=True):
            st.subheader("🔑 Active RSA Key Infrastructure")
            pub_path = os.path.join(DIRS["keys"], "public_key.pem")
            priv_path = os.path.join(DIRS["keys"], "private_key.pem")
            st.write(f"• **Public Key:** `{pub_path}` (Exists: {os.path.exists(pub_path)})")
            st.write(f"• **Private Key:** `{priv_path}` (Exists: {os.path.exists(priv_path)})")
            if os.path.exists(pub_path):
                with open(pub_path, "r") as f:
                    st.text_area("RSA-2048 Public Key (PEM)", f.read(), height=150)


# ------------------------------------------------------------------------------
# VIEW: USER AUTHENTICATION
# ------------------------------------------------------------------------------
elif st.session_state.current_view == "User Authentication":
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <h2 style="color: #ffffff; margin-bottom: 0.25rem;">🪪 User Authentication & Access Control</h2>
        <div style="color: #94a3b8; font-size: 0.9rem;">
            Salted PBKDF2-HMAC-SHA256 password derivation (100,000 iterations) stored securely in SQLite
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab_login, tab_register = st.tabs(["🔑 Account Sign In", "📝 Register New User"])

    with tab_login:
        col1, col2 = st.columns([1, 1], gap="medium")
        with col1:
            with st.container(border=True):
                st.subheader("Sign In")
                log_user = st.text_input("Username", value=st.session_state.username)
                log_pass = st.text_input("Password", type="password")
                if st.button("Sign In", use_container_width=True, type="primary"):
                    ok, msg = login_user(log_user, log_pass)
                    if ok:
                        st.session_state.logged_in = True
                        st.session_state.username = log_user
                        st.success("🎉 Login successful!")
                        set_page("Dashboard")
                        st.rerun()
                    else:
                        st.error(f"❌ {msg}")
        with col2:
            with st.container(border=True):
                st.subheader("🔒 Password Security")
                st.markdown("""
                - **Salted Hashing:** 16 cryptographically random bytes (`os.urandom(16)`).
                - **PBKDF2-HMAC-SHA256:** 100,000 iterations to resist rainbow table attacks.
                - **Constant-Time Verification:** Protected against timing attacks.
                """)

    with tab_register:
        with st.container(border=True):
            st.subheader("Create Account")
            reg_user = st.text_input("New Username").strip()
            reg_pass = st.text_input("New Password (min 6 characters)", type="password")
            reg_conf = st.text_input("Confirm New Password", type="password")
            if st.button("Register Account", use_container_width=True, type="primary"):
                ok, msg = register_user(reg_user, reg_pass, reg_conf)
                if ok:
                    st.success(f"🎉 {msg} You can now log in.")
                else:
                    st.error(f"❌ {msg}")