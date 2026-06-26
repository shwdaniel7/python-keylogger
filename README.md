````md
<p align="center">
  <img src="https://i.imgur.com/MQqpAwP.gif" width="500" alt="Yuki Nagato typing">
</p>

<h1 align="center">Python Keylogger</h1>

<p align="center">
  <strong>Educational Cybersecurity Project</strong>
</p>

<p align="center">
  Demonstrating keyboard event capture, TCP sockets and multithreading in Python.
</p>

<p align="center">
  <sub>Made by <strong>Arneb</strong> • <a href="https://github.com/shwdaniel7">@shwdaniel7</a></sub>
</p>

---

> [!WARNING]
> This repository was created **exclusively for educational purposes**.
>
> Its purpose is to demonstrate how keyboard event capture, TCP socket communication and multithreading work in Python.
>
> It is **not intended for malicious use** and should only be executed on systems you own or have explicit authorization to test.

---

# 📖 About

This project was developed while studying Python and Cybersecurity.

The objective is to demonstrate, in a simplified and transparent way, how a basic keylogger works internally. The implementation intentionally avoids persistence, stealth techniques, privilege escalation, antivirus evasion, obfuscation, or any other capabilities commonly associated with real-world malware.

This repository is intended as a learning resource for understanding both offensive security concepts and the defensive mechanisms used to detect them.

---

# ✨ Features

- Keyboard event capture
- Timestamp logging
- TCP socket communication
- Multithreaded execution
- Temporary log storage
- Simple HTTP response for local visualization

---

# 📂 Project Structure

```text
.
├── main.py
├── keylogger.py
├── server.py
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```

---

# ⚙️ Workflow

```text
Keyboard
    │
    ▼
keylogger.py
    │
    ├── Store event locally
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
    HTTP GET Response (optional)
```

---

# 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/shwdaniel7/python-keylogger.git
```

Install the dependency.

```bash
pip install -r requirements.txt
```

Run the project.

```bash
python main.py
```

---

# 📚 Technologies

- Python 3
- keyboard
- socket
- threading
- tempfile
- datetime

---

# ⚠️ Limitations

This project intentionally **does not** implement techniques commonly found in real-world malware.

- Localhost communication only (`127.0.0.1`)
- No persistence
- No privilege escalation
- No process injection
- No stealth techniques
- No antivirus evasion
- No obfuscation
- No encryption
- No remote C2 server
- No external data exfiltration

These limitations exist to keep the source code understandable, safe to study and focused on educational purposes.

---

# ⚖️ Legal Notice

Running keyloggers against systems or users without explicit authorization may violate local laws.

This repository is provided exclusively for educational and research purposes.

The author assumes no responsibility for any misuse of this software.

---

<p align="center">
  <strong>Made by arneb</strong><br>
  <a href="https://github.com/shwdaniel7">github.com/shwdaniel7</a>
</p>
````
