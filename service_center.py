'''
Завдання 1

Потрібно розробити програму, яка імітує приймання й обробку заявок: 
- програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними),
- додавати їх до черги, а
- потім послідовно видаляти з черги для "обробки", 
імітуючи таким чином роботу сервісного центру.

Ось псевдокод для завдання з використанням черги (Queue з модуля queue в Python) для системи обробки заявок:
import Queue

Створити чергу заявок
queue = Queue()

Функція generate_request():
    Створити нову заявку
    Додати заявку до черги

Функція process_request():
    Якщо черга не пуста:
        Видалити заявку з черги
        Обробити заявку
    Інакше:
        Вивести повідомлення, що черга пуста

Головний цикл програми:
    Поки користувач не вийде з програми:
        Виконати generate_request() для створення нових заявок
        Виконати process_request() для обробки заявок
'''
import queue
import time

# Створення черги заявок
request_queue = queue.Queue()
request_counter = 0 # Змінна для унікальних ідентифікаторів

# Функція для генерації нових заявок
def generate_request():
    global request_counter
    request_counter += 1

    new_request = f"Request {request_counter}"
    request_queue.put(new_request)
    
    print(f"Generated new request: {new_request}")

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        processed_request = request_queue.get()
        print(f"Processing request: {processed_request}")
    else:
        print("No requests in the queue. Waiting for new requests.")

# Головний цикл програми
while True:
    print("\nMenu:")
    print("1. Generate new request")
    print("2. Process requests")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        generate_request()
    elif choice == '2':
        process_request()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    time.sleep(1)  # чекаємо 1 секунду між ітераціями для імітації роботи в реальному часі


