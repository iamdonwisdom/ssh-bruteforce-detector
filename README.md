# SSH Brute-Force Detector

A Python-based cybersecurity tool that detects repeated failed SSH login attempts from authentication logs.

## Features

- Detects failed SSH login attempts
- Extracts source IP addresses
- Counts login attempts per IP
- Classifies suspicious activity
- Generates security alerts

## Technologies Used

- Python 3
- Kali Linux

## How It Works

The tool scans an authentication log file and searches for:

Failed password

entries.

It extracts the source IP address, counts failed login attempts, and generates alerts based on suspicious activity.

## Sample Output

```text
===== SSH BRUTE-FORCE DETECTOR =====

[ALERT] 192.168.1.10 → 7 attempts → HIGH 🔴
[WARNING] 10.0.0.5 → 3 attempts → MEDIUM 🟠

===== SUMMARY =====
Total suspicious IPs: 2
```

## Skills Demonstrated

- Log Analysis
- Python Programming
- Threat Detection
- Cybersecurity Monitoring
- SOC Analyst Fundamentals

## Future Improvements

- Real-time monitoring
- Email alerts
- CSV report export
- Dashboard visualization

## Screenshot

![SSH Brute-Force Detector](screenshots/your-screenshot-name.png)
