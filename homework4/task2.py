from collections import Counter

import requests


def process_response(url: str) -> int:
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException:
        raise ValueError(f"Unreachable {url}")
    text = r.content.decode("utf-8")
    count = Counter(i for line in text for i in line if i == "i")
    return count["i"]
