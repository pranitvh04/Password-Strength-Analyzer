# 🔐 Password Strength Analyzer

A simple Python script to evaluate the strength of a password based on its structure and resistance to common weak patterns. Ideal for beginners learning Python and foundational cybersecurity concepts.

---

## 🔧 Features

- Evaluates password strength as **Weak**, **Medium**, or **Strong**
- Checks for:
  - ✅ Minimum length (8 characters)
  - ✅ Uppercase **and** lowercase letters
  - ✅ Digits
  - ✅ Symbols
  - ✅ Avoidance of common weak patterns (e.g., `123`, `password`, etc.)

---

## 🧪 Example Usage

```bash
$ python password_checker.py
Enter your password: Hello123!

Password Analysis:
Strength: Medium ⚠️
Issues:
- No symbol


💡 How It Works
The script scores a password based on five key criteria:
✅ Sufficient length (≥ 8 characters)
✅ Contains both uppercase and lowercase letters
✅ Includes digits
✅ Includes at least one symbol (e.g., !@#$)
✅ Avoids common weak patterns (like 123, password, qwerty, etc.)

Strong: Meets 4 or more criteria and avoids weak patterns
Medium: Meets 3 criteria or has minor issues
Weak: Fails to meet 3 or more criteria

...

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/yourusername/password-strength-analyzer.git
cd password-strength-analyzer

2. Run the Script
python password_checker.py


📁 File Structure
password-strength-analyzer/
├── password_checker.py
└── README.md
