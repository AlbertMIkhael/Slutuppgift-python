import psutil


def hämta_cpu_användning():
    return psutil.cpu_percent(interval=1)


def hämta_minnesanvändning():
    mem = psutil.virtual_memory()
    procent = mem.percent
    anvant_gb = round(mem.used / (1024 ** 3), 1)
    total_gb = round(mem.total / (1024 ** 3), 1)
    return procent, anvant_gb, total_gb


def hämta_diskanvändning():
    disk = psutil.disk_usage('/')
    procent = disk.percent
    anvant_gb = round(disk.used / (1024 ** 3), 1)
    total_gb = round(disk.total / (1024 ** 3), 1)
    return procent, anvant_gb, total_gb

