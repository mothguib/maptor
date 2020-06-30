# test9

import json
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "/../../")

from maptor import PCKGROOT

path = PCKGROOT + "/../logs/" + "logs/map_a/hpcc/10/20/" \
                           "hpcc-map_a-soc_1_10-20-1.log.json"


print("# Log of positions for ", path.split('/')[-1])
print("-----------------")
with open(path, 'r') as s:
    log = json.load(s)
p = np.array(log[0][0])

print("Shape of the `p` tensor:")
print(p.shape)

print("Shape of the tensor of real idls:")
pidls = np.array(log[0][1])
print(pidls.shape, '\n')

with open(path.replace(".log", ".log.agts"), 'r') as s:
    ii = np.array(json.load(s))
print("Shape of agt idls")
print(ii.shape, '\n')

print("First positions of agents 0 and 1:")
print("0: ", p[0][0], ", 1:", p[0][1], '\n')

print("Last positions of agents 0 and 1:")
print("0: ", p[-1][0], ", 1:", p[-1][1], '\n')

print("First and last individual idleness for agent 1:")
print(ii[1][0], '\n', ii[1][-1], '\n')

print("First and last real idleness:")
print(pidls[0], '\n', pidls[-1], '\n')