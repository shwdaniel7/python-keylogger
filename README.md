<p align="center">
  <img src="https://i.imgur.com/MQqpAwP.gif" width="450" alt="Yuki Nagato typing">
</p>

<h1 align="center">Educational Python Keylogger</h1>

<p align="center">
  A simple Python project demonstrating keyboard event capture, TCP socket communication and multithreading.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Purpose-Educational-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/shwdaniel7/python-keylogger?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/shwdaniel7/python-keylogger?style=for-the-badge">
  <img src="https://img.shields.io/github/repo-size/shwdaniel7/python-keylogger?style=for-the-badge">
</p>

<p align="center">
  made by <strong>arneb</strong> • <a href="https://github.com/shwdaniel7">@shwdaniel7</a>
</p>

---

> [!WARNING]
> This repository was created **exclusively for educational purposes**.
>
> The goal of this project is to demonstrate how keyboard event capture, TCP socket communication and multithreading work in Python.
>
> This project **is not intended for malicious use** and was intentionally developed without persistence, stealth techniques, privilege escalation, antivirus evasion or any functionality commonly associated with real-world malware.
>
> Please use this project only on systems you own or have explicit authorization to test.

---

# 📖 About

This repository was created while studying **Python** and **Cybersecurity**.

Instead of replicating real-world malware, this project focuses on explaining the internal logic behind a basic keylogger using clean and readable code.

The objective is to better understand how keyboard monitoring works and how defensive solutions can identify this type of behavior.

---

# ✨ Features

* ⌨️ Keyboard event capture
* 🕒 Timestamp logging
* 🔌 TCP socket communication
* 🧵 Multithreaded architecture
* 📄 Temporary log storage
* 🌐 Basic HTTP response for local visualization

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

# 🔄 Workflow

```text
Keyboard
    │
    ▼
keylogger.py
    │
    ├── Save event to temporary file
    │
    └── Send event via TCP socket
               │
               ▼
          server.py
               │
               ▼
      Temporary Log File
               │
               ▼
   Local HTTP GET response (optional)
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/shwdaniel7/python-keylogger.git
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

# 🛡️ Limitations

This project intentionally **does not** implement techniques commonly found in real-world malware.

* Localhost communication only (`127.0.0.1`)
* No persistence
* No process injection
* No privilege escalation
* No stealth techniques
* No antivirus evasion
* No obfuscation
* No encryption
* No remote C2 server
* No external data exfiltration

These limitations are intentional and keep the project focused on learning and transparency.

---

# 📚 Technologies

* Python 3
* keyboard
* socket
* threading
* tempfile
* datetime

---

# ⚖️ Legal Notice

Running keyloggers against systems or users without explicit authorization may violate local laws.

This repository is provided exclusively for educational and research purposes.

The author assumes no responsibility for any misuse of this software.

---

<p align="center">
  <b>made by arneb</b>
</p>
