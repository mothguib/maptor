# -*- coding: utf-8 -*-

import json
import sys

import numpy as np

from maptor.model import Paths

sys.path.append(Paths.LOCALPYTROL)
from pytrol.util import pathformatter as pf

statpath = Paths.STATS
maps = ["islands", "map_a", "grid"]
datasrc = ''
duration = 3000
# strts = ["hpcc_0.1", "hpcc_0.2", "hcc_0.2", "hpcc_0.5", "hpcc_0.8",
# "hpcc_0.9"]
# ies = ["hpme_0.2", "hple_0.2", "hpre_0.2", "rhpme_0.2", "rhple_0.2",
#        "rhpre_0.2"]
# datasrc = "hcc_0.2"
# strts = ies
strts = ["cr"]

nagts = [5, 10, 15, 25]

nexstatpath = ''

for strt in strts:
    av_mtrs = np.zeros([0, 6])
    for m in maps:
        for n in nagts:
            # Normalised execution's statistiques' file path
            nexstatpath = pf.build_stat_path(tpl=m, strt=strt,
                                             nagts=n,
                                             statpath=statpath,
                                             datasrc=datasrc, nrm=True,
                                             duration=duration)

            with open(nexstatpath, 'r') as s:
                vs = json.load(s)[0]
                av_mtrs = np.append(av_mtrs, [vs], axis=0)

    # Means of each criterion
    means = np.mean(av_mtrs, axis=0)

    print("{}:\n\t{}".format(strt, means))
