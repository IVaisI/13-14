from menu_functions import f1, f2, f3
from functions_for_work import is_int
import threading
import queue
# Очередь задач
task_queue = queue.Queue()
def worker():
    while True:
        task = task_queue.get()
        if task is None:
            break
        task()
        task_queue.task_done()
def run_menu(user_id):
    array_palindromes = []  # массив палиндромов
    is_text_input = False
    is_algorithm_done = False
    task_done = threading.Event()
    # Запуск рабочего потока
    worker_thread = threading.Thread(target=worker, daemon=True)
    worker_thread.start()
    while True:
        print(f"Пользователь {user_id}: Выберите пункт меню:\n"
              "1. Ввод исходного текста \n"
              "2. Выполнение алгоритма по поиску палиндромов в тексте\n"
              "3. Вывод результата\n"
              "4. Выход из цикла")
        choice = input()
        if is_int(choice):
            choice = int(choice)
        if choice == 1:
            print(f"Пользователь {user_id}: Сейчас задается текст...")
            task_queue.put(lambda: f1(array_palindromes, user_id, task_done))
            task_done.wait()
            task_done.clear()
            is_text_input = True
        elif choice == 2:
            if is_text_input:
                print(f"Пользователь {user_id}: Сейчас выполняется алгоритм поиска палиндромов...")
                task_queue.put(lambda: f2(array_palindromes, user_id, task_done))
                task_done.wait()
                task_done.clear()
                is_algorithm_done = True
            else:
                print("Ошибка!\nСначала введите текст\n\n")
        elif choice == 3:
            if is_algorithm_done:
                if is_text_input:
                    print(f"Пользователь {user_id}: Сейчас выводится результат...")
                    task_queue.put(lambda: f3(array_palindromes, user_id, task_done))
                    task_done.wait()
                    task_done.clear()
            else:
                print("\nСначала выполните алгоритм\n")
        elif choice == 4:
            task_queue.put(None)
            worker_thread.join()
            break
        else:
            print('error')
def menu():
    # Создаем два потока для двух пользователей
    user1_thread = threading.Thread(target=run_menu, args=(1,))
    user2_thread = threading.Thread(target=run_menu, args=(2,))
    # Запускаем потоки
    user1_thread.start()
    user2_thread.start()
    # Ждем завершения потоков
    user1_thread.join()
    user2_thread.join()
if __name__ == "__main__":
    menu()