import time

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))

    # Number of fill chacters required
    filledLength = int(length * iteration // total)
    bar = (fill * filledLength) + ('-' * (length - filledLength))
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = '\r')

for i in range(100):
    printProgressBar(i, 100, "Downloading", "Goal", 0, 100, "*")
    time.sleep(.1)
