"""
Author: Michael Dean
test\\systeminfo.py
"""

from backend.systeminfo import *


def testall():
    assert test_read_sys_platform()


def test_read_sys_platform():
    if read_sys_platform() in ["Windows", "Linux", "Darwn"]:
        return True
    else:
        return False


if __name__ == "__main__":
    testall()
