'''
Необхідно розробити функцію, яка приймає рядок як вхідний параметр, 
додає всі його символи до двосторонньої черги (deque з модуля collections в Python), 
а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 

Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, 
а також бути нечутливою до регістру та пробілів.
'''

from collections import deque

def is_palindrome(s):
    # Перетворення рядка в нижній регістр і видалення пробілів
    s = s.lower().replace(" ", "")
    
    # Створення двосторонньої черги та додавання символів до неї
    char_queue = deque(s)

    # Порівняння символів з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True

while True:
    print("\nMenu:")
    print("0. Exit")

    input_string = input("Введіть фразу: ")

    if input_string == '0':
        print("Goodbye!")
        break
    else:        
        result = is_palindrome(input_string)

        if result:
            print(f"The string '{input_string}' is a palindrome.")
        else:
            print(f"The string '{input_string}' is not a palindrome.")

