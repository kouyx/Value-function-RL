import numpy as np

prob = np.zeros((7, 7))
prob[0, 1] = 0.5
prob[0, 5] = 0.5
prob[1, 2] = 0.8
prob[1, 6] = 0.2
prob[2, 3] = 0.6
prob[2, 4] = 0.4
prob[3, 6] = 1.0
prob[4, 0] = 0.2
prob[4, 1] = 0.4
prob[4, 2] = 0.4
prob[5, 0] = 0.1
prob[5, 5] = 0.9
prob[6, 6] = 1.0
rw = np.zeros((7, 1))
rw[0] = -2.0    # value function = -5.0
rw[1] = -2.0    # value function =  0.9
rw[2] = -2.0    # value function =  4.1
rw[3] = 10.0    # value function = 10.0
rw[4] =  1.0    # value function =  1.9
rw[5] = -1.0    # value function = -7.6
rw[6] =  0.0    # value function =  0
