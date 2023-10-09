# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена
# и текст найден в её выводе и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.
import subprocess


def checkout_text(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False