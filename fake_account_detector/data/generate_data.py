import csv
import random

rows = []
for i in range(200):
    username = f"user{i}"

    # Simulated stats
    followers = random.randint(0, 5000)
    friends = random.randint(0, 8000)
    statuses = random.randint(0, 2000)

    # Simple rule to generate bots:
    # low followers + very high following → suspicious
    if followers < 50 and friends > 2000:
        label = 1   # bot
    else:
        label = random.choice([0, 1])

    rows.append([username, followers, friends, statuses, label])

with open("data/accounts_small.csv", "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["username", "followers", "friends", "statuses", "label"])
    w.writerows(rows)

print("Dataset created at data/accounts_small.csv")
