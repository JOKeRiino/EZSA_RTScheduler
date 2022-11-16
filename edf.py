# EDF scheduling
from tqdm import tqdm
from helpers import lcmofarray
import copy
from formatOutput import format_output_as_gant
from helpers import sortbydeadline

def test_edf_schedulability(filedata):
    sum = 0
    for task in filedata:
        sum += (task[1] / task[2])
    return sum


def edf_dens_test(filedata):
    sum = 0
    for task in filedata:
        sum += (task[1] / task[3])
    return sum

def findTaskdata(taskbackup, taskname):
    for task in taskbackup:
        if task[0] == taskname:
            return task


def edf(filedata):
    print("\nEDF:")
    print(filedata)
    # test if schedulable
    test_result = test_edf_schedulability(filedata)
    if test_result <= 1:
        print("Prozessorauslastung: ", test_result * 100, "% - EDF möglich")
    else:
        print("Prozessorauslastung: ", test_result * 100, "% - EDF NICHT möglich")

    density_result = edf_dens_test(filedata)
    print("Dichte: ", density_result)

    lcm = lcmofarray(filedata)
    print("Hyperperiode: ", lcm)

    taskdata = copy.deepcopy(filedata)
    taskdataBackup = copy.deepcopy(taskdata)

    edfoutput = []
    for t in tqdm(range(lcm), desc="EDF Scheduling", colour="#48dd40"):

        # SORT TASKDATA HERE!!!
        taskdata.sort(key=sortbydeadline)

        # Go through sorted tasks and append them to execution!
        for task in taskdata:
            if task[1] != 0:
                if task[2] != 0 and task[2] >= task[1]:
                    edfoutput.append(task[0])
                    task[1] -= 1
                    break
                else:
                    raise Exception(task[0], " Cannot be scheduled, because comp time", task[1] ,"is longer than remaining period time", task[2], "on tick ", t)

        # Make sure the periods are updated every tick
        for x in range(len(taskdata)):
            taskdata[x][2] -= 1
            taskdata[x][3] -= 1
            if taskdata[x][2] == 0:
                # If period is 0 recopy code from filedata
                # taskdata[x] = copy.deepcopy(taskdataBackup[x])
                taskdata[x] = copy.deepcopy(findTaskdata(taskdataBackup, taskdata[x][0]))
        if len(edfoutput) < (t + 1):
            edfoutput.append("i")

    print(edfoutput)
    format_output_as_gant(edfoutput, filedata)
