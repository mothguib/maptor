# -*- coding: utf-8 -*-

import json
import os
import sys

import numpy as np

from maptor.control.MAPLoader import MapLoader
from maptor import Paths

sys.path.append(Paths.LOCALPYTROL)
import pytrol.util.pathformatter as pf


class BinaryProcessor:
    """
    A kind of processor providing various methods and tools to convert in
    binary format log paths of agents generated by the simulator Pytrol.
    """

    @staticmethod
    def load_log(log_fp: str, tpl: str):
        """
        Loading a log file of an execution.

        :param log_fp: path of the log file of a given execution,
        containing 3D-positions of agents to process
        :type log_fp: str
        :param tpl: map id
        :type tpl: int or str
        :return: a 4-tuple where:
            * the 1st coordinate is a list representing the map as graph
            * the 2nd coordinate is a list representing the "paths" of agents
            also known as the "sequence of positions" of agents
            * the 3rd coordinate is a list representing the real idlenesses
            for each period over all the execution
            * the 4th coordinate is a list representing the metrics of the
            execution
        :rtype:
        """

        graph = MapLoader.load_graph(tpl)

        with open(log_fp, 'r') as s:
            # Loading of the execution's log
            log = json.load(s)

        return graph, log[0][0], log[0][1], log[1]

    @classmethod
    def create_log_path(cls,
                        strt: str,
                        nagts,
                        duration: int,
                        tpl: str,
                        log_rep: str,
                        ext: str,
                        exec_id: int = -1,
                        variant: str = "0.2",
                        soc_name: str = None):
        """
        Creates a path for a log of type corresponding to the extension `ext`.

        :param ext:
        :type ext:
        :param strt:
        :type strt:
        :param nagts:
        :type nagts:
        :param duration:
        :type duration:
        :param exec_id:
        :type exec_id:
        :param tpl:
        :type tpl:
        :param variant:
        :type variant:
        :param soc_name:
        :type soc_name:
        :param log_rep:
        :type log_rep:
        :return:
        :rtype:
        """

        binpos_path = pf.build_log_path(tpl=tpl, strt=strt, variant=variant,
                                        nagts=nagts, exec_id=exec_id,
                                        duration=duration, soc_name=soc_name,
                                        logs_rep=log_rep, ext=ext)

        directory = os.path.dirname(binpos_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        return binpos_path

    @classmethod
    def binary_vectorise(cls, seq_pos: list, graph: np.ndarray) -> list:
        """

        :param seq_pos: sequence of 3D positions for every agent for each time
        step. Shape: `T x N_agts x 3`
        :type seq_pos: list
        :param graph: the graph standing for the map
        :type graph: list
        :return: the sequence binary-vectorised
        :rtype:
        """

        # Duration of the given execution: total number of periods
        duration = len(seq_pos)
        num_agts = len(seq_pos[0]) - 1
        num_vertices = len(graph)

        # Binary positions for all the execution, with the shape
        # `T' x N_agts x N_vts` where `T'` is the length of the initial
        # sequence with only vertex positions.
        b_pos = []

        # Loop over the agents
        for i in range(num_agts):
            b_pos_a = []
            # Loop over the time
            for t in range(duration):
                # i + 1 because the first agent is the coordinator
                if seq_pos[t][i + 1][1] == -1:
                    pos = [0] * num_vertices
                    pos[seq_pos[t][i + 1][0]] = 1
                    b_pos_a += [pos]
            # The binary positions
            b_pos += [b_pos_a]

        return b_pos

    @classmethod
    def generate_binpos(cls, log_fp: str, binpos_rep: str = None, tpl=-1):
        """
        Converts 3D-position ( (v, e, u) ) logs into binary position ones

        :param log_fp: file path of the log file of a given execution,
        containing 3D-positions of agents to process
        :type log_fp: str
        :param binpos_rep: path of the binary position log file
        :type binpos_rep: str
        :param tpl: map id
        :type tpl: int or str
        :return:
        :rtype:
        """

        graph, seq_pos, ridls, mts = cls.load_log(log_fp, tpl)

        binpos_path = cls.create_binpos_path(log_fp, binpos_rep)

        with open(binpos_path, 'w') as s:
            json.dump(cls.binary_vectorise(seq_pos, graph), s)

        return binpos_path

    @classmethod
    def gbpos(cls, log_fp: str, tpl: str, binpos_rep: str = ''):
        """
        Abbreviated version of the method `generate_binpos`

        :param log_fp:
        :param binpos_rep:
        :param tpl:
        :return:
        """
        return cls.generate_binpos(log_fp, binpos_rep, tpl)

    @staticmethod
    def map_to_binpos(map_name: str, path_bin_pos: str = ''):

        if path_bin_pos == '':
            path_bin_pos = Paths.BINMAPS + map_name + ".bin.json"

        directory = os.path.dirname(path_bin_pos)

        if not os.path.exists(directory):
            os.makedirs(directory)

        graph = MapLoader.mapname_to_iterables(map_name)[0]
        seqs = []

        for s in range(len(graph)):
            # Binary source
            bs = [0] * len(graph)
            if len(np.where(graph[s] > -1)[0]) > 0:
                bs[s] = 1

            # Binary target
            ts = [0] * len(graph)
            for t in range(len(graph)):
                ts = [0] * len(graph)
                if graph[s][t] > -1:
                    ts[t] = 1
                    seqs += [[bs, ts]]

        with open(path_bin_pos, 'w') as s:
            json.dump(seqs, s)

        return path_bin_pos

    @staticmethod
    def map_to_prob_pos(map_name: str, path_prob_pos: str = ''):
        """
        Map to a vector of probability. This method enables to take into
        account all the neighbours of a node at one time: the distribution
        over neighbours of a node is uniform

        :param map_name:
        :type map_name:
        :param path_prob_pos:
        :type path_prob_pos:
        :return:
        :rtype:
        """

        if path_prob_pos == '':
            path_prob_pos = Paths.PROBMAPS + map_name + ".prob.json"
        directory = os.path.dirname(path_prob_pos)

        if not os.path.exists(directory):
            os.makedirs(directory)

        graph = MapLoader.mapname_to_iterables(map_name)[0]
        seqs = []
        nb_edges = 0

        for s in range(len(graph)):
            seq1 = [0] * len(graph)
            if len(np.where(graph[s] == 1)[0]) > 0:
                seq1[s] = 1

            seq2 = np.zeros(len(graph))
            for t in range(len(graph)):
                if graph[s][t] > -1:
                    seq2[t] = 1
                    nb_edges += 1
            seq2 /= np.sum(seq2)

            seqs += [[seq1, seq2.tolist()]]

        with open(path_prob_pos, 'w') as s:
            json.dump(seqs, s)

        print("Number of edges counted for the map ", map_name, ": ", nb_edges)

        return path_prob_pos

    @staticmethod
    def binary_pos_to_vertex_id(bin_pos) -> int:
        return np.where(np.array(bin_pos, dtype=np.uint8) == 1)[0][0]

    @classmethod
    def bptvi(cls, bin_pos) -> int:
        return cls.binary_pos_to_vertex_id(bin_pos)
