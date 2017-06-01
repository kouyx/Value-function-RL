import numpy as np
from data_yin import prob, rw  # or data_david


def value_func(prob_mat, reward_arr, gamma, value_former, recur_depth=0):
    value_current = np.round((reward_arr + gamma * np.dot(prob_mat, value_former)), 2)
    if any(value_current != value_former):
        recur_depth += 1
        value_former = value_func(prob_mat, reward_arr, gamma, value_current, recur_depth)
        return value_former
    else:
        print("Recursion depth: {}.".format(recur_depth))
        return value_current


if __name__ == '__main__':
    gm = 0.9
    vl = value_func(prob, rw, gm, rw)
    print("Final value function: \n{}".format(np.round(vl, 1)))
