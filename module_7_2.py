def custom_write(file_name, strings):
    strings_positions = {}

    for i, string in enumerate (strings):
        opened_file = open(file_name, 'a', encoding = 'utf-8')
        string_byte = opened_file.tell()
        strings_positions[(i, string_byte)] = strings
        opened_file.write(f'{string}\n')
        opened_file.close()
    return strings_positions

info = ['Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



