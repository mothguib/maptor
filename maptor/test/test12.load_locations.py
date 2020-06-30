# -*- coding: utf-8 -*-

import json

from maptor.control import MapLoader
from maptor.model import Paths


def main(m: str = 'islands'):
    map_path = Paths.MAPS + "/" + m + ".json"

    with open(map_path) as s:
        graph_d = json.load(s)

    graph, fl_edge_lgts, vertices, edges, edges_to_vertices, locations, \
    edge_activations, idls = MapLoader.map_dict_to_iterables(graph_d)

    print(locations)


if __name__ == "__main__":
    m = "circle"
    main(m)

