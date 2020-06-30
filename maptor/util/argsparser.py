# -*- coding: utf-8 -*-

import argparse

from maptor import Paths


def parse_args():
    parser = argparse.ArgumentParser(description="PytrolSimEditor: "
                                                 "Pytrol editor and "
                                                 "configurator")

    parser.add_argument("--map", type=str, default="map_a",
                        help="the topology of network")
    parser.add_argument("--nagts", type=int, default=10,
                        help="number of agents")
    parser.add_argument("--strategy", type=str, default="hpcc",
                        help="the strategy of agents")
    parser.add_argument("--society", type=str, default=None,
                        help="the society name of agents")
    parser.add_argument("--variant", type=str, default='0.5',
                        help="the variant of the strategy (its parameters, "
                             "etc.")
    parser.add_argument("--duration", type=int, default=3000,
                        help="number of periods of the execution")

    parser.add_argument("--exec-id", type=int, default=0,
                        help="Execution id for a given scenario")
    parser.add_argument("--nbexecs", type=int, default=30,
                        help="number of simulation executions")
    parser.add_argument("--inf-exec-id", type=int, default=0,
                        help="Infimum execution id")
    parser.add_argument("--sup-exec-id", type=int, default=299,
                        help="Supremum execution id")

    parser.add_argument("--data-src", type=str, default="hpcc_0.5",
                        help="source domain whence data were drawn")

    parser.add_argument("--dirpath-data", type=str, default=Paths.DATA,
                        help="directory path of Pytrol's data")
    parser.add_argument("--dirpath-execs", type=str, default=Paths.EXECS,
                        help="directory path of executions files")
    parser.add_argument("--dirpath-stats", type=str,
                        default=Paths.LOCALSTATS,
                        help="directory path of scenarios' statistiques")
    parser.add_argument("--dirpath-models", type=str,
                        default=Paths.DIRPATHMODELS,
                        help="directory path of machine learning models")
    parser.add_argument("--dirpath-logs", type=str, default=Paths.LOGS,
                        help="path of the directory where saving logs of "
                             "executions")
    parser.add_argument("--dirpath-logs-bin", type=str, default=Paths.LOCALBIN,
                        help="path of the directory where saving bin " \
                             "logs of executions")
    parser.add_argument("--dirpath-logs-viidls", type=str,
                        default=Paths.LOCALVIIDLS,
                        help="path of the directory where saving viidls logs "
                             "of executions")
    parser.add_argument("--dirpath-logs-vidls", type=str,
                        default=Paths.LOCALVIDLS,
                        help="path of the directory where saving vidls logs "
                             "of executions")
    args = parser.parse_args()

    return args
