# Simulationsumgebung für Schedulingverfahren RMS und DMS
# TODOS:
#   DONE: Get Data into the program!
#   DONE: Get basic cycle to work!
#   DONE: RMS & DMS Scheduling work!

from filereader import readfile
from rms import rms
from dms import dms
from edf import edf


def rms_from_file(path, optiPrio):
    filedata = readfile(path)
    rms(filedata, optiPrio)


def dms_from_file(path):
    filedata = readfile(path)
    dms(filedata)


def edf_from_file(path):
    filedata = readfile(path)
    edf(filedata)


if __name__ == '__main__':
    # file structure: Name, Comp Time (C), Period (T), Deadline (D)
    # rms_from_file("Assets/Tasks4.txt", optiPrio=True)
    # rms_from_file("Assets/TasksOptiPrio.txt", optiPrio=True)
    # dms_from_file("Assets/Tasks4.txt")
    # rms_from_file("Assets/Tasks22.txt")
    # dms_from_file("Assets/Tasks22.txt")

    edf_from_file("Assets/TasksEDF.txt")

    # RTA
    # rms_from_file("Assets/TasksRTA.txt")

    # optiPrio
    # print(opti_prio(readfile("Assets/TasksOptiPrio.txt")))

