# test7.generate_save_binpos_and_idls.py: test of the method `generate_save_binpos_and_idls`

import json
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "/../../")

from maptor import PCKGROOT

lp = PCKGROOT + "/../logs/" + "logs/islands/hpcc/15" \
                  "/10000/hpcc-islands-soc_1_15-10000-185.log.json"

lap = PCKGROOT + "/../logs/" + "logs/islands/hpcc/15/" \
                   "10000/hpcc-islands-soc_1_15-10000-185.agts" \
                   ".log.json"

lp2 = PCKGROOT + "/../logs/" + "logs/islands/hpcc/1" \
                   "/3000/hpcc-islands-soc_1_1-3000-1.log.json"

lb = PCKGROOT + "/../logs/" + "logs-bin/islands/hpcc/1/3000/" \
                  "hpcc-islands-soc_1_1-0.log.bin.json"

lp3 = os.environ["REPS"] + "/Pytrol/various/logs/map_a/hpcc/10/20/" \
                           "hpcc-map_a-soc_1_10-20-1.log.json"

lap3 = os.environ["REPS"] + "/Pytrol/various/logs/map_a/hpcc/10/20/" \
                           "hpcc-map_a-soc_1_10-20-1.log.agts.json"

print("Log of positions for the execution HPCC 15 10000 185 ")
with open(lp, 'r') as s:
    log = json.load(s)
p = np.array(log[0][0])
print(p.shape)

print("Log of real idls for the execution HPCC 15 10000 185 ")
pidls = np.array(log[0][1])
print(pidls.shape, '\n')

print("Log of agt idls for the execution HPCC 15 10000 185 ")
with open(lap, 'r') as s:
    a = np.array(json.load(s))
print(a.shape)

agt_id = 1
for i in range(20):
    print("Position of agent", agt_id, "at t =", i, ":", p[i][agt_id])
    print("Nodes where idleness is nul:", np.where(a[agt_id][i] == 0)[0],
          "\nIndividual idleness:", a[agt_id][i])
print('\n\n')

print("Log of positions for the execution HPCC 1 3000 1 ")
with open(lp2, 'r') as s:
    log = json.load(s)
p = np.array(log[0][0])
print(p.shape)
print("Log of real idls for the execution HPCC 1 3000 1 ")
pidls = np.array(log[0][1])
print(pidls.shape, '\n')

with open(lb, 'r') as s:
    b = np.array(json.load(s))
print(b.shape)
print(np.where(b == 1)[2])

print("Log of positions for the execution HPCC 10 20 1 ")
with open(lp3, 'r') as s:
    log = json.load(s)
p = np.array(log[0][0])
print(p.shape)

print("Log of real idls for the execution HPCC 10 20 1 ")
pidls = np.array(log[0][1])
print(pidls.shape, '\n')

# Testing if coordinator (agent id 0) is situated.
print("Id of agent on the node 24 according to the time: ",
      np.where(p == 24)[1])
print(np.where(pidls[::-1, 24] == 0))

print("Log of agt idls 3")
with open(lap3, 'r') as s:
    a = np.array(json.load(s))
print(a.shape)

agt_id = 1
print("agt ", agt_id)
for i in range(20):
    print("Position of agent", agt_id, "at t =", i, ":", p[i][agt_id])
    print("Nodes where idleness is nul:", np.where(a[agt_id][i] == 0)[0], \
          "\nIndividual idleness:", a[agt_id][i])
print('\n')

agt_id = 0
print("agt ", agt_id)
for i in range(20):
    print("Position of agent", agt_id, "at t =", i, ":", p[i][agt_id])
    print("Nodes where idleness is nul:", np.where(a[agt_id][i] == 0)[0], \
          "\nIndividual idleness:", a[agt_id][i])
print('\n')