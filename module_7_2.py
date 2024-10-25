def custom_write(file_name: str, strings: list[str]) -> dict:
    strings_position = {}

    file = open(file_name, "a", encoding="utf-8")

    for i, string in enumerate(strings, start=1):
        byte_number = file.tell()
        file.write(f"string\n")
        strings_position[(i, byte_number)] = string

    file.close()

    return strings_position


info = [
    "Text for tell.",
    "Используйте кодировку utf-8.",
    "Because there are 2 languages!",
    "Спасибо!",
]

result = custom_write("test.txt", info)

for elem in result.items():
    print(elem)
