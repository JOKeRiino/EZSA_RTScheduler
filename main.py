# Simulationsumgebung für Schedulingverfahren RMS und DMS
# TODOS:
#   DONE: Get Data into the program!
#   DONE: Get basic cycle to work!
#   DONE: RMS & DMS Scheduling work!

from filereader import readfile
from rms import rms
from dms import dms


def rms_from_file(path):
    filedata = readfile(path)
    rms(filedata)


def dms_from_file(path):
    filedata = readfile(path)
    dms(filedata)


if __name__ == '__main__':
    # file structure: Name, Comp Time (C), Period (T), Deadline (D)
    # rms_from_file("Assets/Tasks4.txt")
    # dms_from_file("Assets/Tasks4.txt")
    # rms_from_file("Assets/Tasks22.txt")
    # dms_from_file("Assets/Tasks22.txt")

    #RTA
     rms_from_file("Assets/TasksRTA.txt")
