# os.walk
# os.path.join
# os.path.getmtime
# os.path.dirname
# os.path.getsize
# time
import os, time
directory = "."
print(os.path.abspath(directory))
for root, dirs, files in os.walk(directory, topdown=True, onerror=None, followlinks=False):
    for file in files:
        filepath = os.path.dirname(directory)
        filetime = os.path.getmtime(directory)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(directory)
        parent_dir = os.path.abspath(directory)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')