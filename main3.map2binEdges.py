# -*- coding: utf-8 -*-

# Converting maps into a set of size-2 sequences where each one stands for
#  an edge

import json
import os
import sys
import numpy as np

# Adds the current package to the Python's path to run it from anywhere in the
# terminal
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from maptor import model
from maptor import MAPS
from maptor.control import BinaryProcessor, MapLoader

# Executing only if running as a script
if __name__ == "__main__":
    # Map name
    # m = sys.argv[1]

    for m in MAPS:
        path = BinaryProcessor.map_to_binpos(m)

        print("Path: ", path)
        with open(path, 'r') as s:
            # Binary map
            bm = json.load(s)
            print("Shape of the tensor of binary sequences for the map ", m,
                  ": ", np.array(bm).shape)

        with open(model.Paths.MAPS + '/' + m + ".json", 'r') as s2:
            vertices, edges, edges_to_vertices = MapLoader. \
                map_dict_to_iterables(json.load(s2))[2:5]

        print("Number of edges for the map {}: {}".format(m, len(edges)))

        # Number of vertices
        nv = len(vertices)

        nnghs = np.zeros(nv, dtype=np.int16)

        for i in range(nv):
            nnghs[i] = len(np.where(edges_to_vertices == i)[0])

        print("Mean degree of the map {}: {}".format(m, np.mean(nnghs)))
        print('\n')
