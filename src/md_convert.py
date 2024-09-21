import markdown
import os


#функция считыввает мд файл и возвращает его в формате строки, на вход принимает
#папку и имя файла
def convert(directory, filename):
    os.listdir(f"../{directory}")
    with open(f'../{directory}/{filename}', 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    return markdown_text 