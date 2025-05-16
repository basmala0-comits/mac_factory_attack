# mac_factory_attack
🔍 Project Overview
This project demonstrates:
✅ Why MD5 (secret + message) is vulnerable to length extension attacks
✅ How HMAC-MD5 secures against such attacks
✅ Practical exploitation using a Python-based client

Perfect for learning cryptographic weaknesses and secure implementations!

⚙️ Prerequisites
Before running, ensure you have:

Python 3.6+ (python --version)

Basic terminal knowledge

🚀 Setup & Installation
No dependencies needed!
(Uses built-in Python modules: hashlib, hmac)

🖥️ Running the Servers
Open three separate terminal windows.

1️⃣ Vulnerable Server
File: server.py
Purpose: Demonstrates an insecure MD5(secret + message) implementation.

Steps:

bash
cd folder path
python server.py
When prompted, enter:

SECRET_KEY (e.g., mysecret)

Original message (e.g., user=alice)

Output:

Original MAC: d41d8cd98f00b204e9800998ecf8427e
(Note this MAC for the attack!)

2️⃣ Secure Server
File: secureserver.py
Purpose: Uses HMAC-MD5 to block attacks.

Steps:

bash
cd file path
python secureserver.py
Enter the same SECRET_KEY and message as above.

Output:

Original HMAC: 913d8e8f8d8c8b8a8988878685848382
(This will reject forged messages.)

💥 Performing the Attack
File: client.py
Purpose: Exploits the vulnerable server.

Steps:

Run the client:

bash
cd folder path
python client.py
Enter the following (from the vulnerable server’s output):

Original message (user=alice)

Original MAC (d41d8cd9...)

Secret length (8 for mysecret)

Data to append (&admin=true)

Output:

Forged message: user=alice\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\x00\x00\x00\x00\x00\x00\x00&admin=true
Forged MAC: a1b2c3d4ecd0e0f08eab7690d2a6ee69
Attack SUCCEEDED ✅
📊 Expected Output & Analysis
Server	Legitimate Message	Forged Message	Result
Vulnerable (MD5)	✅ Accepted	✅ Accepted (BAD!)	Attack works
Secure (HMAC)	✅ Accepted	❌ Rejected (GOOD!)	Attack blocked
Why?

The vulnerable server trusts any message with a valid MAC, even if extended.

The secure server detects tampering due to HMAC’s cryptographic structure.

🔐 Security Comparison
Aspect	Vulnerable MD5	Secure HMAC-MD5
Construction	MD5(secret + message)	HMAC(key, message)
Length Extension	❌ Vulnerable	✅ Resistant
Secret Exposure	❌ Leaks via padding	✅ No leakage
Use Case	❌ Never use!	✅ Recommended
🎯 Key Takeaways
Never use MD5(secret + message) – it’s trivially breakable.

Always use HMAC (or modern alternatives like SHA-256-HMAC).

Secret length matters – shorter secrets are easier to attack.

Real-world impact: Many APIs and systems were hacked this way!

📜 License
MIT License - Free for learning and experimentation.

🚀 Happy Hacking!
