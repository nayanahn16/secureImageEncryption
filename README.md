# Secure Image Encryption and File Transfer System Using Python and Cryptographic Libraries

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red.svg)](https://streamlit.io/)
[![Cryptography](https://img.shields.io/badge/Cryptography-AES--GCM%20%7C%20RSA--OAEP-green.svg)](https://cryptography.io/)
[![Security](https://img.shields.io/badge/Security-NIST%20FIPS%20Compliant-success.svg)](https://csrc.nist.gov/)

A comprehensive Major Project implementing a robust, hybrid cryptographic application for secure digital image and file encryption, authenticated transmission simulation, and tamper-evident decryption. Built using Python, Streamlit, SQLite, and industry-standard cryptographic libraries (`cryptography`).

---

## 1. Introduction

In modern network architectures, transmitting digital multimedia and confidential documents across untrusted or public channels poses serious confidentiality, integrity, and authenticity risks. Traditional symmetric systems suffer from key-distribution vulnerabilities, while pure asymmetric systems are computationally infeasible for bulk multimedia files.

This project delivers a **production-grade Hybrid Cryptosystem** that seamlessly combines the raw speed and authenticated integrity of **AES-256-GCM** with the mathematical security of **RSA-2048 OAEP** asymmetric key encapsulation.

---

## 2. Problem Statement

1. **Vulnerability of Plaintext Transfer:** Digital images transferred over networks are prone to interception, unauthorized eavesdropping, and man-in-the-middle tampering.
2. **Key Distribution Bottlenecks:** Symmetric ciphers (such as AES) require a secure pre-shared secret between parties.
3. **Asymmetric Inefficiency on Multimedia:** Asymmetric ciphers (such as RSA) cannot directly encrypt large image files due to block size restrictions and severe computational overhead.
4. **Ciphertext Tampering & InvalidTag Failures:** Insecure packaging, bit flips, or missing authentication tags lead to silent data corruption or cryptographic exceptions (`cryptography.exceptions.InvalidTag`).

---

## 3. Objectives

- **Develop Secure User Authentication:** Implement salted password hashing using PBKDF2-HMAC-SHA256 (100,000 iterations) with SQLite storage and parameterized queries.
- **Implement Hybrid Cryptography:**
  - Encrypt images/files with **AES-256-GCM** generating a 12-byte nonce and 128-bit authentication tag.
  - Wrap the symmetric AES key using **RSA-2048 OAEP** with SHA-256 padding.
- **Eliminate InvalidTag Decryption Errors:** Design a deterministic binary packaging format (`SIEF` header) that encapsulates metadata, wrapped key, nonce, and ciphertext+tag without byte displacement.
- **Secure File Transfer Simulation:** Enforce strict staging channel protocols ensuring that **only encrypted `.enc` files** are transferred.
- **Integrity Verification:** Compare pre-encryption and post-decryption SHA-256 hashes to guarantee bit-level identity.
- **Provide Educational DES Demonstration:** Contrast legacy Feistel ciphers (DES / 3DES) with modern AES-256-GCM.

---

## 4. Key Features

- **Multi-Role Authentication:** User registration, input validation, duplicate prevention, and login session management.
- **Support for Varied Media Formats:** JPG, JPEG, PNG, PDF, TXT, DOCX.
- **Hybrid Encryption Pipeline:** Symmetric bulk file encryption combined with asymmetric key exchange.
- **Deterministic Package Architecture:** Tamper-evident packaging preserving original filenames, dimensions, and SHA-256 hashes.
- **Graceful Error Handling:** Dedicated handling for `InvalidTagError`, key mismatch, corrupted headers, and path traversal attempts.
- **Educational DES Module:** Interactive Triple-DES encryption/decryption alongside technical comparison matrices.
- **Interactive Web Interface:** Modern Streamlit dashboard with real-time security indicators and file managers.

---

## 5. Technology Stack

| Component | Technology | Rationale |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ / 3.14 | High-level scripting, rich cryptographic ecosystem |
| **Frontend UI** | Streamlit | Responsive, real-time reactive user interface |
| **Symmetric Cipher** | AES-256-GCM | Authenticated Encryption with Associated Data (AEAD) |
| **Asymmetric Cipher** | RSA-2048 OAEP (SHA-256) | Secure key encapsulation, IND-CCA2 security |
| **Hashing & KDF** | SHA-256, PBKDF2-HMAC | Tamper detection and salted password protection |
| **Database** | SQLite 3 | Embedded, zero-configuration relational storage |
| **Legacy Comparison**| Triple-DES (CBC + PKCS#7)| Educational demonstration of Feistel ciphers |

---

## 6. System Architecture

```
                      +-----------------------------+
                      | User Authentication (SQLite)|
                      |    (Salted PBKDF2-SHA256)   |
                      +--------------+--------------+
                                     |
                                     v
                  +-----------------------------------+
                  |         Upload File / Image       |
                  |          (uploads/ directory)     |
                  +------------------+----------------+
                                     |
                                     v
                  +-----------------------------------+
                  |       Generate Ephemeral Keys     |
                  |  - 256-bit AES Key (AESGCM)       |
                  |  - 12-byte Unique Random Nonce    |
                  +------------------+----------------+
                                     |
         +---------------------------+---------------------------+
         |                                                       |
         v                                                       v
+-------------------------------+               +-------------------------------+
|     AES-256-GCM Encryption    |               |      RSA-2048 OAEP Wrapping   |
| (Payload + 128-bit GHASH tag) |               |     (Encrypts 256-bit AES Key)|
+---------------+---------------+               +---------------+---------------+
                |                                               |
                +-----------------------+-----------------------+
                                        |
                                        v
                    +---------------------------------------+
                    |  Unified .enc Binary Packaging (SIEF) |
                    |  - Magic Bytes: b'SIEF'               |
                    |  - Metadata JSON (Filename & SHA256)  |
                    |  - RSA-Wrapped AES Key (256 bytes)    |
                    |  - Nonce (12 bytes)                   |
                    |  - Ciphertext + Authentication Tag    |
                    +-------------------+-------------------+
                                        |
                                        v
                    +---------------------------------------+
                    |   Simulated Secure Channel Transfer   |
                    |         (transfer/ directory)         |
                    +-------------------+-------------------+
                                        |
                                        v
                    +---------------------------------------+
                    |        Receiver Inbox Ingestion       |
                    |         (received/ directory)         |
                    +-------------------+-------------------+
                                        |
                                        v
                    +---------------------------------------+
                    |       RSA Private Key Unwrapping      |
                    |          (Recovers 256-bit AES Key)   |
                    +-------------------+-------------------+
                                        |
                                        v
                    +---------------------------------------+
                    |        AES-256-GCM Decryption         |
                    |      (GHASH Auth Tag Verification)    |
                    +-------------------+-------------------+
                                        |
                                        v
                    +---------------------------------------+
                    |       SHA-256 Integrity Verification  |
                    |       SHA256(Original) == SHA256(Dec) |
                    +-------------------+-------------------+
                                        |
                                        v
                    +---------------------------------------+
                    |    Recovered Original Image/File      |
                    |        (decrypted/ directory)         |
                    +---------------------------------------+
```

---

## 7. Cryptographic Workflows

### 7.1 Encryption Workflow
1. User uploads a file (e.g. `test_image.jpg`).
2. System computes `Original_SHA256 = SHA256(file_bytes)`.
3. An ephemeral **256-bit AES key** is generated via `os.urandom(32)`.
4. A **12-byte random nonce** is generated via `os.urandom(12)`.
5. The file is encrypted using **AES-GCM**, appending a 16-byte authentication tag.
6. The AES key is wrapped with the recipient's **RSA public key** using **OAEP padding with MGF1(SHA-256)**.
7. The binary package is written to `encrypted/<filename>.enc`.

### 7.2 Decryption Workflow
1. The `.enc` file is read in binary mode (`"rb"`).
2. The `SIEF` header parses:
   - Version number
   - Original filename and expected SHA-256 hash
   - 256-byte RSA-encrypted AES key
   - 12-byte nonce
   - Remaining bytes: AES-GCM ciphertext + authentication tag
3. The recipient's **RSA private key** (`keys/private_key.pem`) unwraps the AES key.
4. **AES-GCM** decrypts the ciphertext using the recovered key and nonce.
   - If even a single bit is altered, an `InvalidTag` exception is caught and reported safely.
5. The SHA-256 hash of the recovered data is calculated and verified against the header hash.
6. The bitwise identical file is saved to `decrypted/<filename>` and rendered for download.

---

## 8. Root Cause Analysis: The InvalidTag Problem

### Problem Encountered
In earlier project iterations, decryption consistently threw `cryptography.exceptions.InvalidTag`.

### Root Causes Identified
1. **Incomplete Download Payload:** The web download button delivered only the raw ciphertext bytes instead of the complete package containing the wrapped key and nonce.
2. **Header Slicing Displacements:** When reading the transferred file, the receiver treated the entire header plus payload as raw ciphertext, causing the GCM authentication tag verification to fail.
3. **Key Overwriting:** Separate auxiliary files (`nonce.bin`, `encrypted_aes_key.bin`) were overwritten when multiple files were processed, causing key mismatches.

### Solution Implemented
- Designed the **`SIEF` (Secure Image Encryption File) format**:
  - `[Magic: 4B]` + `[Version: 1B]` + `[MetaLen: 4B]` + `[MetaJSON: NB]` + `[KeyLen: 4B]` + `[EncKey: 256B]` + `[NonceLen: 2B]` + `[Nonce: 12B]` + `[Ciphertext+Tag]`
- Self-contained packages prevent any cross-file collisions.
- Unified packaging and un-packaging functions ensure exact byte alignment.

---

## 9. Folder Structure

```
Secure_Image_Encryption/
│
├── app.py                     # Main Streamlit web application
├── requirements.txt           # Project dependencies
├── README.md                  # Comprehensive documentation
│
├── authentication/            # User authentication package
│   ├── __init__.py
│   ├── register.py            # User registration & PBKDF2 hashing
│   ├── login.py               # User login & constant-time validation
│   └── users.db               # SQLite database
│
├── encryption/                # Cryptographic modules
│   ├── __init__.py
│   ├── aes_encrypt.py         # AES-256-GCM encryption & SIEF packaging
│   ├── aes_decrypt.py         # AES-256-GCM decryption & tag verification
│   ├── rsa_keys.py            # RSA-2048 key generation & OAEP wrapping
│   ├── des_demo.py            # Educational Triple-DES demonstration
│   ├── hybrid_encryption.py   # Standalone CLI hybrid encryption script
│   └── hybrid_decryption.py   # Standalone CLI hybrid decryption script
│
├── transfer/                  # File transfer simulation
│   ├── __init__.py
│   ├── send_file.py           # Sending encrypted files to staging
│   └── receive_file.py        # Receiving packages into inbox
│
├── keys/                      # Cryptographic key storage
│   ├── public_key.pem         # RSA-2048 public key
│   └── private_key.pem        # RSA-2048 private key
│
├── uploads/                   # Staging for uploaded files
│   └── test_image.jpg         # Sample image for demonstration
├── encrypted/                 # Encrypted .enc packages
├── received/                  # Received packages
├── decrypted/                 # Decrypted recovered files
│
└── tests/                     # Unit and integration test suite
    ├── test_authentication.py # Tests for register/login/salting
    ├── test_encryption.py     # Tests for AES, RSA, DES, transfer
    └── test_decryption.py     # Tests for round-trip, InvalidTag, tampering
```

---

## 10. Installation & Setup

### Prerequisites
- Python 3.10, 3.11, 3.12, 3.13, or 3.14
- Git (optional)

### Step 1: Clone or Navigate to the Project
```bash
cd Majorproject
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment
- **Windows (Command Prompt / PowerShell):**
  ```powershell
  venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 11. How to Run the Application

Execute the Streamlit application using:
```bash
python -m streamlit run app.py
```
or
```bash
streamlit run app.py
```

The application will launch in your default web browser at:
`http://localhost:8501`

---

## 12. Verification & Testing

The project includes an automated test suite covering all 14 project requirements:

To execute all tests:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### Test Coverage Highlights
- `test_authentication.py`: Registration, duplicate usernames, input validation, login verification, password salting uniqueness.
- `test_encryption.py`: RSA key generation, RSA-OAEP key wrapping, 12-byte nonce randomness, SIEF package formatting, transfer restrictions.
- `test_decryption.py`: Full image round-trip, bit-for-bit SHA-256 match, tampered bit detection via `InvalidTagError`, wrong RSA key rejection.

---

## 13. Security Considerations & Best Practices

1. **Defense in Depth:** Combination of authenticated encryption (AES-GCM), asymmetric wrapping (RSA-OAEP), and password derivation (PBKDF2).
2. **Tamper Detection:** Altering even a single bit in the `.enc` ciphertext will fail the 128-bit GHASH tag verification.
3. **No Private Key Leakage:** Private keys and AES keys are never rendered in client responses or UI logs.
4. **Parameterized SQL Queries:** Prevents SQL injection vulnerabilities.
5. **Path Traversal Protection:** All filenames are sanitized with `os.path.basename`.

---

## 14. Educational DES Comparison

| Metric | DES (1977) | Triple-DES (1998) | AES-256-GCM (Modern) |
| :--- | :--- | :--- | :--- |
| **Key Size** | 56 bits | 112 / 168 bits | 256 bits |
| **Block Size** | 64 bits (8 B) | 64 bits (8 B) | 128 bits (16 B) |
| **Structure** | Feistel (16 rounds) | Feistel (48 rounds) | SPN (14 rounds) |
| **Integrity** | None | None | 128-bit GHASH Auth Tag |
| **Security Status** | Broken (Insecure) | Deprecated | NIST Gold Standard |
| **Role in Project** | Educational Demo Only | Educational Demo Only | Core Production Engine |

---

## 15. Limitations & Future Enhancements

### Limitations
- File transfer is currently simulated across local channel directories (`transfer/` and `received/`).
- Database uses SQLite, suitable for local and departmental demonstration.

### Future Enhancements
- **Network Sockets / TLS Transmission:** Implement real-world TCP sockets with mutual TLS (mTLS) certificates.
- **Multi-Factor Authentication (MFA):** Integrate TOTP (Time-Based One-Time Passwords).
- **Multi-Recipient Encapsulation:** Allow encrypting a single AES key under multiple recipient RSA public keys.
- **Post-Quantum Cryptography (PQC):** Integrate lattice-based Kyber/ML-KEM algorithms.

---

## 16. Conclusion

This Major Project successfully demonstrates a secure, high-performance image and file encryption and transfer platform. By addressing key-management challenges with RSA-2048 OAEP and high-speed data encryption with AES-256-GCM, the system provides confidentiality, integrity, authenticity, and non-repudiation. The resolution of the `InvalidTag` issue ensures flawless demonstration, oral examination, and evaluation.
