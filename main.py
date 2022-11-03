# Simulationsumgebung für Schedulingverfahren RMS und DMS
# TODOS:
#   DONE: Get Data into the program!
#   DONE: Get basic cycle to work!
#   TODO: Timing on remaining period time is wrong and messing up with two values!
import math
import copy

def readfile(filename):
    # read data from file
    f = open(filename, 'r')
    data = []
    for line in f.readlines():
        task = []
        # for each comma-separated value in the string (with linebreaks removed)
        for index in line.replace("\n", "").split(","):
            if index.isnumeric():
                # if it's a number cast it into an int
                task.append(int(index))
            else:
                # else just append to task array
                task.append(index)
        # add every line to one array
        data.append(task)
    # print(data)
    return data


def lcmofarray(a):
    # return the lowest common multiple of elements in an array
    lcm = a[0][2]
    for i in range(1, len(a)):
        lcm = lcm * a[i][2] // math.gcd(lcm, a[i][2])
    return lcm


def sortbyperiod(elem):
    # helper function to sort array by 3rd value in element-array
    return elem[2]


def sortbydeadline(elem):
    # helper function to sort array by 4th value in element-array
    return elem[3]


def getutil(arr):
    # Calculate the utilization from the given array
    u = 0
    for task in arr:
        u = u + (task[1] / task[2])
    return u


def rms(filedata):
    print("\nRMS:")
    print(filedata)
    # rms algorithm
    lcm = lcmofarray(filedata)
    print("Hyperperiode: ", lcm)
    util = getutil(filedata)
    maxutil = len(filedata) * (math.pow(2, (1 / len(filedata))) - 1)
    print("Prozessorauslastung: ", util, ", Max: ", maxutil)
    if maxutil < util:
        print("==> RMS-Test nicht bestanden!")
    else:
        print("==> RMS-Test bestanden!")
    # sort by period length
    taskdata = copy.deepcopy(filedata)
    taskdata.sort(key=sortbyperiod)
    taskdataBackup = copy.deepcopy(taskdata)
    # calculate the output for RMS here
    rmsoutput = []
    for t in range(lcm):
        # Go through sorted tasks and append them to execution!
        for task in taskdata:
            if task[1] != 0:
                if task[2] != 0 and task[2] >= task[1]:
                    rmsoutput.append(task[0])
                    task[1] -= 1
                    break
                else:
                    raise Exception(task[0], " Cannot be scheduled, because comp time", task[1] ,"is longer than remaining period time", task[2], "on tick ", t)

        # Make sure the periods are updated every tick
        for x in range(len(taskdata)):
            taskdata[x][2] -= 1
            if taskdata[x][2] == 0:
                # If period is 0 recopy code from filedata
                taskdata[x] = copy.deepcopy(taskdataBackup[x])
        if len(rmsoutput) < (t + 1):
            rmsoutput.append("i")
    print(rmsoutput)
    print(taskdata)

def dms(filedata):
    print("\nDMS:")
    print(filedata)
    # dms algorithm
    lcm = lcmofarray(filedata)
    print("Hyperperiode: ", lcm)
    util = getutil(filedata)
    print("Prozessorauslastung: ", util)
    # sort by deadline length
    taskdata = copy.deepcopy(filedata)
    # make sure deadline exists
    for task in taskdata:
        if not task[3]:
            task[3]=task[2]
    taskdata.sort(key=sortbydeadline)
    taskdataBackup = copy.deepcopy(taskdata)
    # calculate the output for RMS here
    dmsoutput = []
    for t in range(lcm):
        # Go through sorted tasks and append them to execution!
        for task in taskdata:
            if task[1] != 0:
                if task[3] != 0 and task[3] >= task[1]:
                    dmsoutput.append(task[0])
                    task[1] -= 1
                    break
                else:
                    raise Exception(task[0], " Cannot be scheduled, because comp time", task[1] ,"is longer than remaining deadline time", task[3], "on tick ", t)

        # Make sure the periods are updated every tick
        for x in range(len(taskdata)):
            taskdata[x][2] -= 1
            taskdata[x][3] -= 1
            if taskdata[x][2] == 0:
                # If period is 0 recopy code from filedata
                taskdata[x] = copy.deepcopy(taskdataBackup[x])
        if len(dmsoutput) < (t + 1):
            dmsoutput.append("i")
    print(dmsoutput)
    print(taskdata)    

if __name__ == '__main__':
    # file structure: Name, Comp Time (C), Period (T), Deadline (D)
    fileData4 = readfile("Assets/Tasks4.txt")
    rms(fileData4)
    dms(fileData4)
    fileData22 = readfile("Assets/Tasks22.txt")
    # rms(fileData22)
    # dms(fileData22)

