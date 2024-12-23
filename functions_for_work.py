import random
import time
def is_int(choice):
    """ Проверка на то, что s - целое число для меню"""
    try:
        if type(choice) is int:
            return True
        if choice is None:
            return False
        if not choice.isdecimal():
            return False
        int(choice)
        return True
    except (Exception, ValueError, TypeError):
        return False
def input_text(user_id):
    print(f"Пользователь {user_id}: Начало ввода текста...")
    time.sleep(2)  # Имитация длительного ввода
    text = input(f"Пользователь {user_id}: Введите текст для обработки (для завершения ввода нажмите клавишу Enter): ")
    while True:
        line = input()
        if line == "":
            break
        text += " " + line
    return text
def random_text(user_id):
    print(f"Пользователь {user_id}: Начало генерации случайного текста...")
    time.sleep(2)  # Имитация длительного ввода
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ' + ' ' * 7
    length = random.randint(20, 100)  # Генерация случайной длины
    return ''.join(random.choice(letters) for _ in range(length))