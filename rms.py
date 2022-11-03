import copy
import math
from tqdm import tqdm
from helpers import lcmofarray
from helpers import getutil
from helpers import sortbyperiod
from formatOutput import format_output_as_gant


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
    for t in tqdm(range(lcm), desc="RMS Scheduling", colour="#48dd40"):
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
    format_output_as_gant(rmsoutput, filedata)
