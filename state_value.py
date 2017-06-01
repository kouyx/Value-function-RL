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
    try:
        gm_input = raw_input("Input a gamma between 0 and 1 (or leave empty to set to 0.9):")
        if gm_input == "":
            gm = 0.9
        elif float(gm_input) > 1 or float(gm_input) < 0:
            print("Input is out of range [0, 1]. Set gamma to default (0.9).")
            gm = 0.9
        else:
            gm = float(gm_input)
    except ValueError:
        print("Input is not a number. Set gamma to default (0.9).")
        gm = 0.9
    finally:
        print("Gamma = {}".format(gm))
        vl = value_func(prob, rw, gm, rw)
        print("Final value function: \n{}".format(np.round(vl, 1)))
