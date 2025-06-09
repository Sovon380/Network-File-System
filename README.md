# NFS Web UI - Flask Based Network File System Manager

![Python](https://img.shields.io/badge/python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 📖 Overview

**NFS Web UI** is a fully functional web-based file sharing platform developed with Python and Flask.  
It allows multiple users to upload, download, delete, and manage their own files stored in isolated directories.

An integrated Admin Panel enables administrators to monitor users, track file storage, and manage activity logs — perfect for small team file sharing, internal servers, or educational lab setups.

---

## 🔥 Key Features

- 🔐 User Authentication (Registration, Login, Logout)
- 👑 Admin Panel (Admin-only access)
- 🗄️ Per-user private file storage
- 📤 File Upload with secure file handling
- 📥 File Download
- 🗑 File Deletion
- 🔑 Change Password functionality
- 📝 Activity Logs (automatic event tracking)
- 📊 Admin can view user file statistics
- 💻 Bootstrap-based responsive UI

---

## 📁 Project Structure

```bash
nfs_web_ui/
│
├── nfs_web.py              # Main Flask Application
├── users.json              # User Database (hashed passwords)
├── activity.log            # Activity Log File
├── shared_files/           # Per-user file storage folders
│
├── templates/              # HTML Templates (Bootstrap Styled)
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── view_shares.html
│   ├── upload.html
│   ├── change_password.html
│   └── admin.html
│
├── requirements.txt        # Python dependencies
└── .gitignore              # Git Ignore File

```

## ⚙ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sovon380/Network-File-System.git
cd nfs-web-ui
```
### 2️⃣ Setup Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Initialize Admin User
Generate hashed password for admin user:

```bash
python
```
Then inside the Python shell:

```bash
from werkzeug.security import generate_password_hash
import json

users = {"admin": generate_password_hash("your_admin_password_here")}
with open("users.json", "w") as f:
    json.dump(users, f)
exit()
```
## 🚀 Running The Application
Inside your virtual environment:

```bash
python nfs_web.py
```
The application will be available at:
```bash
http://localhost:5000
```
## 🔒 Security Notes
Ensure this app is deployed inside secure networks.

Never expose on public-facing servers without additional security layers.

Consider switching to SQLite or PostgreSQL for production-grade database storage.

Setup HTTPS for secure communication.

## 🏗️ Future Improvements
🔐 Password reset (forgot password)

📦 File size restrictions

🧹 Admin user deletion capability

📂 Global file usage statistics

🐳 Docker deployment

🖥️ Production deployment instructions

## 📜 License
MIT License. Feel free to use and modify for personal or educational projects.

## 🤝 Author
Developed By: Sovon Mallick

Technologies: Python, Flask, Bootstrap, Werkzeug

## 🙏 Special Thanks
To all contributors of Flask and open-source community ❤️
