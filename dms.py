import copy
from tqdm import tqdm
from helpers import lcmofarray
from helpers import getutil
from helpers import sortbydeadline
from formatOutput import format_output_as_gant


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
            task[3] = task[2]
    taskdata.sort(key=sortbydeadline)
    taskdataBackup = copy.deepcopy(taskdata)
    # calculate the output for RMS here
    dmsoutput = []
    for t in tqdm(range(lcm), desc="DMS Scheduling", colour="#48dd40"):
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
    format_output_as_gant(dmsoutput, filedata)
