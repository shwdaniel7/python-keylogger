# Python Keylogger (Educational Project)

> **⚠️ Educational Purpose Only**
>
> This repository was created exclusively for educational purposes in order to study Python programming, sockets, multithreading and basic Cybersecurity concepts.
>
> This project **is not intended for malicious use** and should only be executed in controlled environments or on machines that you own.

---

## 📖 About

This project demonstrates, in a simplified way, how a keylogger works internally.

It was developed to practice:

- Python
- Multithreading
- TCP Socket Programming
- Keyboard Event Capture
- Local Client-Server Communication

The implementation intentionally avoids techniques commonly found in real malware, making it easier to understand and analyze.

---

## ⚙️ How it works

The project consists of three modules.

### `main.py`

Responsible for starting the application.

It:

- Starts the TCP server in a background thread;
- Waits for the server to initialize;
- Starts the keyboard logger.

---

### `keylogger.py`

Responsible for monitoring keyboard events.

For every pressed key, it:

1. Detects the key using the `keyboard` library;
2. Gets the current timestamp;
3. Stores the event inside a temporary file;
4. Sends the information to the local TCP server.

---

### `server.py`

Receives messages sent by the keylogger.

The server:

- Accepts TCP connections on `127.0.0.1:5000`;
- Stores received events;
- Responds to simple HTTP GET requests, allowing anyone to build their own frontend or consume the logs using a browser or any HTTP client.

---

## 📊 Application Flow

```text
Keyboard
    │
    ▼
keylogger.py
    │
    ├── Save to temporary file
    │
    └── Send via TCP Socket
               │
               ▼
          server.py
               │
               ▼
 Temporary Log File
               │
               ▼
 Browser / Live Server
```

---

## 📁 Project Structure

```text
.
├── main.py
├── keylogger.py
├── server.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/python-keylogger.git
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the project.

```bash
python main.py
```

The local server will be available at:

```
http://127.0.0.1:5000
```

---

## ⚠️ Limitations

This project is intentionally simple and **does not represent a real-world malware**.

Some intentional limitations include:

- Localhost communication only (`127.0.0.1`);
- No persistence mechanism;
- No stealth techniques;
- No antivirus evasion;
- No privilege escalation;
- No remote command execution;
- No external data exfiltration;
- Temporary local storage only.

These limitations exist to keep the project educational and easy to understand.

---

## 📚 Technologies

- Python 3
- keyboard
- socket
- threading
- tempfile
- datetime

---

## ⚖️ Legal Notice

This project was created exclusively for educational and research purposes.

Running keyloggers on systems or devices without explicit authorization may violate local laws.

The author is **not responsible** for any misuse of this code.