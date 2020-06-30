# -*- coding: utf-8 -*-

# N.B.: Statistics must be generated before plotting results

import os
import sys

# Adds the current package to the Python's path to run it from anywhere in the
# terminal
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from maptor import Paths
from maptor.control.StatisticComputer import StatisticComputer
from maptor.control import plotter as pl

log_fp = Paths.DATA + "/logs/"
statpath = Paths.DATA + "/stats/"

nagts = [5, 10, 15, 25]

# -------------------------------------------

# Best IE 0.2, Best RIE 0.2
'''
# Representative strategies
reps = ["hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Representatives' names
# legend_reps = ['hcc 0.2', 'cr']
legend_reps = ["hpcc", "cr"]
# Best ie strategy among
ies = ["hpme_0.2", "hple_0.2", "hpre_0.2"]
# Best rie strategy among
ries = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]
# Multi-best-strategy among
strts_1 = [ies, ries]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2", "hcc_0.2"]
# "Multi-best-among" names
# legend_strts_1 = ["best ie 0.2", "best rie 0.2"]
legend_strts_1 = ["best ie", "best rie"]
maps = ["map_a", "islands", "grid"]

for c in 0, 1, 2, 3:
    for m in maps:
        pl.best_var_best_strt(reps,
                              strts_1,
                              [],
                              legend_reps=legend_reps,
                              legend_strts_1=legend_strts_1,
                              statpath=statpath,
                              ds_strts_1=ds_strts_1,
                              ds_reps=ds_reps,
                              mtr=c,
                              maps=[m],
                              nagts=nagts,
                              display_value=False,
                              dsn=True)
'''

# Best RIE 0.2, Best IRIE 0.2, RMAPLPM and HPCC 0.5 and CR
# Representative strategies
reps = ["hpcc_0.5", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# `reps`'s legend
legend_reps = ['hpcc', 'cr']
# Best rie strategy among
ries_0_2 = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]
# Best irie strategy among
iries_0_2 = ["rhpme_0.2_i_14", "rhple_0.2_i_14", "rhpre_0.2_i_14"]
# Multi-best-strategy among
strts_1 = [ries_0_2, iries_0_2]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2", "hcc_0.2"]
# "Multi-best-among" names
legend_strts_1 = ["best rie", "best i-rie"]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = ["rmaplpm"]
ds_strts_2 = ["hpcc_0.5"]
legend_strts_2 = ["rampager"]
maps = ["map_a", "islands", "grid"]


for c in 0, 1, 2, 3:
    for m in maps:
        pl.best_var_best_strt(reps,
                              strts_1,
                              strts_2,
                              legend_reps=legend_reps,
                              legend_strts_1=legend_strts_1,
                              legend_strts_2=legend_strts_2,
                              statpath=statpath,
                              ds_strts_1=ds_strts_1,
                              ds_strts_2=ds_strts_2,
                              ds_reps=ds_reps,
                              mtr=c,
                              maps=[m],
                              nagts=nagts,
                              display_value=False,
                              dsn=True)

# Best RIE 0.5, Best IRIE 0.5, Best RIE 0.2, Best IRIE 0.2
'''
# Representative strategies
reps = ["hpcc_0.5", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Best rie strategy among
ries_0_2 = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]
# Best irie strategy among
iries_0_2 = ["rhpme_0.2_i_14", "rhple_0.2_i_14", "rhpre_0.2_i_14"]
# Best rie strategy among
ries_0_5 = ["rhpme_0.5", "rhple_0.5", "rhpre_0.5"]
# Best irie strategy among
iries_0_5 = ["rhpme_0.5_i_14", "rhple_0.5_i_14", "rhpre_0.5_i_14"]
# Multi-best-strategy among
strts_1 = [ries_0_2, iries_0_2, ries_0_5, iries_0_5]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2", "hcc_0.2", "hpcc_0.5", "hpcc_0.5"]
# "Multi-best-among" names
legend_strts_1 = ["best rie 0.2", "best i-rie 0.2", "best rie 0.5",
                  "best i-rie 0.5"]
strts_2 = []
maps = ["map_a", "islands", "grid"]


for c in 0, 1, 2, 3:
    for m in maps:
        pl.best_var_best_strt(reps,
                              strts_1,
                              strts_2,
                              legend_strts_1=legend_strts_1,
                              statpath=statpath,
                              ds_strts_1=ds_strts_1,
                              ds_reps=ds_reps,
                              mtr=c,
                              maps=[m],
                              nagts=nagts,
                              display_value=False,
                              dsn=True)
'''

# Best RIE 0.5, Best IRIE 0.5, Best RIE 0.2, Best IRIE 0.2 and RMAPLPM
'''
# Representative strategies
reps = ["hpcc_0.5", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Best rie strategy among
ries_0_2 = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]
# Best irie strategy among
iries_0_2 = ["rhpme_0.2_i_14", "rhple_0.2_i_14", "rhpre_0.2_i_14"]
# Best rie strategy among
ries_0_5 = ["rhpme_0.5", "rhple_0.5", "rhpre_0.5"]
# Best irie strategy among
iries_0_5 = ["rhpme_0.5_i_14", "rhple_0.5_i_14", "rhpre_0.5_i_14"]
# Multi-best-strategy among
strts_1 = [ries_0_2, iries_0_2, ries_0_5, iries_0_5]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2", "hcc_0.2", "hpcc_0.5", "hpcc_0.5"]
# "Multi-best-among" names
legend_strts_1 = ["best rie 0.2", "best i-rie 0.2", "best rie 0.5",
                  "best i-rie 0.5"]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = ["rmaplpm"]
ds_strts_2 = ["hpcc_0.5"]
legend_strts_2 = ["rampager-2-50"]
maps = ["map_a", "islands", "grid"]


for c in 0, 1, 2, 3:
    for m in maps:
        pl.best_var_best_strt(reps,
                              strts_1,
                              strts_2,
                              legend_strts_1=legend_strts_1,
                              legend_strts_2=legend_strts_2,
                              statpath=statpath,
                              ds_strts_1=ds_strts_1,
                              ds_strts_2=ds_strts_2,
                              ds_reps=ds_reps,
                              mtr=c,
                              maps=[m],
                              nagts=nagts,
                              display_value=False,
                              dsn=True)

# Multi-best-strategy among
strts_1 = [ries_0_5, iries_0_5]
# `multi_best_strt`'s data source
ds_strts_1 = ["hpcc_0.5", "hpcc_0.5"]
# "Multi-best-among" names
legend_strts_1 = ["best rie 0.5", "best i-rie 0.5"]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = ["rmaplpm"]
ds_strts_2 = ["hpcc_0.5"]
legend_strts_2 = ["rampager-2-50"]
maps = ["map_b", "circle"]

for c in 0, 1, 2, 3:
    for m in maps:
        pl.best_var_best_strt(reps,
                              strts_1,
                              strts_2,
                              legend_strts_1=legend_strts_1,
                              legend_strts_2=legend_strts_2,
                              statpath=statpath,
                              ds_strts_1=ds_strts_1,
                              ds_strts_2=ds_strts_2,
                              ds_reps=ds_reps,
                              mtr=c,
                              maps=[m],
                              nagts=nagts,
                              display_value=False,
                              dsn=True)

legend_strts_2 = ["rampager-2-49"]
maps = ["corridor"]

for c in 0, 1, 2, 3:
    for m in maps:
        pl.best_var_best_strt(reps,
                              strts_1,
                              strts_2,
                              legend_strts_1=legend_strts_1,
                              legend_strts_2=legend_strts_2,
                              statpath=statpath,
                              ds_strts_1=ds_strts_1,
                              ds_strts_2=ds_strts_2,
                              ds_reps=ds_reps,
                              mtr=c,
                              maps=[m],
                              nagts=nagts,
                              display_value=False,
                              dsn=True)

'''

# RMAPLPM, A
'''
datasrc = "hpcc_0.5"
# Representative strategies
reps = [datasrc, "cr"]
compared = ["rmaplpm_1-50-5", "rmaplpm_2-50-5", "rmaplpm_3-50-5",
            "rmaplpm_4-50-5"]
legends = reps + ["rampager_1-50-5", "rampager_2-50-5", "rampager_3-50-5",
            "rampager_4-50-5"]
strts = reps + compared
datasrcs = ['', ''] + [datasrc] * len(compared)
for c in 0, 1, 2, 3:
    pl.plot_all(strts, statpath, mtr=c, maps=["map_a"], nagts=nagts,
                datasrcs=datasrcs, legend_strts=legends, display_value=False)
'''

# Best RLPM and RMAPLPM
'''
# Topologies
maps = ["map_a", "islands", "grid"]
# Representative strategies
reps = ["hpcc_0.5", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Muli-best variant: strategies which we shall display the best variant of
strts = ["rlpm", "rmaplpm"]
ds_strts = ["hcc_0.2", "hpcc_0.5"]
legend_strts = ["best rlpm (t.f. 0.2)", "rampager-2-50 (t.f. 0.5)"]


for c in 0, 1, 2, 3:
    for m in maps:
        pl.best_of_vars(reps,
                        strts,
                        statpath=statpath,
                        ds_reps=ds_reps,
                        ds_strts=ds_strts,
                        mtr=c,
                        maps=[m],
                        nagts=nagts,
                        legend_strts=legend_strts,
                        display_value=False,
                        dsn=True)

# Topologies
maps = ["map_b", "circle"]
# Muli-best variant: strategies which we shall display the best variant of
strts = ["rmaplpm"]
ds_strts = ["hpcc_0.5"]
legend_strts = ["rampager-2-50"]
for c in 0, 1, 2, 3:
    for m in maps:
        pl.best_of_vars(reps,
                        strts,
                        statpath=statpath,
                        ds_reps=ds_reps,
                        ds_strts=ds_strts,
                        mtr=c,
                        maps=[m],
                        nagts=nagts,
                        legend_strts=legend_strts,
                        display_value=False,
                        dsn=True)

# Topologies
maps = ["corridor"]
# Representative strategies
reps = ["hpcc_0.5", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Muli-best variant: strategies which we shall display the best variant of
strts = ["rmaplpm"]
ds_strts = ["hpcc_0.5"]
legend_strts = ["rampager-2-49"]
for c in 0, 1, 2, 3:
    for m in maps:
        pl.best_of_vars(reps,
                        strts,
                        statpath=statpath,
                        ds_reps=ds_reps,
                        ds_strts=ds_strts,
                        mtr=c,
                        maps=[m],
                        nagts=nagts,
                        legend_strts=legend_strts,
                        display_value=False,
                        dsn=True)
'''

# Best RLPM
'''
# Topologies
maps = ["map_a", "islands", "grid"]
# Representative strategies
reps = ["hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Muli-best variant: strategies which we shall display the best variant of
strts = ["rlpm"]
ds_strts = ["hcc_0.2"]

# c = 0
for c in 0, 1, 2, 3:
    pl.best_of_vars(reps,
                    strts,
                    statpath=statpath,
                    ds_reps=ds_reps,
                    ds_strts=ds_strts,
                    mtr=c,
                    maps=maps,
                    nagts=nagts,
                    display_value=False,
                    dsn=True)
'''

# HPCCs
'''
hpccs = ["hpcc_0.5", "hcc_0.2", "hpcc_0.1", "hpcc_0.2", "hpcc_0.8",
         "hpcc_0.9"]
maps = ["islands", "map_a", "grid"]
nagts = [5, 10, 15, 25]
for c in 0, 1, 2, 3:
    for m in maps:
        pl.plot_all(strts=hpccs, mtr=c, maps=[m], nagts=nagts,
                    statpath=statpath, nrm=True, display_value=False)
'''

'''
c = 3

# Representative strategies
reps = ["hpcc_0.5", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Best rie strategy among
ries_0_2 = ["rhpme_0.2"]
# Best irie strategy among
# Best rie strategy among
ries_0_5 = ["rhpme_0.5"]
# Best irie strategy among
# Multi-best-strategy among
strts_1 = [ries_0_2, ries_0_5]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2", "hpcc_0.5"]
# "Multi-best-among" names
legend_strts_1 = ["best rie 0.2", "best rie 0.5"]

# Muli-best variant: strategies which we shall display the best variant of
strts_2 = ["rmaplpm"]
ds_strts_2 = ["hpcc_0.5"]
legend_strts_2 = ["rampager-2-50"]
maps = ["map_a", "islands", "grid"]


for m in maps:
    pl.best_var_best_strt(reps,
                          strts_1,
                          strts_2,
                          legend_strts_1=legend_strts_1,
                          legend_strts_2=legend_strts_2,
                          statpath=statpath,
                          ds_strts_1=ds_strts_1,
                          ds_strts_2=ds_strts_2,
                          ds_reps=ds_reps,
                          mtr=c,
                          maps=[m],
                          nagts=nagts,
                          display_value=False,
                          dsn=True)

# Multi-best-strategy among
strts_1 = [ries_0_5]
# `multi_best_strt`'s data source
ds_strts_1 = ["hpcc_0.5", "hpcc_0.5"]
# "Multi-best-among" names
legend_strts_1 = ["best rie 0.5", "best i-rie 0.5"]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = ["rmaplpm"]
ds_strts_2 = ["hpcc_0.5"]
legend_strts_2 = ["rampager-2-50"]
maps = ["map_b", "circle"]

for m in maps:
    pl.best_var_best_strt(reps,
                          strts_1,
                          strts_2,
                          legend_strts_1=legend_strts_1,
                          legend_strts_2=legend_strts_2,
                          statpath=statpath,
                          ds_strts_1=ds_strts_1,
                          ds_strts_2=ds_strts_2,
                          ds_reps=ds_reps,
                          mtr=c,
                          maps=[m],
                          nagts=nagts,
                          display_value=False,
                          dsn=True)

legend_strts_2 = ["rampager-2-49"]
maps = ["corridor"]

for m in maps:
    pl.best_var_best_strt(reps,
                          strts_1,
                          strts_2,
                          legend_strts_1=legend_strts_1,
                          legend_strts_2=legend_strts_2,
                          statpath=statpath,
                          ds_strts_1=ds_strts_1,
                          ds_strts_2=ds_strts_2,
                          ds_reps=ds_reps,
                          mtr=c,
                          maps=[m],
                          nagts=nagts,
                          display_value=False,
                          dsn=True)
'''
