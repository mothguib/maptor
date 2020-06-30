# test4.py: test to figure out why the number of edges in the data
# structures `graph` and `edges` returned by MapLoader.map_dict_to_iterables
#  are different.

import numpy as np

from maptor.control import MapLoader

graph, fl_edge_lgts, vertices, edges, edges_to_vertices, locations, \
    edge_activations, idls = MapLoader.mapname_to_iterables("map_a")

