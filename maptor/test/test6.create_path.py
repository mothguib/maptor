#

import sys
import os

import numpy as np

sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "/../../")

from maptor.control.LogProcessor import LogProcessor
from maptor import Paths

lp = Paths.DATA + "logs/islands/hpcc/15" \
                             "/10000/hpcc-islands-soc_1_15-10000-185.log.json"

print(LogProcessor.create_path(lp, Paths.BIN, "log.bin"))
