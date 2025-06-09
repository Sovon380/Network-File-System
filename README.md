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

nfs_web_ui/
│
├── nfs_web.py # Main Flask Application
├── users.json # User Database (hashed passwords)
├── activity.log # Activity Log File
├── shared_files/ # Per-user file storage folders
│
├── templates/ # HTML Templates (Bootstrap Styled)
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── view_shares.html
│ ├── upload.html
│ ├── change_password.html
│ └── admin.html
│
├── requirements.txt # Python dependencies
└── .gitignore # Git Ignore File

