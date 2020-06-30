# -*- coding: utf-8 -*-

import json
import os
import warnings
import numpy as np
import networkx as nx

from maptor import Maps
from maptor import Paths


SCALE = 50


class MAPLoader:
    @classmethod
    def map_dict_to_iterables(cls,
                              graph_d: dict):

        vertices = {}

        # Vertices' dictionary
        vertices_d = graph_d['vertices']

        for i, v in enumerate(vertices_d):
            vertices[v['id']] = i

        # Edge dictionary
        edges_d = graph_d['edges']
        graph = np.ones([len(vertices), len(vertices)], dtype=np.int16) * -1

        # Floating edge lengths
        fl_edge_lgts = np.zeros([len(edges_d)], dtype=np.float16)

        # Original edge id to integer edge id
        edges = {}

        # Integer edge ids to integer vertices' ids
        edges_to_vertices = np.empty([len(fl_edge_lgts), 2], dtype=np.int16)

        # List of duplicate edges (same source and target) if any
        dup_edges = []

        i = 0
        for e in edges_d:
            if graph[vertices[e['source']]][vertices[e['target']]] > -1:
                dup_edges += [e["id"]]

            edges[e["id"]] = i
            graph[vertices[e['source']]][vertices[e['target']]] = i
            graph[vertices[e['target']]][vertices[e['source']]] = i
            fl_edge_lgts[i] = float(e['length'])
            edges_to_vertices[i] = [vertices[e['source']], vertices[e[
                'target']]]
            i += 1

        locations = MapLoader.load_locations(graph_d, edges_to_vertices,
                                             fl_edge_lgts)

        # Number of edges in the graph
        graph_nb_edges = int(len(np.where(graph > -1)[0]) / 2)

        if graph_nb_edges != len(edges):
            warn_str = "At least one duplicate edge in the configuration " \
                       "file: edges " + ", ".join(dup_edges) + "."
            warnings.warn(warn_str, UserWarning)

        edge_activations = np.ones(len(fl_edge_lgts), dtype=np.int16)

        idls = np.array([0] * len(graph), dtype=np.int16)

        return graph, fl_edge_lgts, vertices, edges, edges_to_vertices, \
               locations, edge_activations, idls

    @classmethod
    def load_locations(cls,
                       graph_d: dict,
                       edges_to_vertices: np.ndarray,
                       fl_edge_lgts: np.ndarray) -> np.ndarray:

        if 'location' in graph_d['vertices'][0]:
            # Vertices' dictionary
            vertices_d = graph_d['vertices']

            locations = np.zeros((len(vertices_d), 3))

            if 'x' in vertices_d[0]['location'] \
                    and 'y' in vertices_d[0]['location']:

                for i, v in enumerate(vertices_d):
                    locations[i][0] = np.float32(v['location']['x'])
                    locations[i][1] = np.float32(v['location']['y'])

                if 'z' in vertices_d[0]:
                    for i, v in enumerate(vertices_d):
                        locations[i][2] = np.float32(v['location']['z'])
        else:
            # Positions of nodes
            locations = cls.load_map_locations(graph_d,
                                               edges_to_vertices,
                                               fl_edge_lgts)

        return locations

    @classmethod
    def load_map_locations(cls,
                           graph_d: dict,
                           edges_to_vertices: np.ndarray,
                           fl_edge_lgts: np.ndarray) -> np.ndarray:
        """
        Here a model is the situation of the map `graph_d`

        :param graph_d:
        :param edges_to_vertices:
        :param fl_edge_lgts:
        :return:
        """

        # Model file name
        model_fn = graph_d["label"] + ".loc.json"
        model_path = Paths.LOC + "/" + model_fn

        if os.path.exists(model_path):
            locs = cls.load_locations_from_model(graph_d)
        else:
            locs = cls.generate_locations(edges_to_vertices,
                                          fl_edge_lgts)

            if not os.path.exists(os.path.dirname(model_path)):
                os.makedirs(os.path.dirname(model_path))
            with open(model_path, 'w') as s:
                json.dump(locs.tolist(), s)

        return locs

    @staticmethod
    def load_locations_from_model(graph_d: dict) -> np.ndarray:
        """
        Here a model is the situation of the map `graph_d`

        :param graph_d:
        :type graph_d:
        :return:
        """

        # Vertices' dictionary
        vtcs_d = graph_d["vertices"]

        # Model file name
        model_fn = graph_d["label"] + ".loc.json"
        # Model path
        model_path = Paths.LOC + "/" + model_fn

        # Localisations
        locs = np.zeros((len(vtcs_d), 3), dtype=np.float64)

        with open(model_path, 'r') as s:
            model = json.load(s)

            for i, e in enumerate(model):
                locs[i] = [np.float64(e[0]),
                           np.float64(e[1]),
                           np.float64(e[2])]

        return locs

    @staticmethod
    def generate_locations(edges_to_vertices: np.ndarray,
                           fl_edge_lgts: np.ndarray,
                           scale: float = SCALE) -> np.ndarray:

        # Number of vertices
        nvtcs = edges_to_vertices.max() + 1

        # The NetworkX graph
        g = nx.Graph()

        # Localisations
        locs = np.zeros((nvtcs, 3), dtype=np.float64)

        for i, e in enumerate(edges_to_vertices):
            # You can attach any attributes you want when adding the edge
            g.add_edge(e[0], e[1], length=fl_edge_lgts[i])

        # Dictionary of positions
        locs_d = nx.spring_layout(g)
        '''
        The resulting shape is a square of side 
        `[center - scale, center + scale]`(default: `[-1, 1]`).
        '''

        for v in locs_d:
            locs[v] = [locs_d[v][0], locs_d[v][1], 0.0]

        return locs * scale

    @classmethod
    def map_fp_to_iterables(cls, fp: str):
        """
        File path of the map to the format JSON to iterables

        :param fp: file path of the map
        :type fp: str
        :return:
        :rtype:
        """
        with open(fp, 'r') as s:
            map_dict = json.load(s)

        return cls.map_dict_to_iterables(map_dict)

    @classmethod
    def mapname_to_iterables(cls, tpl: str):
        return cls.map_fp_to_iterables(Paths.MAPS + tpl + ".json")

    @staticmethod
    def get_mapname(execname: str, tpl: str) -> str:
        """
        Getting map name from an execution name or an int or str map id

        :param execname:
        :param tpl:
        :return:
        """

        if isinstance(tpl, str):
            mapname = tpl
        elif tpl == -1:
            # Graph path
            mapname = execname.split("-")[1]
        else:
            mapname = Maps.id_to_name(tpl)

        return mapname

    @staticmethod
    def load_graph(tpl: str) -> np.ndarray:
        """

        :param tpl:
        :return:
        :rtype: np.ndarray
        """

        return MapLoader.mapname_to_iterables(tpl)[0]
