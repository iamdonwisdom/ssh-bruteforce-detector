
from collections import Counter
from collections import Counter
ip_counts = Counter()

with open("auth.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()

            if "from" in parts:
                ip = parts[parts.index("from") + 1]
                ip_counts[ip] +=1
print(f"Scan Time: {datetime.now()}")
print("\n===== SSH BRUTE-FORCE DETECTOR =====\n")

for ip, attempts in ip_counts.items():

if attempts >= HIGH_THRESHOLD:
    print(f"[ALERT] {ip} → {attempts} attempts → HIGH 🔴")

elif attempts >= MEDIUM_THRESHOLD:
    print(f"[WARNING] {ip} → {attempts} attempts → MEDIUM 🟠")

elif attempts >= LOW_THRESHOLD:
    print(f"[NOTICE] {ip} → {attempts} attempts → LOW 🟡")

print("\n===== SUMMARY =====")
print(f"Total suspicious IPs: {len(ip_counts)}")

from collections import Counter

print("""
====================================
     SSH BRUTE-FORCE DETECTOR
====================================
""")
HIGH_THRESHOLD = 7
MEDIUM_THRESHOLD = 5
LOW_THRESHOLD = 3

ip_counts = Counter()
total_attempts = sum(ip_counts.values())

total_attempts = sum(ip_counts.values())

highest_ip = max(ip_counts, key=ip_counts.get)
highest_attempts = ip_counts[highest_ip]

print("\n===== SUMMARY =====")
print(f"Total Failed Logins: {total_attempts}")
print(f"Total Suspicious IPs: {len(ip_counts)}")
print(f"Highest Offender: {highest_ip} ({highest_attempts} attempts)")
