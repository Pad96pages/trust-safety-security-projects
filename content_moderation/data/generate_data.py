import csv

rows = [
    ("I love your post!", "allow"),
    ("You're stupid and worthless", "remove"),
    ("Thanks for sharing this", "allow"),
    ("Buy followers cheap http://buy.example", "escalate"),
    ("I will hurt you badly", "remove"),
    ("Check this link http://malicious.example", "escalate"),
]

with open("data/moderation_small.csv", "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["text", "label"])
    w.writerows(rows)

print("Dataset created: data/moderation_small.csv")
