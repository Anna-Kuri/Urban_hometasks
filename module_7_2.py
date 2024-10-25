def custom_write(file_name: str, strings: list) -> dict:
    strings_position = {}
    file = open(file_name, 'a', encoding='utf-8')
    for i, string in enumerate(strings, start=1):
        byte_number = file.tell()
        file.write(string + '\n')
        strings_position[(i,byte_number)] = string
    return strings_position
    file.close()

info = [
'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


