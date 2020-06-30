# test10.bestmetricvalue.py: test of the method `best_variant_metric`

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "/../../")

from maptor import Paths
from maptor.control import StatisticComputer


log_fp = Paths.DATA + "/logs/"
statpath = Paths.DATA + "/stats/"

sc = StatisticComputer(log_fp, statpath)

strt = "rlpm"

sc.best_variant_metric("islands", strt, 5, 3000, 1, True)