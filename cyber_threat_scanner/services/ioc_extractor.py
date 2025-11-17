import re

URL_RE = re.compile(r'https?://\S+')
IP_RE = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
HASH_RE = re.compile(r'\b[a-fA-F0-9]{32,64}\b')

def extract_iocs(text: str):
    return {
        "urls": URL_RE.findall(text),
        "ips": IP_RE.findall(text),
        "hashes": HASH_RE.findall(text)
    }
