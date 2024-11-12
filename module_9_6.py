from typing import Iterator


def all_variants(text):
    for size in range(1, len(text) + 1):
        for i in range(len(text) - size + 1):
            yield text[i : i + size]


a = all_variants("abc")

for i in a:
    print(i)

