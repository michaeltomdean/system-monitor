"""
Author: Michael Dean
systeminfo.py

System info contains all the code fetching data about the system, such as CPU
utilization, memory, name of the CPU etc.
"""
import cpuinfo
import platform
import psutil


def read_sys_platform():
    """
    Reads system platform
    :return: platform (str)
    """
    return platform.system()


def read_cpu_hardware():
    """
    Reads all the information regarding CPU
    :return:
    """
    return cpuinfo.get_cpu_info()


def read_load_avg():
    """
    Read load average from psutil. Load average comes in the form [avg 1min, avg5min, avg15min]. First time it is
    run the data is meaningless so needs to be run once then updated continously. Its runs in the background and is
    non-blocking.
    :return: psutil.getloadavg()
    """
    return [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]


def read_cpu_usage():
    """
    Reads CPU usage over a 2-second interval. Runs blocking so must be run in a thread.
    :return: psutil.cpu_percent(2)
    """
    return psutil.cpu_percent(2)


def read_mem_usage():
    return psutil.virtual_memory()[2]


if __name__ == "__main__":
    print(read_mem_usage())
