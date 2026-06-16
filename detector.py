from collections import Counter
from datetime import datetime

HIGH_THRESHOLD = 7
MEDIUM_THRESHOLD = 5
LOW_THRESHOLD = 3

ip_counts = Counter()

with open("auth.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()

            if "from" in parts:
                ip = parts[parts.index("from") + 1]
                ip_counts[ip] += 1

print(f"\nScan Time: {datetime.now()}")

print("\n===== SSH BRUTE-FORCE DETECTOR =====\n")

for ip, attempts in ip_counts.items():

    if attempts >= HIGH_THRESHOLD:
        print(f"[ALERT] {ip} → {attempts} attempts → HIGH 🔴")

    elif attempts >= MEDIUM_THRESHOLD:
        print(f"[WARNING] {ip} → {attempts} attempts → MEDIUM 🟠")

    elif attempts >= LOW_THRESHOLD:
        print(f"[NOTICE] {ip} → {attempts} attempts → LOW 🟡")

total_attempts = sum(ip_counts.values())

highest_ip = max(ip_counts, key=ip_counts.get)
highest_attempts = ip_counts[highest_ip]

print("\n===== SUMMARY =====")
print(f"Total Failed Logins: {total_attempts}")
print(f"Total Suspicious IPs: {len(ip_counts)}")
print(f"Highest Offender: {highest_ip} ({highest_attempts} attempts)")

with open("report.txt", "w") as report:
    report.write("SSH BRUTE-FORCE DETECTION REPORT\n")
    report.write("=" * 35 + "\n\n")

    for ip, attempts in ip_counts.items():
        report.write(f"{ip} - {attempts} failed attempts\n")

    report.write(f"\nTotal Failed Logins: {total_attempts}")
    report.write(f"\nTotal Suspicious IPs: {len(ip_counts)}")
    report.write(f"\nHighest Offender: {highest_ip} ({highest_attempts} attempts)")
