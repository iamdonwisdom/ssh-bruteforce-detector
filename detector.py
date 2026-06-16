
from collections import Counter

ip_counts = Counter()

with open("auth.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()

            if "from" in parts:
                ip = parts[parts.index("from") + 1]
                ip_counts[ip] += 1

print("\n===== SSH BRUTE-FORCE DETECTOR =====\n")

for ip, attempts in ip_counts.items():

    if attempts >= 5:
        print(f"[ALERT] {ip} → {attempts} attempts → HIGH 🔴")

    elif attempts >= 3:
        print(f"[WARNING] {ip} → {attempts} attempts → MEDIUM 🟠")

print("\n===== SUMMARY =====")
print(f"Total suspicious IPs: {len(ip_counts)}")

from collections import Counter

print("""
====================================
     SSH BRUTE-FORCE DETECTOR
====================================
""")

ip_counts = Counter()
total_attempts = sum(ip_counts.values())

print("\n===== SUMMARY =====")
print(f"Total failed logins: {total_attempts}")
print(f"Total suspicious IPs: {len(ip_counts)}")
