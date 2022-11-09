# optimized priority with rta
import copy
from helpers import swappositions
from rta import rta


def rta_opti_prio(filearray):

    res_array = copy.deepcopy(filearray)
    res_rta = True

    for K in range(len(filearray)):
        for nxt in range(K, len(filearray)):

            res_array = swappositions(res_array, K, nxt)
            res_rta = rta(res_array)[K] <= filearray[K][2]

            if res_rta:
                break
        if not res_rta:
            break

    return res_array
