# test3.py: test of the methods binary_vectorise and thr_d_to_binary_pos:

import json

from maptor import PCKGROOT
from maptor.control import MapLoader
from maptor.control.BinaryProcessor import BinaryProcessor


log_path = PCKGROOT + "data/logs/json/islands/hpcc/hpcc-islands-soc_1_10/" + \
                "hpcc-islands-soc_1_10-0.log.json"


# log_path = VARIOUS + "test_logs/hpcc-islands-soc_1_10-0.tmp.log.prcss.json"

map_path = PCKGROOT + "data/maps/json/islands.json"

with open(log_path, 'r') as s:
    seq = json.load(s)[0][0]

with open(map_path, 'r') as s:
    graph = MapLoader.map_dict_to_iterables(json.load(s))[0]

v = BinaryProcessor.binary_vectorise(seq, graph)

BinaryProcessor.thr_d_to_binary_pos(log_path)
