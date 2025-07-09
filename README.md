I use this daily to encode and decode my payloads, I hope you find it useful as well.
---

# 🔐 Base64 URL Encoder/Decoder (Multi-Layer)

A simple Python CLI tool to **encode or decode URLs/payloads** using `quote_plus` and `unquote_plus` from Python's `urllib.parse`. Supports **multi-layer encoding/decoding**, and also provides a full recursive decode option.

---

## ⚙️ Features

- Encode or decode a payload `n` times
- Automatically detect and fully decode deeply nested encodings
- CLI and interactive modes
- Lightweight, no external dependencies except `pyinputplus`

---

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/occupythemind/Base64URL_encoder/.git
cd Base64URL_encoder/

2. Install dependencies

pip install pyinputplus


---

🚀 Usage

Command-line

python3 burl.py -p [payload] -m [encode|decode] -n [optional layer count]

Examples

# Encode once
python3 burl.py -p "admin/dashboard" -m encode

# Encode 3 times
python3 burl.py -p "admin/dashboard" -m encode -n 3

# Decode once
python3 burl.py -p "%252Fadmin" -m decode -n 1

# Full decode (no -n needed)
python3 burl.py -p "%252Fadmin" -m decode


---

🧾 Help Menu

python3 burl.py -h

USAGE:  python3 burl.py -p [payload] -m [encode/decode] -n [optional] 
where:
    -p  Specifies the payload to be encoded or decoded.
    -m  Specifies the mode. Either encode or decode.
    -n  Specifies the number of times to encode or decode. Default is 1.
         But in the case of decoding, if omitted, full decode will be applied.


---

💡 Tip

If you omit -p or -m, the tool will prompt you interactively using pyinputplus.


---

📄 License

MIT — free to use, modify, and share.

