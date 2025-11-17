import re

BLACKLIST_URLS = [r"buy", r"malicious"]
PROFANITY = [r"\b(stupid|worthless|idiot)\b"]
THREATS = [r"i will hurt", r"i will kill", r"i will find"]

def apply_rules(text: str):
    t = text.lower()

    for p in THREATS:
        if re.search(p, t):
            return {"action": "remove", "reason": "threat_detected"}

    for p in PROFANITY:
        if re.search(p, t):
            return {"action": "warn", "reason": "profanity_detected"}

    for u in BLACKLIST_URLS:
        if re.search(u, t):
            return {"action": "escalate", "reason": "suspicious_url"}

    return None
