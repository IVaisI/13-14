from functions_for_work import *
import re
def f1(array_palindromes, user_id, task_done):
    global message
    print(f"Пользователь {user_id}: Выберите тип ввода:\n1. Ввод текста с клавиатуры\n2. Случайная генерация")
    type_input = input()
    if is_int(type_input):
        type_input = int(type_input)
    if type_input == 1:
        message = input_text(user_id)
        print(f"Пользователь {user_id}: Вы ввели следующий текст: {message} ")
    elif type_input == 2:
        message = random_text(user_id)
        print(f"Пользователь {user_id}: Сгенерированный текст: {message}")
    else:
        print('error')
    task_done.set()
    return True
def f2(array_palindromes, user_id, task_done):
    text = message.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    palindromes = []
    # Проверка слова на палиндром
    for word in words:
        if word == word[::-1]:
            palindromes.append(word)
    print(f"Пользователь {user_id}: Алгоритм выполнен\n")
    array_palindromes.extend(palindromes)
    task_done.set()
def f3(array_palindromes, user_id, task_done):
    if len(array_palindromes) == 0:
        print(f"Пользователь {user_id}: Палиндромов в тексте нет")
    else:
        print(f"Пользователь {user_id}: Список палиндромов: ")
        for i in array_palindromes:
            print(i)
    task_done.set()