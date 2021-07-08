import sys


def my_precious_logger(text: str):
    if text.lower().startswith("error"):
        sys.stderr.write(text)
        return text
    else:
        sys.stdout.write(text)
        return text
