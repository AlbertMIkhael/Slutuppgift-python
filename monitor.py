import psutil


def hamta_cpu_anvandning():
    return psutil.cpu_percent(interval=1)


def hamta_minnesanvandning():
    mem = psutil.virtual_memory()
    procent = mem.percent
    anvant_gb = round(mem.used / (1024 ** 3), 1)
    total_gb = round(mem.total / (1024 ** 3), 1)
    return procent, anvant_gb, total_gb


def hamta_diskanvandning():
    disk = psutil.disk_usage('/')
    procent = disk.percent
    anvant_gb = round(disk.used / (1024 ** 3), 1)
    total_gb = round(disk.total / (1024 ** 3), 1)
    return procent, anvant_gb, total_gb
