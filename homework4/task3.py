import sys


def my_precious_logger(text: str) -> str:
    (sys.stderr if text.lower().startswith("error") else sys.stdout).write(text)
    return text
