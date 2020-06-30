# -*- coding: utf-8 -*-

# Converting maps into a set of size-2 sequences where each one stands for
#  an edge

# import os
# import sys
# Adds the current package to the Python's path to run it from anywhere in the
# terminal
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from maptor.control.StatisticComputer import StatisticComputer
from maptor.util import argsparser as parser

args = parser.parse_args()

log_fp = args.dirpath_logs
statpath = args.dirpath_stats

# datasrc = args.datasrc
# datasrc = "hcc_0.2"
datasrc = "hpcc_0.5"

# nagts = [1, 5, 10, 15, 25]
nagts = [5, 10, 15, 25]
# nagts = [15]

# maps = ["islands", "map_a", "grid"]
# maps = ["map_a", "islands", "grid", "circle", "map_b", "corridor"]
# maps = ["map_a"]
# maps = ["islands", "grid", "circle", "map_b"]
# maps = ["corridor"]

sc = StatisticComputer(log_fp, statpath)

# maps = ["map_a", "islands", "grid", "circle", "map_b"]
# nagts = [5, 10, 15, 25]
# datasrc = "hpcc_0.5"
# sc.compute_for_configs("rmaplpm_2-50-5", maps=maps, nagts=nagts,
#                        datasrc=datasrc)

# maps = ["corridor"]
# nagts = [5, 10, 15, 25]
# datasrc = "hpcc_0.5"
# sc.compute_for_configs("rmaplpm_2-49-5", maps=maps, nagts=nagts,
#                        datasrc=datasrc)

# maps = ["map_a"]
# nagts = [5, 10, 15, 25]
# sc.compute_for_configs("rmaplpm_4-50-5", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("rmaplpm_3-50-5", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("rmaplpm_2-50-5", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("rmaplpm_1-50-5", maps=maps, nagts=nagts,
#                        datasrc=datasrc)

maps = ["map_a", "islands", "grid"]
nagts = [5, 10, 15, 25]
datasrc = "hcc_0.2"
sc.compute_for_configs("rlpm_50-2--1", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("rlpm_4-10--1", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("rlpm_3-50--1", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("rlpm_2-50--1", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("rlpm_1-50--1", maps=maps, nagts=nagts,
                       datasrc=datasrc)

# maps = ["map_a"]
# nagts = [5, 10, 15, 25]
# for datasrc in ["hcc_0.2", "hpcc_0.2", "hpcc_0.5"]:
#     sc.compute_for_configs("rlpm_adagrad_pre_100_50-2--1", maps=["map_a"],
#                            nagts=[15], datasrc=datasrc)
#     sc.compute_for_configs("rlpm_adagrad_pre_100_4-10--1", maps=["map_a"],
#                            nagts=[15], datasrc=datasrc)
#     sc.compute_for_configs("rlpm_adagrad_pre_100_3-50--1", maps=["map_a"],
#                            nagts=[15], datasrc=datasrc)
#     sc.compute_for_configs("rlpm_adagrad_pre_100_2-50--1", maps=["map_a"],
#                            nagts=[15], datasrc=datasrc)
#     sc.compute_for_configs("rlpm_adagrad_pre_100_1-50--1", maps=["map_a"],
#                            nagts=[15], datasrc=datasrc)
#
#     sc.compute_for_configs("rlpm_sgd_pre_100_50-2--1", maps=["map_a"],
#                            nagts=[15], datasrc=datasrc)
#     sc.compute_for_configs("rlpm_sgd_pre_100_4-10--1", maps=["map_a"],
#                            nagts=[15], datasrc=datasrc)
#     sc.compute_for_configs("rlpm_sgd_pre_100_3-50--1", maps=["map_a"],
#                            nagts=[15], datasrc=datasrc)
#     sc.compute_for_configs("rlpm_sgd_pre_100_2-50--1", maps=["map_a"],
#                            nagts=[15], datasrc=datasrc)
#     sc.compute_for_configs("rlpm_sgd_pre_100_1-50--1", maps=["map_a"],
#                            nagts=[15], datasrc=datasrc)

# maps = ["map_a"]
# nagts = [15]
# datasrc = "hpcc_0.2"
# sc.compute_for_configs("rlpm_sgd_no_pre_100_50-2--1", maps=["map_a"],
#                        nagts=[15], datasrc=datasrc)
# sc.compute_for_configs("rlpm_sgd_no_pre_100_4-10--1", maps=["map_a"],
#                        nagts=[15], datasrc=datasrc)
# sc.compute_for_configs("rlpm_sgd_no_pre_100_3-50--1", maps=["map_a"],
#                        nagts=[15], datasrc=datasrc)
# sc.compute_for_configs("rlpm_sgd_no_pre_100_2-50--1", maps=["map_a"],
#                        nagts=[15], datasrc=datasrc)
# sc.compute_for_configs("rlpm_sgd_no_pre_100_1-50--1", maps=["map_a"],
#                        nagts=[15], datasrc=datasrc)

# maps = ["islands", "map_a", "grid", "map_b", "circle", "corridor"]
# nagts = [5, 10, 15, 25]
# sc.compute_for_configs("hcc_0.2", maps=maps, nagts=nagts)
# sc.compute_for_configs("hpcc_0.2", maps=maps, nagts=nagts)
# sc.compute_for_configs("hpcc_0.9", maps=maps, nagts=nagts)
# sc.compute_for_configs("hpcc_0.1", maps=maps, nagts=nagts)
# sc.compute_for_configs("hpcc_0.8", maps=maps, nagts=nagts)
# sc.compute_for_configs("hpcc_0.5", maps=maps, nagts=nagts)
# sc.compute_for_configs("cr", maps=maps, nagts=nagts)
# sc.compute_for_configs("hpcc_0.2", maps=["grid"], nagts=nagts)

# maps = ["islands", "map_a", "grid"]
# nagts = [5, 10, 15, 25]
# datasrc = 'hcc_0.2'
# sc.compute_for_configs("rhple_0.2_i_14", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("rhpre_0.2_i_14", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("rhpme_0.2_i_14", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("hple_0.2_i_14", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("hpre_0.2_i_14", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("hpme_0.2_i_14", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("rhple_0.2", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("rhpre_0.2", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("rhpme_0.2", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("hple_0.2", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("hpre_0.2", maps=maps, nagts=nagts,
#                        datasrc=datasrc)
# sc.compute_for_configs("hpme_0.2", maps=maps, nagts=nagts,
#                        datasrc=datasrc)


# sc.compute_for_configs("rlpm_1-1--1")
# sc.compute_for_configs("rlpm_2-2--1")
# sc.compute_for_configs("lpm_4-10--1")
# sc.compute_for_configs("rhple_0.2_i_ov_wtc_14", maps=maps, nagts=nagts)
# sc.compute_for_configs("rhpre_0.2_i_ov_wtc_14", maps=maps, nagts=nagts)
# sc.compute_for_configs("rhpme_0.2_i_ov_wtc_14", maps=maps, nagts=nagts)
# sc.compute_for_configs("hple_0.2_i_ov_wtc_14", maps=maps, nagts=nagts)
# sc.compute_for_configs("hpre_0.2_i_ov_wtc_14", maps=maps, nagts=nagts)
# sc.compute_for_configs("hpme_0.2_i_ov_wtc_14", maps=maps, nagts=nagts)

# sc.compute_for_configs("rhple_0.2_i_ov_wtc_wi_14", maps=maps, nagts=nagts)
# sc.compute_for_configs("rhpre_0.2_i_ov_wtc_wi_14", maps=maps, nagts=nagts)
# sc.compute_for_configs("rhpme_0.2_i_ov_wtc_wi_14", maps=maps, nagts=nagts)

'''
maps = ["islands", "map_a", "grid"]
datasrc = "hcc_0.2"
nagts = [5, 10, 15, 25]
sc.compute_for_configs("hple_0.2_i_ov_wtc_wi_14", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("hpre_0.2_i_ov_wtc_wi_14", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("hpme_0.2_i_ov_wtc_wi_14", maps=maps, nagts=nagts,
                       datasrc=datasrc)
'''

'''
maps = ["islands", "map_a", "grid"]
datasrc = "hcc_0.2"
nagts = [5, 10, 15, 25]
sc.compute_for_configs("rhple_0.2_i_14", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("rhpre_0.2_i_14", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("rhpme_0.2_i_14", maps=maps, nagts=nagts,
                       datasrc=datasrc)
'''

'''
maps = ["islands", "map_a", "grid"]
datasrc = "hcc_0.2"
nagts = [5, 10, 15, 25]
sc.compute_for_configs("hple_0.2_i_14", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("hpre_0.2_i_14", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("hpme_0.2_i_14", maps=maps, nagts=nagts,
                       datasrc=datasrc)
'''

'''
maps = ["islands", "map_a", "grid"]
datasrc = "hcc_0.2"
nagts = [5, 10, 15, 25]
sc.compute_for_configs("rhple_0.2", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("rhpre_0.2", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("rhpme_0.2", maps=maps, nagts=nagts,
                       datasrc=datasrc)
'''

'''
maps = ["islands", "map_a", "grid"]
datasrc = "hcc_0.2"
nagts = [5, 10, 15, 25]
sc.compute_for_configs("hple_0.2", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("hpre_0.2", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("hpme_0.2", maps=maps, nagts=nagts,
                       datasrc=datasrc)
'''

'''
maps = ["islands", "map_a", "grid", "map_b", "circle", "corridor"]
datasrc = "hpcc_0.5"
nagts = [5, 10, 15, 25]
sc.compute_for_configs("rhple_0.5", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("rhpre_0.5", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("rhpme_0.5", maps=maps, nagts=nagts,
                       datasrc=datasrc)
'''

'''
maps = ["islands", "map_a", "grid", "map_b", "circle", "corridor"]
datasrc = "hpcc_0.5"
nagts = [5, 10, 15, 25]
sc.compute_for_configs("rhple_0.5_i_14", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("rhpre_0.5_i_14", maps=maps, nagts=nagts,
                       datasrc=datasrc)
sc.compute_for_configs("rhpme_0.5_i_14", maps=maps, nagts=nagts,
                       datasrc=datasrc)
'''