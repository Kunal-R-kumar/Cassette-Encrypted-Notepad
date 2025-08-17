# 🎵 Cassette – Encrypted Notepad Application

**Cassette** is a secure and modern **GUI-based notepad application** built with Python (Tkinter) that provides **user authentication, encrypted note storage, and file management**.  
It ensures that personal notes remain private and accessible only to the rightful user.

---

## ✨ Features

- **User Authentication**
  - Signup and Login with password validation
  - Passwords securely encoded and stored in local files
- **Encrypted Notes**
  - Traditional encryption/decryption ensures secure text storage
  - Notes are unreadable outside the application
- **File Management**
  - Create, open, edit, save, and delete diary/note files
  - Organized per-user in a dedicated directory
- **Modern GUI**
  - Full-screen, responsive Tkinter interface
  - Backgrounds, buttons, and calendar integration for DOB
- **Keyboard Shortcuts**
  - `Alt+S` → Save file  
  - `Alt+M` → Return to Menu  
  - `Alt+A` → About section  
  - `Alt+D` → Delete file  
  - `Alt+X` → Quit application  

---

## 🔐 Security

- Usernames and passwords are stored in an **encoded CSV file**.  
- Notes are encrypted before saving and automatically decrypted when opened.  
- Each user has a **dedicated folder** for their notes, ensuring privacy.

---

## 🛠️ Tech Stack

- **Language**: Python  
- **Libraries/Modules**:  
  - `tkinter` – GUI  
  - `tkcalendar` – Calendar for DOB selection  
  - `csv` – Data storage  
  - `os` – File management  
  - `subprocess` – Running other modules  
  - `random` – Generating unique keys  
  - `pillow (PIL)` – Image handling  

---

## 📦 Modules Required

Make sure you have the following modules installed:  

```bash
pip install pillow tkcalendar
```

## Run the App
```bash
python Cassettenwusr.py 
```
---

# Author

_**Developed by Kunal R Kumar
📧 kkumar021104@gmail.com**_
