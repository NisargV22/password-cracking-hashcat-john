# 🔐 Password Cracking with Hashcat & John the Ripper (SHA-256)

This is a **demo project** that cracks a SHA-256 password hash using:
- [Hashcat](https://hashcat.net/hashcat/) (GPU/CPU)
- [John the Ripper Jumbo](https://www.openwall.com/john/) (CPU)

> ⚠️ **Educational use only.** Do not attack systems you don’t own or have permission to test.

---

## 📂 Project Layout
password-cracking-project/
│-- hashes.txt # Contains the target SHA-256 hash
│-- wordlist.txt # Dictionary with possible passwords
│-- screenshots/ # Screenshots of runs & results
│-- README.md # Project documentation


---

## 📝 Hash & Wordlist Setup
- **Hash used (SHA-256 of `CodeC123`)**  


7cd358c1154b7ede30f733a9f2d83886da2517d7e940ee2ac22d3bc63cc4102a


- **Wordlist (wordlist.txt)**  


CodeC123


---

## ⚡ Cracking with Hashcat
Command:
```bash
hashcat.exe -m 1400 -a 0 hashes.txt wordlist.txt


Example Run:


⚡ Cracking with John the Ripper

Command:

john.exe --format=dynamic_61 --wordlist=wordlist.txt hashes.txt


Example Run:


✅ Results

Both tools successfully cracked the hash:

Hash      : 7cd358c1154b7ede30f733a9f2d83886da2517d7e940ee2ac22d3bc63cc4102a
📸 Screenshots

Screenshots of terminal outputs are stored in the screenshots/ folder:

hashcat_run.png → Hashcat crack output

john_run.png → John the Ripper crack output

result.png → Final cracked password

👤 Author

Vadechiya Nisarg

Project for educational/demo purposes

