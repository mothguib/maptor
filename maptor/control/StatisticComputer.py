# -*- coding: utf-8 -*-


import json
import os
import sys

import numpy as np

from maptor import NAGTS, MAPS, Paths

sys.path.append(Paths.LOCALPYTROL)
from pytrol.util import pathformatter as pf


class StatisticComputer:
    def __init__(self, log_fp: str, statpath: str):
        self.log_fp = log_fp + '/'
        self.statpath = statpath + '/'

    def compute_for_config(self, tpl: str,
                           strt: str,
                           nagts: int,
                           datasrc: str = None,
                           duration: int = 3000,
                           nbexecs: int = -1):

        if datasrc is None:
            datasrc = ''

        # The directory path of the current MAP configuration
        configpath = pf.build_logs_dirpath(tpl=tpl, strt=strt,
                                           nagts=nagts, datasrc=datasrc,
                                           duration=duration,
                                           logs_rep=self.log_fp)

        logs = list(filter(lambda fn: fn.endswith("log.json"),
                           os.listdir(configpath)
                           )
                    )

        if nbexecs == -1:
            nbexecs = len(logs)

        execs_mtrs = np.zeros([0, 6])

        for i, l in enumerate(logs):
            if i == nbexecs:
                break

            with open("{}/{}".format(configpath, l), 'r') as s:
                # Loading of metrics for each execution
                execs_mtrs = np.append(execs_mtrs, [json.load(s)[1]], axis=0)

        if not os.path.exists(self.statpath):
            os.makedirs(self.statpath)

        # Execution's statistiques' file path
        exstatpath = pf.build_stat_path(tpl=tpl, strt=strt, nagts=nagts,
                                        statpath=self.statpath,
                                        datasrc=datasrc, nrm=False,
                                        duration=duration)

        exstat_dirpath = os.path.dirname(exstatpath)

        if not os.path.exists(exstat_dirpath):
            os.makedirs(exstat_dirpath)

        # Normalised execution's statistiques' file path
        nexstatpath = pf.build_stat_path(tpl=tpl, strt=strt, nagts=nagts,
                                         statpath=self.statpath,
                                         datasrc=datasrc, nrm=True,
                                         duration=duration)

        # Means of each criterion
        means = np.mean(execs_mtrs, axis=0)

        # Standard deviation of each criterion
        std = np.std(execs_mtrs, axis=0) / np.sqrt(len(execs_mtrs))

        stats = np.array([means, std])

        # Normalised means
        nmeans = means * nagts
        # Normalised standard deviation
        nstd = std * nagts

        nstats = np.array([nmeans, nstd])

        with open(exstatpath, 'w') as s:
            json.dump(stats.tolist(), s)

        with open(nexstatpath, 'w') as s:
            json.dump(nstats.tolist(), s)

        print("Path: " + exstatpath)
        print("Map:" + tpl + ", " + strt + ", " + str(nagts) + " agents")
        print(stats)

        print("Path: " + nexstatpath)
        print("Map:" + tpl + ", " + strt + ", " + str(nagts) + " agents, "
                                                               "normalised")
        print(nstats)

        return stats, nstats

    def compute_for_configs(self,
                            strat: str,
                            datasrc: str = None,
                            maps: list = None,
                            nagts: list = None,
                            nbexecs: int = -1):

        if datasrc is None:
            datasrc = ''

        if maps is None:
            maps = MAPS

        if nagts is None:
            nagts = NAGTS

        for _m in maps:
            for na in nagts:
                self.compute_for_config(tpl=_m, strt=strat, nagts=na,
                                        nbexecs=nbexecs, datasrc=datasrc)
