# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x)
# Установить пакет для расчёта crc32 (sudo apt install libarchive-zip-perl)
# Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32
import subprocess


def checkout_text(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def getout(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return result.stdout
