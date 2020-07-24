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

# maps = ["circle", "map_b", "corridor"]
maps = ["islands", "map_a", "grid"]
# maps = ["islands", "map_a", "grid", "circle", "map_b", "corridor"]
# maps = ["map_a"]

# Instantiation of the statistic computer
sc = StatisticComputer(log_fp, statpath)

# datasrc = "hcc_0.2"
datasrc = "hpcc_0.5"

# Representative strategies
reps = [datasrc, "cr"]

# Best ie strategy among
best_among_rie = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]

# `best_among_rie`'s Data source
best_among_rie_ds = [0.2] * len(best_among_rie)

# Best rie strategy among
best_among_irie = ["rhpme_0.2_i_14", "rhple_0.2_i_14", "rhpre_0.2_i_14"]

# `best_among_irie`'s Data source
best_among_irie_ds = [0.2] * len(best_among_irie)

# Multi-best-strategy among
multi_best_strt = [best_among_rie, best_among_irie]

# `multi_best_strt`'s data source
multi_best_strt_ds = [best_among_rie_ds, best_among_irie_ds]

# "Multi-best-among" names
banames = ["rie", "i-rie"]

# Best variant: strategy that we shall display the best variant of
# best_variant = ["rlpm"]
multi_best_variant = ["rmaplpm", "rlpm"]

# Compared strategies: strategies which are compared with the representatives
# compared = ["rhple_0.2", "rhple_0.2_i_14",
#            "rhple_0.2_i_ov_14", "rhple_0.2_i_ov_wtc_14"]

# compared = ["hpme_i_0.2", "hple_i_0.2", "hpre_i_0.2", "rhpme_i_0.2",
# "rhple_i_0.2", "rhpre_i_0.2"]

# compared = ["hpme_0.2", "hple_0.2", "hpre_0.2", "rhpme_0.2", "rhple_0.2",
# "rhpre_0.2"]

# compared = ["rhple_0.2", "rhpre_0.2", "rhpme_0.2"]

compared = ["rmaplpm_1-50-5", "rmaplpm_2-50-5", "rmaplpm_3-50-5",
            "rmaplpm_4-50-5"]

# compared = ["rlpm_sgd_pre_100_4-10--1", "rlpm_sgd_pre_100_1-50--1",
#             "rlpm_sgd_pre_100_2-50--1", "rlpm_sgd_pre_100_3-50--1",
#             "rlpm_sgd_pre_100_50-2--1",
#             "rlpm_adagrad_pre_100_4-10--1", "rlpm_adagrad_pre_100_1-50--1",
#             "rlpm_adagrad_pre_100_2-50--1", "rlpm_adagrad_pre_100_3-50--1",
#             "rlpm_adagrad_pre_100_50-2--1"]

# compared = ["rlpm_sgd_no_pre_4-10--1", "rlpm_sgd_no_pre_1-50--1",
#             "rlpm_sgd_no_pre_2-50--1", "rlpm_sgd_no_pre_3-50--1",
#             "rlpm_sgd_no_pre_50-2--1",
#             "rlpm_sgd_pre_4-10--1", "rlpm_sgd_pre_1-50--1",
#             "rlpm_sgd_pre_2-50--1", "rlpm_sgd_pre_3-50--1",
#             "rlpm_sgd_pre_50-2--1",
#             "rlpm_adagrad_pre_4-10--1", "rlpm_adagrad_pre_1-50--1",
#             "rlpm_adagrad_pre_2-50--1", "rlpm_adagrad_pre_3-50--1",
#             "rlpm_adagrad_pre_50-2--1"]

# compared = ["rlpm_4-10--1", "rlpm_1-50--1", "rlpm_2-50--1", "rlpm_3-50--1",
#             "rlpm_50-2--1"]

hpccs = ["hpcc_0.5", "cr", "hcc_0.2", "hpcc_0.1", "hpcc_0.2", "hpcc_0.8",
         "hpcc_0.9"]

strts = reps + compared
# strts = ["hpcc_0.5", "cr", "hcc_0.2", "hpcc_0.1", "hpcc_0.2", "hpcc_0.8",
#         "hpcc_0.9"]

datasrcs = ['', ''] + [datasrc] * len(compared)
adpc_strts = ["hpcc_0.5", "hcc_0.2"]
ds_reps = ['', '']

# -------------------------------------------

# IEs and RIEs

'''
nagts = [5, 10, 15, 25]
# Representative strategies
reps = ["hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Best ie strategy among
ies = ["hple_0.2", "hpre_0.2"]
ries = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]
# `ies`'s data source
ds_ies = ['hcc_0.2'] * len(ies)
ds_ries = ['hcc_0.2'] * len(ries)
datasources = ds_reps + ds_ies + ds_ries
strts = reps + ies + ries

for c in range(3):
    for m in ["islands", "map_a", "grid"]:
        pl.plot_all(strts, mtr=c, maps=[m], nagts=nagts, statpath=statpath, \
                    datasrcs=datasources, display_value=False)
'''

# Best RIE 0.2, Best IRIE 0.2 and RMAPLPM
'''
# Representative strategies
reps = ["hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Best ie strategy among
ies = ["hpme_0.2", "hple_0.2", "hpre_0.2"]
# Best rie strategy among
ries = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]
# Multi-best-strategy among
strts_1 = [ies, ries]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2", "hcc_0.2"]
# "Multi-best-among" names
legend_strts_1 = ["best ie 0.2", "best rie 0.2"]
maps = ["map_a", "islands", "grid"]

for c in 0, 1, 2, 3:
    for m in maps:
        pl.best_var_best_strt(reps,
                              strts_1,
                              [],
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

# RMAPLPM, RLPM, RHPME
'''
maps = ["islands", "map_a", "grid"]
compared = ["rlpm_1-50--1", "rmaplpm_2-50-5", "rhpme_0.2", "rhpme_0.2_i_14"]
datasrcs = ['', ''] + ["hcc_0.2", "hpcc_0.5", "hcc_0.2"] * len(compared)

# maps = ["circle", "map_b"]
# compared = ["rmaplpm_2-50-5"]
# datasrcs = ['', ''] + ["hpcc_0.5"] * len(compared)

# maps = ["corridor"]
# compared = ["rmaplpm_2-49-5"]
# datasrcs = ['', ''] + ["hpcc_0.5"] * len(compared)

# Representative strategies
reps = [datasrc, "cr"]
strts = reps + compared
for c in 0, 2, 3:
    for m in maps:
        pl.plot_all(strts, statpath, mtr=c, maps=[m], nagts=nagts,
                    datasrcs=datasrcs)
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

# RIE, IRIE, RLPM
'''
reps = ["hcc_0.2", "cr"]
ds_reps = ['', '']
# Best rie strategy among
ries = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]
# Best irie strategy among
iries = ["rhpme_0.2_i_14", "rhple_0.2_i_14", "rhpre_0.2_i_14"]
# Multi-best-strategy among
strts_1 = [ries, iries]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2", "hcc_0.2"]
# "Multi-best-among" names
legend_strts_1 = ["rie", "i-rie"]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = ["rlpm"]
ds_strts_2 = ["hcc_0.2"]

for m in ["map_a", "islands", "grid"]:
    pl.best_var_best_strt(reps,
                          strts_1,
                          strts_2,
                          legend_strts_1=legend_strts_1,
                          statpath=statpath,
                          ds_strts_1=ds_strts_1,
                          ds_strts_2=ds_strts_2,
                          ds_reps=ds_reps,
                          mtr=0,
                          maps=[m],
                          nagts=nagts,
                          display_value=True,
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
                        display_value=True,
                        dsn=True)
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
legend_strts = ["best rlpm (t.f. 0.2)", "best rampager (t.f. 0.5)"]

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
maps = ["map_b", "circle", "corridor"]
# Representative strategies
reps = ["hpcc_0.5", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Muli-best variant: strategies which we shall display the best variant of
strts = ["rmaplpm"]
ds_strts = ["hpcc_0.5"]
legend_strts = ["best rampager (t.f. 0.5)"]
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

# Best IE 0.2, Best RLPM, Best RMAPLPM
'''
# Topologies
maps = ["map_a", "islands", "grid"]
# Representative strategies
reps = ["hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Best rie strategy among
ies = ["hpme_0.2", "hple_0.2", "hpre_0.2"]
# Multi-best-strategy among
strts_1 = [ies]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2"] * len(strts_1)
# "Multi-best-among" names
legend_strts_1 = ["ie 0.2",]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = ["rlpm", "rmaplpm"]
ds_strts_2 = ["hcc_0.2", "hpcc_0.5"]
legend_strts_2 = ["best rlpm (t.f. 0.2)", "best rmaplpm (t.f. 0.5)"]

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

# Best RIE, Best IRIE, Best RLPM, Best RMAPLPM
'''
# Topologies
maps = ["map_a", "islands", "grid"]
# Representative strategies
reps = ["hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Best rie strategy among
ries = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]
# Best irie strategy among
iries = ["rhpme_0.2_i_14", "rhple_0.2_i_14", "rhpre_0.2_i_14"]
# Multi-best-strategy among
strts_1 = [ries, iries]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2"] * len(strts_1)
# "Multi-best-among" names
legend_strts_1 = ["rie 0.2", "i-rie 0.2"]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = ["rlpm", "rmaplpm"]
ds_strts_2 = ["hcc_0.2", "hpcc_0.5"]
legend_strts_2 = ["best rlpm (t.f. 0.2)", "best rmaplpm (t.f. 0.5)"]

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


# Topologies
maps = ["map_b", "circle", "corridor"]
# Representative strategies
reps = ["hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Best rie strategy among
ries = ["rhpme_0.5", "rhple_0.5", "rhpre_0.5"]
# Best irie strategy among
iries = ["rhpme_0.5_i_14", "rhple_0.5_i_14", "rhpre_0.5_i_14"]
# Multi-best-strategy among
strts_1 = [ries, iries]
# `multi_best_strt`'s data source
ds_strts_1 = ["hpcc_0.5"] * len(strts_1)
# "Multi-best-among" names
legend_strts_1 = ["rie 0.5", "i-rie 0.5"]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = ["rmaplpm"]
ds_strts_2 = ["hpcc_0.5"]
legend_strts_2 = ["best rmaplpm (t.f. 0.5)"]

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

# Best RIE 0.2
'''
# Representative strategies
reps = ["hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = [''] * len(reps)
# Best rie 0.2 strategy among
ries1 = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]
# Multi-best-strategy among
strts_1 = [ries1]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2"]
# "Multi-best-among" names
legend_strts_1 = ["best rie 0.2"]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = []
ds_strts_2 = []
strts_2 = []
ds_strts_2 = []

for c in 0, 1, 2, 3:
    for m in ["map_a", "islands", "grid"]:
        pl.best_var_best_strt(reps,
                              strts_1,
                              strts_2,
                              legend_strts_1=legend_strts_1,
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

# Best RIE 0.2 vs. Best IRIE 0.2
'''
# Representative strategies
reps = ["hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = [''] * len(reps)
# Best rie 0.2 strategy among
ries = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]
# Best rie 0.5 strategy among
iries = ["rhpme_0.2_i_14", "rhple_0.2_i_14", "rhpre_0.2_i_14"]
# Multi-best-strategy among
strts_1 = [ries, iries]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2", "hcc_0.2"]
# "Multi-best-among" names
legend_strts_1 = ["best rie 0.2", "best i-rie 0.2"]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = []
ds_strts_2 = []
strts_2 = []
ds_strts_2 = []

for c in 0, 1, 2, 3:
    for m in ["map_a", "islands", "grid"]:
        pl.best_var_best_strt(reps,
                              strts_1,
                              strts_2,
                              legend_strts_1=legend_strts_1,
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

# Best RIE 0.2 vs. Best RIE 0.5
'''
# Representative strategies
reps = ["hpcc_0.5", "hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = [''] * len(reps)
# Best rie 0.2 strategy among
ries1 = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]
# Best rie 0.5 strategy among
ries2 = ["rhpme_0.5", "rhple_0.5", "rhpre_0.5"]
# Multi-best-strategy among
strts_1 = [ries1, ries2]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2", "hpcc_0.5"]
# "Multi-best-among" names
legend_strts_1 = ["best rie 0.2", "best rie 0.5"]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = []
ds_strts_2 = []
strts_2 = []
ds_strts_2 = []

for c in 0, 1, 2, 3:
    for m in ["map_a", "islands", "grid"]:
        pl.best_var_best_strt(reps,
                              strts_1,
                              strts_2,
                              legend_strts_1=legend_strts_1,
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

# Best IRIE 0.2 vs. Best IRIE 0.5
'''
# Representative strategies
reps = ["hpcc_0.5", "hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = [''] * len(reps)
# Best rie 0.2 strategy among
iries1 = ["rhpme_0.2_i_14", "rhple_0.2_i_14", "rhpre_0.2_i_14"]
# Best rie 0.5 strategy among
iries2 = ["rhpme_0.5_i_14", "rhple_0.5_i_14", "rhpre_0.5_i_14"]
# Multi-best-strategy among
strts_1 = [iries1, iries2]
# `multi_best_strt`'s data source
ds_strts_1 = ["hcc_0.2", "hpcc_0.5"]
# "Multi-best-among" names
legend_strts_1 = ["best i-rie 0.2", "best i-rie 0.5"]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = []
ds_strts_2 = []
strts_2 = []
ds_strts_2 = []

for c in 0, 1, 2, 3:
    for m in ["map_a", "islands", "grid"]:
        pl.best_var_best_strt(reps,
                              strts_1,
                              strts_2,
                              legend_strts_1=legend_strts_1,
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

# Best RIE 0.5 vs. Best IRIE 0.5
'''
# Representative strategies
reps = ["hpcc_0.5", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Best rie strategy among
ries = ["rhpme_0.5", "rhple_0.5", "rhpre_0.5"]
# Best irie strategy among
iries = ["rhpme_0.5_i_14", "rhple_0.5_i_14", "rhpre_0.5_i_14"]
# Multi-best-strategy among
strts_1 = [ries, iries]
# `multi_best_strt`'s data source
ds_strts_1 = ["hpcc_0.5", "hpcc_0.5"]
# "Multi-best-among" names
legend_strts_1 = ["best rie 0.5", "best i-rie 0.5"]
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = []
ds_strts_2 = []

for c in 0, 1, 2, 3:
    for m in ["map_a", "islands", "grid"]:
        pl.best_var_best_strt(reps,
                              strts_1,
                              strts_2,
                              legend_strts_1=legend_strts_1,
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
# Muli-best variant: strategies which we shall display the best variant of
strts_2 = ["rmaplpm"]
ds_strts_2 = ["hpcc_0.5"]
legend_strts_2 = ["best rampager (t.f. 0.5)"]
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
legend_strts_2 = ["best rampager (t.f. 0.5)"]
maps = ["map_b", "circle", "corridor"]

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

# RHPME, RHPLE, RHPRE
'''
nagts = [5, 10, 15, 25]
# Representative strategies
reps = ["hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Best ie strategy among
ies = ["rhpme_0.2", "rhple_0.2", "rhpre_0.2"]
# `ies`'s data source
ds_ies = ['hcc_0.2'] * len(ies)
datasources = ds_reps + ds_ies
strts = reps + ies

for c in range(3):
    for m in ["islands", "map_a", "grid"]:
        pl.plot_all(strts, mtr=c, maps=[m], nagts=nagts, statpath=statpath, \
                    datasrcs=datasources, display_value=False)
'''

# HPME, HPLE, HPRE
'''
nagts = [5, 10, 15, 25]
# Representative strategies
reps = ["hcc_0.2", "cr"]
# `reps`'s data source
ds_reps = ['', '']
# Best ie strategy among
ies = ["hpme_0.2", "hple_0.2", "hpre_0.2"]
# `ies`'s data source
ds_ies = ['hcc_0.2'] * len(ies)
datasources = ds_reps + ds_ies
strts = reps + ies

for c in range(3):
    for m in ["islands", "map_a", "grid"]:
        pl.plot_all(strts, mtr=c, maps=[m], nagts=nagts, statpath=statpath, \
                    datasrcs=datasources, display_value=False)
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

# Plotting the performances of the representatives and the best variant for
# each strategy populating `best_of` w.r.t the number of agents for each map
# and for all maps
'''
for m in maps:
    pl.best_of_vars(reps, multi_best_variant, mtr=0,
                                  maps=[m],
                                  nagts=nagts,
                                  statpath=statpath,
                                  ds_reps=ds_reps,
                                  adpc_strts=adpc_strts,
                                  value_fontsize=23,
                                  display_value=True,
                                  yoffset=15)
    
'''

'''
for m in maps:
    pl.best_of_vars(reps, multi_best_variant, mtr=1,
                                  maps=[m],
                                  nagts=nagts,
                                  statpath=statpath,
                                  ds_reps=ds_reps,
                                  adpc_strts=adpc_strts,
                                  value_fontsize=23,
                                  display_value=True,
                                  yoffset=5)
for m in maps:
    pl.best_of_vars(reps, multi_best_variant, mtr=2,
                                  maps=[m],
                                  nagts=nagts,
                                  statpath=statpath,
                                  ds_reps=ds_reps,
                                  adpc_strts=adpc_strts,
                                  value_fontsize=23,
                                  display_value=True,
                                  yoffset=15)

for m in maps:
    pl.best_of_vars_norm_max_idleness(reps, multi_best_variant, 
    mtr=3,
                                                    maps=[m],
                                                    nagts=nagts,
                                                    statpath=statpath,
                                                    ds_reps=ds_reps,
                                                    adpc_strts=adpc_strts,
                                                    value_fontsize=23,
                                                    display_value=True,
                                                    yoffset=15)
'''

'''
pl.plot_all(strts=strts, mtr=1, maps=maps, nagts=nagts,
            statpath=statpath, nrm=True)
'''

'''
for i in range(4):
    pl.plot_bar_chart_a_15(strts=strts, mtr=i, maps=["map_a"], nagts=[15],
                           statpath=statpath, nrm=True, adpcs=datasrcs)
'''

'''
for m in maps:
    pl.plot_all(strts=strts, mtr=0, maps=[m], nagts=nagts,
                statpath=statpath, nrm=True, display_text=False)
'''

'''
for s in ["rhple", "rhpme", "rhpre"]:
    compared = [s + "_0.2", s + "_0.2_i_14",
                s + "_0.2_i_ov_14", s + "_0.2_i_ov_wtc_14"]
    strts = reps + compared
    for m in maps:
        pl.plot_all(strts=strts, mtr=2, maps=[m], nagts=nagts)
'''

# Ploting Iav and QMI's values for all strategies populating `strts`
'''
for m in ["islands", "map_a", "grid"]:
    pl.plot_all(strts, mtr=0, maps=[m], nagts=nagts)
    pl.plot_all(strts, mtr=2, maps=[m], nagts=nagts)

pl.plot_all(strts, mtr=0, display_value=False, nagts=nagts)
pl.plot_all(strts, mtr=2, display_value=False, nagts=nagts)
'''

# Plotting the QMI values of the representatives and the best variant for each
# strategy populating `best_of` w.r.t the number of agents for each map
# and for all maps
'''
for m in ["islands", "map_a", "grid"]:
    pl.best_of_vars(reps, best_of, mtr=1, maps=[m])

pl.best_of_vars(reps, best_of, mtr=1)
'''

# Plots the I_av values of the representatives and the best variant for each
# strategy populating `best_of` w.r.t the number of agents for each map
# and for all maps
'''
for m in ["islands", "map_a", "grid"]:
    pl.best_of_vars(reps=reps, best_of=best_of, mtr=0,
                                     maps=[m], display_value=False)

pl.best_of_vars(reps=reps, best_of=best_of, mtr=0,
                                 display_value=False)
'''

# Plots all the representatives and compared strategies populating the list
# `compared` in the criterion space of metrics.
'''
for m in ["islands", "map_a", "grid"]:
    pl.plot_metric_space_reps_and_compared(compared, reps, maps=[m])

pl.plot_metric_space_reps_and_compared(compared)
'''

# Plots the representatives and the best variant for each strategy
# populating `best_of` in the criterion space of metrics.
'''
for m in ["islands", "map_a", "grid"]:
    pl.plot_metric_space_reps_best_of_var(best_of=best_of, reps=reps,
                                           maps=[m])

pl.plot_metric_space_reps_best_of_var(best_of=best_of, reps=reps)
'''

# Plotting all the compared strategies populating the list `compared` in the
# criterion space of metrics averaged over the population sizes.
'''
for m in ["islands", "map_a", "grid"]:
    pl.plot_metric_space_av_reps_and_compared(compared, reps, maps=[m])

pl.plot_metric_space_av_reps_and_compared(compared)
'''

'''
strts = ["hpcc", "cr", "rlpm_1-1--1", "rlpm_2-2--1", "rlpm_4-10--1",
         "rlpm_2-50--1", "rlpm_3-50--1", "rlpm_50-2--1"]

pl.plot_all(strts, 1)
pl.plot_all(strts, 2)
'''

'''
strts = ["hpcc", "cr",
         "rlpm_1-50--1", "rlpm_2-50--1", "rlpm_3-50--1", "rlpm_50-2--1"]

pl.plot(strts, 1)
pl.plot(strts, 2)

strts = ["hpcc", "cr",
         "rlpm_1-1--1", "rlpm_2-2--1", "rlpm_4-10--1", "rlpm_1-50--1"]

pl.plot(strts, 1)
pl.plot(strts, 2)

strts = ["hpcc", "cr",
         "rlpm_1-1--1", "rlpm_2-2--1", "rlpm_4-10--1", "rlpm_2-50--1"]

pl.plot(strts, 1)
pl.plot(strts, 2)

strts = ["hpcc", "cr",
         "rlpm_1-1--1", "rlpm_2-2--1", "rlpm_4-10--1", "rlpm_3-50--1"]

pl.plot(strts, 1)
pl.plot(strts, 2)

strts = ["hpcc", "cr",
         "rlpm_1-1--1", "rlpm_2-2--1", "rlpm_4-10--1", "rlpm_50-2--1"]

pl.plot(strts, 1)
pl.plot(strts, 2)
'''