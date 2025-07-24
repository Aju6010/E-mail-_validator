# 📧 Email Validator App

A simple and user-friendly web app built with **Streamlit** to validate email addresses using Python's `email-validator` library.

🔗 **Live App:**  
[https://e-mail-validator-2sga8a69ujyvknbdh2rnih.streamlit.app/](https://e-mail-validator-2sga8a69ujyvknbdh2rnih.streamlit.app/)

---

## ✨ Features

- ✅ Validates email address syntax
- 🌐 Supports domain checking
- 🚫 Flags invalid characters, spaces, or malformed inputs
- 📋 Displays clean success and error messages

---

## 🚀 Getting Started

### 📥 Clone the repository

```bash
git clone https://github.com/your-username/email-validator-app.git
cd email-validator-app
```

### 📦 Install dependencies

Make sure you have Python 3.7+ installed, then run:

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install manually:
```bash
pip install streamlit email-validator
```

### ▶️ Run the app locally

```bash
streamlit run email_validator_app.py
```

---

## 🖼️ App Preview

_(Insert a screenshot if available)_

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) – UI framework for building data web apps
- [email-validator](https://pypi.org/project/email-validator/) – Library for email validation

---

## 📁 File Structure

```
email-validator-app/
│
├── email_validator_app.py     # Main Streamlit application
├── requirements.txt           # List of Python packages
└── README.md                  # Project documentation
```

---

## 🙋‍♂️ How It Works

- User inputs an email address into the form.
- The app checks:
  - Syntax (e.g., missing `@`, invalid characters)
  - Valid domain formatting
- Returns either ✅ Valid or ❌ Error with reason.

---

## 📬 Example Emails to Try

| Email                        | Result            |
|-----------------------------|-------------------|
| `test@example.com`          | ✅ Valid          |
| `plainaddress`              | ❌ Missing '@'    |
| `user name@example.com`     | ❌ Contains space |
| `name@xn--d1acufc.xn--p1ai` | ✅ Valid (Unicode)|
| `username@.com`             | ❌ Invalid domain |

---

## 📢 Share With Friends

Anyone can test email validity by visiting the live app link:  
🔗 [https://e-mail-validator-2sga8a69ujyvknbdh2rnih.streamlit.app/](https://e-mail-validator-2sga8a69ujyvknbdh2rnih.streamlit.app/)

---

## 📃 License

This project is licensed under the MIT License.
