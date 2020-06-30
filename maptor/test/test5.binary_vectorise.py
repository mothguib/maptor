#

import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "/../../")

from maptor import PCKGROOT
from maptor.control.BinaryProcessor import BinaryProcessor

lp = PCKGROOT + "../../Pytrol-Resources/" + "logs/islands/hpcc/15" \
                             "/3000/hpcc-islands-soc_1-15-3000-10.log.json"


graph, seq_pos, ridls, mts = BinaryProcessor.load_log(lp)
print(np.array(seq_pos, dtype=np.int).shape)

b = BinaryProcessor.binary_vectorise(seq_pos, graph)
print(np.array(b[1], dtype=np.int))
print(np.array(b[1], dtype=np.int).shape)
