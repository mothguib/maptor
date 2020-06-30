# test7.generate_save_binpos_and_idls.py: test of the `generate_save_binpos_and_idls` method,
# abreviated `generate_save_binpos_and_idls`

import json
import sys
import os
import numpy as np

# Adds the current package to the Python's path to run it from the terminal
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "/../../")

from maptor.control import BinaryProcessor
from maptor.control.LogProcessor import LogProcessor
from maptor import Paths


lp = Paths.DATA + "logs/islands/hpcc/10" \
                  "/3000/hpcc-islands-soc_1_10-3000-0.log.json"

la = Paths.DATA + "logs/islands/hpcc/10/" \
                  "3000/hpcc-islands-soc_1_10-3000-0.log.agts.json"

lb = BinaryProcessor.create_binpos_path(lp, Paths.PCKGROOT +
                                        "/../logs/logs-bin")
li = LogProcessor.create_viidls_path(lp, Paths.PCKGROOT +
                                        "/../logs/logs-viidls")
lidls = LogProcessor.create_viidls_path(lp, Paths.PCKGROOT +
                                         "/../logs/logs-vidls")

print("Input files")
print(la)
print(la)

# `bpp`, `iip` and idlsp for binary positions, individual idlenesses, and real
# idlenesses paths, respectively
bpp, iip, idlsp = LogProcessor.generate_save_binpos_and_idls(lp, la, Paths.PCKGROOT +
                                      "/../logs/logs-bin",
                             Paths.PCKGROOT +
                                      "/../logs/logs-viidls",
                             Paths.PCKGROOT +
                                      "/../logs/logs-vidls")

print("Output files")
print(lb)
print(li)

with open(bpp, 'r') as s:
    lb = json.load(s)

min_len = min([len(e) for e in lb])

# Truncation of the loaded list to have an uniform shape for all elements
for i in range(len(lb)):
    lb[i] = lb[i][:min_len]
ndb = np.array(lb, dtype=np.uint8)

print("Shape of the binary positions:", ndb.shape)

with open(iip, 'r') as s:
    li = json.load(s)

# Truncation of the loaded list to have an uniform shape for all elements
for i in range(len(li)):
    li[i] = li[i][:min_len]
ndi = np.array(li, dtype=np.int16)

print("Shape of the individual idlenesses:", ndi.shape)

with open(idlsp, 'r') as s:
    lidls = json.load(s)

# Truncation of the loaded list to have an uniform shape for all elements
for i in range(len(lidls)):
    lidls[i] = lidls[i][:min_len]

ndidls = np.array(lidls, dtype=np.int16)

print("Shape of the real idlenesses:", ndidls.shape)

# Individual and real idlenesses for t = 300 and agent id 0
print(ndi[0][300])
print(ndidls[0][300])
