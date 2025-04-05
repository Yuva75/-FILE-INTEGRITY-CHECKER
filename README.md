# -FILE-INTEGRITY-CHECKER

COMPANY: CODTECH IT SOLUTIONS 

NAME: Yuvaraj C 

INTERN ID: CT04WX96

DOMAIN: CYBERSECURITY

DURATION: 4 WEEEKS 

MENTOR: NEELA SANTOSH 

Description of this Task

A File Integrity Checker is a tool designed to verify whether files have been altered, tampered with, or corrupted over time. It works by generating and comparing cryptographic hash values (such as SHA-256) of files. In Python, this can be implemented efficiently using built-in libraries like hashlib and os. This tool is especially useful in cybersecurity, software deployment, and data backup validation, where maintaining the authenticity and integrity of files is crucial.
The primary concept behind the file integrity checker is the use of hash functions. A hash function takes an input (or 'message') and returns a fixed-size string of bytes. Even a tiny change in the file will produce a completely different hash, making this method highly reliable for detecting modifications

How It Works:

The script calculates the initial SHA-256 hash of each file.
It then enters a loop (default: every 5 seconds), recalculating and comparing hashes.
If a file’s hash has changed, or if a file has been removed, a warning is printed and logged.
The tool keeps updating the stored hashes if files are modified.

Use Cases:

Security and forensic analysis
Monitoring sensitive config/log files
Validating file integrity for backups or critical documents
Classroom/demonstration tool for cryptographic file monitoring

Python-based File Integrity Checker is lightweight, cross-platform, and easy to use, making it a great addition to any developer or system administrator’s toolkit. It not only promotes data security but also helps in early detection of potential security breaches or system failures.

Output

![Image](https://github.com/user-attachments/assets/223a9881-6d30-476e-94d9-336481d35c83)
