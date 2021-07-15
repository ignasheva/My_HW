from typing import Dict, Iterable, List
from unicodedata import category


def my_counter(data: Iterable) -> Dict:
    dictionary = {}
    for item in data:
        dictionary[item] = dictionary.get(item, 0) + 1
    return dictionary


def read_from_file(file_path: str, encoding="utf8") -> str:
    input_file = open(file_path, encoding=encoding)
    data = input_file.read()
    input_file.close()
    return data


def get_longest_diverse_words(file_path: str, encoding="utf8") -> List[str]:
    words = set(read_from_file(file_path, encoding).split())
    words = [word.strip(".,;:!?[]()") for word in words]
    d = {word: len(set(word)) for word in words}
    result_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return list(result_dict.keys())[:10]


def get_rarest_char(file_path: str, encoding="utf8") -> str:
    data = read_from_file(file_path, encoding)
    c = my_counter(data)
    rarest_char = [key for key in dict([min(c.items(), key=lambda k_v: k_v[1])])]
    return rarest_char[0]


def count_punctuation_chars(file_path: str, encoding="utf8") -> int:
    data = read_from_file(file_path, encoding)
    print(data)
    count = my_counter(char for line in data for char in line if category(char) == "Po")
    return sum(count.values())


def count_non_ascii_chars(file_path: str, encoding="utf8") -> int:
    data = read_from_file(file_path, encoding)
    non_ascii_list = []
    for char in data:
        if ord(char) > 127:
            non_ascii_list.append(char)
    result = sum(my_counter(non_ascii_list).values())
    return result


def get_most_common_non_ascii_char(file_path: str, encoding="utf8") -> str:
    data = read_from_file(file_path, encoding)
    non_ascii_list = []
    for char in data:
        if ord(char) > 127:
            non_ascii_list.append(char)
    counter = my_counter(non_ascii_list)
    result = [key for key in dict([max(counter.items(), key=lambda k_v: k_v[1])])]
    return result[0]
