import pytest
from Task_3_4 import checkout_text, getout

folder_out = "/home/funt/folder_out/"
folder_ext = "/home/funt/folder_ext/"
folder_hash = "/home/funt//Autotest_Linux_console_applications/"

# Показать файлы в папке не запуская
def test_7z_l():
    assert checkout_text(f'cd {folder_out}; 7z l ./archiv.7z', "Listing archive: ./archiv.7z"), "test_l FAIL"


# Разархивировать файлы из папки
def test_7z_x():
    assert checkout_text(f'cd {folder_ext}; 7z x {folder_out}archiv.7z', "Everything is Ok"), "test_x FAIL"


# Проверка хэша
def test_7z_h():
    crc32_hash = getout(f'cd {folder_hash}; crc32 checkers.py').upper()
    assert checkout_text(f'cd {folder_hash}; 7z h checkers.py', crc32_hash), "test_h FAIL"


if __name__ == '__main__':
    pytest.main()
