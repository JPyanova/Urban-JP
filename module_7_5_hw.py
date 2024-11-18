import os
import time

main_path = os.getcwd()

for root, dirs, files in os.walk('.'):
    root = root[2:]
    for file in files:
        if os.path.isfile(file):
            file_path = os.path.join(main_path, root, file)
            file_time = os.path.getmtime(file)
            formatted_time = time.ctime(file_time)
            file_size = os.stat(file).st_size
            parent_dir = os.path.dirname(file_path)
            print(f'''Обнаружен файл: {file}'
                  Путь: {file_path}
                  Размер: {file_size} байт
                  Время изменения: {formatted_time}
                  Родительская директория: {parent_dir}''')