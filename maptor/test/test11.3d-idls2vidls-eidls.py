# -*- coding: utf-8 -*-

# test11.3d-idls2vidls-eidls.py: for a given MAP scenario, generates on-vertex
# individual, real and estimated idleness sequences from the logs
# of 3D-position, individual, real and estimated idleness sequences

# ## USAGE

# `python test11.3d-idls2vidls-eidls.py --strategy <strt> --nagts <nagts>
# --duration <duration> --exec-id <exe_id> --map <map> --variant <variant>`

import sys
import time
import os

# Adds the current script's package to the Python's path to run the script
# from anywhere in the terminal
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")

from maptor import Paths
from maptor.util import argsparser
from maptor.control import LogProcessor

sys.path.append(Paths.LOCALPYTROL)
import pytrol.util.pathformatter as pf


def main(strt: str,
         nagts: int,
         duration: int,
         exec_id: int,
         tpl: str,
         variant: str = "0.2",
         soc_name: str = None,
         logs_rep: str = Paths.LOGS,
         viidls_rep: str = Paths.LOCALVIIDLS,
         vidls_rep: str = Paths.LOCALVIDLS,
         veidls_rep: str = Paths.LOCALVEIDLS):
    """


    :param exec_id:
    :type exec_id:
    :param nagts:
    :type nagts:
    :param veidls_rep:
    :type veidls_rep:
    :param variant:
    :type variant:
    :param strt:
    :type strt:
    :param soc_name:
    :type soc_name:
    :param duration:
    :type duration:
    :param tpl:
    :type tpl:object
    :param viidls_rep:
    :type viidls_rep:
    :param logs_rep:
    :type logs_rep:
    :param vidls_rep:
    :type vidls_rep:

    :return:
    :rtype:
    """

    # Log file path
    log_fp = pf.build_log_path(tpl=tpl, strt=strt, variant=variant,
                               nagts=nagts, exec_id=exec_id,
                               logs_rep=logs_rep, ext="log",
                               duration=duration,
                               soc_name=soc_name)

    # Agent log file path
    agts_log_fp = pf.build_log_path(tpl=tpl, strt=strt,
                                   variant=variant,
                                   nagts=nagts, exec_id=exec_id,
                                   logs_rep=logs_rep,
                                   ext="log.agts",
                                   duration=duration,
                                   soc_name=soc_name)

    # Agent estimate log file path
    est_log_fp = pf.build_log_path(tpl=tpl, strt=strt,
                                   variant=variant,
                                   nagts=nagts, exec_id=exec_id,
                                   logs_rep=logs_rep,
                                   ext="log.agts.est",
                                   duration=duration,
                                   soc_name=soc_name)

    start_time = time.time()

    veidls_fp, viidls_fp, vidls_fp = \
        LogProcessor.generate_save_veidls_and_idls(tpl=tpl,
                                              strt=strt,
                                              variant=variant,
                                              nagts=nagts,
                                              exec_id=exec_id,
                                              duration=duration,
                                              log_fp=log_fp,
                                              agts_log_fp=agts_log_fp,
                                              est_log_fp=est_log_fp,
                                              viidls_rep=viidls_rep,
                                              vidls_rep=vidls_rep,
                                              veidls_rep=veidls_rep,
                                              soc_name=soc_name)

    print("Inputs: ", log_fp, '\n', agts_log_fp, '\n', est_log_fp, '\n')
    print("Outputs: ", viidls_fp, '\n', veidls_fp, '\n', vidls_fp, '\n')

    end_time = time.time()

    print(end_time - start_time, ' s')
    print('\n')


args = argsparser.parse_args()

# Executed only if run as a script
if __name__ == "__main__":
    main(strt=args.strategy, nagts=args.nagts, duration=args.duration,
         exec_id=args.exec_id, tpl=args.map, soc_name=args.society,
         variant=args.variant)
