import unicodedata
from collections import Counter
from typing import List


def get_longest_diverse_words(file_path: str, encoding="utf8") -> List[str]:
    with open(file_path, encoding=encoding) as input_file:
        words = set(input_file.read().split())
        words = [word.strip(".,;:!?[]()") for word in words]
        d = {word: len(set(word)) for word in words}
        result_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        return list(result_dict.keys())[:10]


def get_rarest_char(file_path: str, encoding="utf8") -> str:
    with open(file_path, encoding=encoding) as input_file:
        data = input_file.read()
        c = Counter(data)
        res = c.most_common()[:-10:-1]
        return res[0][0]


def count_punctuation_chars(file_path: str, encoding="utf8") -> int:
    with open(file_path, encoding=encoding) as input_file:
        count = Counter(
            char
            for line in input_file
            for char in line
            if unicodedata.category(char) == "Po"
        )
        return sum(count.values())


def count_non_ascii_chars(file_path: str, encoding="utf8") -> int:
    with open(file_path, encoding=encoding) as input_file:
        non_ascii_list = []
        while char := input_file.read(1):
            if ord(char) > 127:
                non_ascii_list.append(char)
        result = sum(Counter(non_ascii_list).values())
        return result


def get_most_common_non_ascii_char(file_path: str, encoding="utf8") -> str:
    with open(file_path, encoding=encoding) as input_file:
        non_ascii_list = []
        while char := input_file.read(1):
            if ord(char) > 127:
                non_ascii_list.append(char)
        result = Counter(non_ascii_list).most_common()
        return result[0][0]
