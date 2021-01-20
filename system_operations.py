import psutil

def cpu():
    usage= str(psutil.cpu_percent())
    return "CPU is at "+ usage

def battary():
    available_bat= str(psutil.sensors_battery())
    return "Battary is at "+available_bat
