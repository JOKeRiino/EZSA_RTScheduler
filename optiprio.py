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
            res = res_array[::-1]
            res_rta = rta(res)[filearray[K][0]]

            if res_rta != -1:
                break
        if res_rta == -1:
            break

    return res_array
