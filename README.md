# GenBruter
It is a simple password brute force tool designed for ethical hacking and security testing. Automates the process of selecting passwords for a given user on a website by sending POST requests with different passwords and analyzing the response.

# EN
## Installation and Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/geniuszlyy/GenBruter.git
   cd GenBruter
   ```
2. **Install dependencies**
   Make sure you have Python 3 and `pip` installed.
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the program**
   ```bash
   python GenBruter.py
   ```
## Usage
- **Target URL**: Enter the URL of the login page you want to attack.
- **Username**: Enter the username (e.g., email) of the user.
- **Negative Response**: Enter the text indicating a failed login attempt (e.g., "Invalid").

![image](https://github.com/user-attachments/assets/613e0300-a85b-40cd-b2ce-634af2196987)

The program will automatically load the list of passwords from the `passwords.txt` file located in the same directory as the script and start the brute-force process.

## Requirements
- Python 3.x
- `requests` library (install with `pip`)

## Notes
- **Password File**: Ensure that the `passwords.txt` file contains one password per line.
- **CSRF Protection**: Some sites may use CSRF tokens or other security mechanisms. In such cases, this tool may not work as expected.

## Disclaimer
This tool is intended for educational purposes and security testing only. Do not use it for unauthorized access to any systems. Always obtain permission before using this tool on a website.

# RU

## Установка и запуск

1. **Клонирование репозитория**
   ```bash
   git clone https://github.com/geniuszlyy/GenBruter.git
   cd GenBruter
   ```
2. **Установка зависимостей**
   Убедитесь, что у вас установлен Python 3 и `pip`.
   ```bash
   pip install -r requirements.txt
   ```
3. **Запуск программы**
   ```bash
   python GenBruter.py
   ```

## Использование
- **URL для атаки**: Введите URL-адрес страницы входа.
- **Имя пользователя**: Введите логин (например, электронную почту).
- **Отрицательный ответ**: Введите текст, указывающий на неудачный вход (например, "Invalid").

![image](https://github.com/user-attachments/assets/613e0300-a85b-40cd-b2ce-634af2196987)

Программа автоматически загрузит список паролей из файла `passwords.txt`, который должен находиться в той же директории, что и скрипт, и начнет перебор паролей.

## Требования
- Python 3.x
- Библиотека `requests` (устанавливается с помощью `pip`)


## Замечания
- **Файл паролей**: Убедитесь, что файл `passwords.txt` содержит пароли по одному на строку.
- **CSRF-защита**: Некоторые сайты могут использовать CSRF-токены или другие механизмы защиты. В таких случаях данный инструмент может не сработать.

## Важное замечание
Этот инструмент предназначен исключительно для образовательных целей и тестирования безопасности. Не используйте его для несанкционированного доступа к чужим системам. Всегда получайте разрешение перед использованием данного инструмента на сайте, который вы тестируете.
