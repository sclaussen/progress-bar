import time

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    # Call in a loop to create terminal progress bar
    #
    # @params:
    # iteration (required): current iteration (Int)
    # total (required):     total iterations (Int)
    # prefix (optional):    prefix string (Str)
    # suffix (optional):    suffix string (Str)
    # decimals (optional):  positive number of decimals in percent complete (Int)
    # length (optional):    character length of bar (Int)
    # fill (optional):      bar fill character (Str)
    # printEnd (optional):  end character (e.g. "\r", "\r\n") (Str)

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))

    # Number of fill chacters required
    filledLength = int(length * iteration // total)
    bar = (fill * filledLength) + ('-' * (length - filledLength))
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

    # Print New Line on Complete
    if iteration == total:
        print()


# percent = "{1:.0f} {0:.3f}, {2:s}".format(9, 7, "caden")
# print(percent);
# print("\U0001f600" * 100)
# print('Hello there Mr ', end="\r")
# print('Cad')


for i in range(100):
    printProgressBar(i, 100, "Downloading", "TICKTOCK", 1, 100, "\U0001f600")
    time.sleep(.1)
