import csv

rows = [
    ("New ransomware called XCrypt is spreading", "threat"),
    ("Phishing email pretending to be Microsoft login", "threat"),
    ("Suspicious URL found http://malicious.example", "threat"),
    ("C2 server located at 192.168.1.50", "threat"),
    ("Just chilling and talking about games", "normal"),
    ("Had lunch with friends today!", "normal"),
]

with open("data/threat_small.csv", "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["text", "label"])
    w.writerows(rows)

print("Created data/threat_small.csv")
