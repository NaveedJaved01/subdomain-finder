# Subdomain Finder 🔎
A beginner-friendly Python-based Subdomain Enumeration Tool designed to discover subdomains using DNS lookups and a custom wordlist.
This project is developed for educational purposes and bug bounty reconnaissance practice.

## 🚀 Features
- Discover subdomains using a wordlist.
- Perform DNS A-record lookups.
- Identify resolved IP addresses.
- Check HTTP and HTTPS availability.
- Display HTTP status codes.
- Save discovered subdomains automatically.
- Generate a simple scan summary.

## 🛠️ Technologies Used
- Python 3
- DNSPython
- Requests Library
- Kali Linux
- Git & GitHub

## 📁 Project Structure
```text
subdomain-finder/
│
├── subdomain_finder.py
├── subdomains.txt
├── requirements.txt
├── README.md
│
└── results/
    └── subdomains_found.txt
```

## ⚙️ Installation
### Step 1: Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Enter the project directory
```bash
cd subdomain-finder
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Give execution permission

```bash
chmod +x subdomain_finder.py
```

## ▶️ Usage

Run the tool with:

```bash
python3 subdomain_finder.py -d example.com
```
Or:
```bash
./subdomain_finder.py -d example.com
```

### Use a custom wordlist
```bash
python3 subdomain_finder.py -d example.com -w subdomains.txt
```
Replace `example.com` with a domain you own or have explicit permission to assess.

## 📊 Example Output
```text
========================================
          SUBDOMAIN FINDER
========================================

[+] Target Domain: example.com
[+] Starting DNS enumeration...

[+] Found: www.example.com -> 93.184.216.34
[+] Found: mail.example.com -> 93.184.216.34

========== SCAN SUMMARY ==========

[+] Total discovered: 2

[+] Results saved to results/subdomains_found.txt
```
*Note: This is illustrative output. Actual results depend on DNS records.*

## 📄 Results
The tool automatically creates:
`results/subdomains_found.txt`
This file contains discovered subdomains and their resolved IP addresses.

## 🎯 Learning Objectives
- Understand DNS and DNS resolution.
- Learn subdomain enumeration.
- Practice reconnaissance techniques.
- Understand HTTP and HTTPS.
- Develop Python automation skills.
- Learn basic bug bounty methodologies.

## 🔐 Bug Bounty Learning
Subdomain enumeration is an important initial reconnaissance activity in web security assessments.
Discovered subdomains can help researchers understand an organization's public-facing attack surface. Discovery alone does not establish a vulnerability.

## ⚠️ Disclaimer
This tool is developed strictly for educational and authorized security testing.
- Only enumerate domains you own or have permission to assess.
- Follow bug bounty program scope and rules.
- Do not perform unauthorized security testing.
- Respect rate limits and program policies.
- Always verify findings before reporting.
The developer is not responsible for misuse of this tool.

## 👨‍💻 Author
Cybersecurity & Bug Bounty Learner

**Skills:** Python | Networking | DNS | Web Security | Ethical Hacking
---
⭐ If you find this project useful, give the repository a star on GitHub!