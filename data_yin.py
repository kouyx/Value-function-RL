import numpy as np

prob = np.zeros((7, 7))
prob[0, 0] = 0.9
prob[0, 2] = 0.1
prob[1, 1] = 1.0
prob[2, 0] = 0.5
prob[2, 3] = 0.5
prob[3, 1] = 0.2
prob[3, 4] = 0.8
prob[4, 5] = 0.6
prob[4, 6] = 0.4
prob[5, 1] = 1.0
prob[6, 2] = 0.2
prob[6, 3] = 0.4
prob[6, 4] = 0.4
rw = np.zeros((7, 1))
rw[0] = -1.0    # value function = -7.6
rw[1] =  0.0    # value function =  0
rw[2] = -2.0    # value function = -5.0
rw[3] = -2.0    # value function =  0.9
rw[4] = -2.0    # value function =  4.1
rw[5] = 10.0    # value function = 10.0
rw[6] =  1.0    # value function =  1.9
