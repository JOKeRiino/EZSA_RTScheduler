# Response-Time Analysis
# for RMS & DMS
import math


def rta(sortedarray):
    # Calculate response time for each task from sortedarray
    # file structure: Name, Comp Time (C), Period (T), Deadline (D)
    # R_1 -> C_b + ∑( ⌈ R_0 / T_a ⌉ * C_a )
    res_times = []
    resdict = {}
    index = 0
    for task in sortedarray:
        # begin with highest priority
        if index == 0:
            # rt of highest priority task is its execution time

            # res_times.append(str(task[0]) + ": " + str(task[1]))
            res_times.append(task[1])
            resdict [task[0]]=task[1]
        else:
            r_0 = task[1]
            r = 0
            # solange zeit kleiner ist als die alte zeit und zeit kleiner gleich der deadline ist
            while r <= task[3]:
                r_sum = 0
                for x in range(index, 0, -1):
                    r_sum += math.ceil(r_0 / sortedarray[x - 1][2]) * sortedarray[x - 1][1]
                r = task[1] + r_sum
                if r == r_0:
                    break
                else:
                    r_0 = r
            if r > task[3]:
                r = -1
            # res_times.append(str(task[0]) + ": " + str(r))
            res_times.append(r)
            resdict[task[0]]=r

        index += 1

    # print("\n RTA: ", res_times)
    outputstring = ""
    for x in range(len(sortedarray)):
        outputstring += sortedarray[x][0] + ": " + str(res_times[x]) + ", "
    print(outputstring)

    print(resdict)

    return resdict
