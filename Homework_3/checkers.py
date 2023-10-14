# Задание 1.
# Дополнить проект фикстурой, которая после каждого шага теста дописывает в заранее созданный файл stat.txt строку вида:
# время, кол-во файлов из конфига, размер файла из конфига, статистика загрузки процессора из файла 
# /proc/loadavg (можно писать просто всё содержимое этого файла).
# Задание 2. (дополнительное задание)
# Дополнить все тесты ключом команды 7z -t (тип архива). Вынести этот параметр в конфиг.
import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False


def getout(cmd):
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout
