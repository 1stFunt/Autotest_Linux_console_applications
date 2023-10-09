import pytest
from Task_1 import checkout_text


def test():
    assert checkout_text("cat /etc/os-release", "jammy", remove_punctuation=True), "test1 FAIL"


if __name__ == '__main__':
    pytest.main()
