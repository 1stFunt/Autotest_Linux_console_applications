# Доработать функцию из предыдущего задания таким образом,
# чтобы у неё появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.
import subprocess
import string  # Импорт модуля string для доступа к знакам пунктуации


def checkout_text(cmd, text, remove_punctuation=False):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')

    if remove_punctuation:
        for punctuation in string.punctuation:
            result.stdout = result.stdout.replace(punctuation, '')

    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False
