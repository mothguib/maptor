# -*- coding: utf-8 -*-

# Converting logs of 3D positions to binary positions

import sys
import time

# Adds the current package to the Python's path to run it from anywhere in the
# terminal
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from maptor import Paths
import maptor.control as control

sys.path.append(Paths.LOCALPYTROL)
import pytrol.util.pathformatter as pf

from maptor.util.argsparser import parse_args

args = parse_args()


def main(strt: str,
         variant: str,
         nb_execs: int,
         pop_sizes: list = None,
         duration: int = 3000,
         maps: list = None,
         soc_name: str = None,
         logs_rep: str = args.dirpath_logs,
         binpos_rep: str = Paths.LOCALBIN,
         viidls_rep: str = Paths.LOCALVIIDLS,
         vidls_rep: str = Paths.LOCALVIDLS):
    """


    :type maps: object
    :param variant: 
    :type variant: 
    :param strt:
    :type strt:
    :param soc_name:
    :type soc_name:
    :param pop_sizes:
    :type pop_sizes:
    :param duration:
    :type duration:
    :param nb_execs:
    :type nb_execs:
    :param maps:
    :type maps:object
    :param binpos_rep:
    :type binpos_rep:
    :param viidls_rep:
    :type viidls_rep:
    :param logs_rep:
    :type logs_rep:
    :param vidls_rep:
    :type vidls_rep:

    :return:
    :rtype:
    """

    if pop_sizes is None:
        pop_sizes = [5, 10, 15, 25]

    for m in maps:
        for p in pop_sizes:
            for i in range(nb_execs):
                # Log file path
                log_fp = pf.build_log_path(tpl=m, strt=strt, variant=variant,
                                           nagts=p, exec_id=i,
                                           logs_rep=logs_rep, ext="log",
                                           duration=duration,
                                           soc_name=soc_name)

                # Agent log file path
                agts_log_fp = pf.build_log_path(tpl=m, strt=strt,
                                                variant=variant,
                                                nagts=p, exec_id=i,
                                                logs_rep=logs_rep,
                                                ext="log.agts",
                                                duration=duration,
                                                soc_name=soc_name)

                start_time = time.time()

                bin_fp, viidl_fp, vidl_fp = \
                    control.LogProcessor.generate_save_binpos_and_idls(
                        log_fp=log_fp,
                        agts_log_fp=agts_log_fp,
                        binpos_rep=binpos_rep,
                        viidls_rep=viidls_rep,
                        vidls_rep=vidls_rep,
                        soc_name=soc_name)

                print("Inputs: ", log_fp, '\n', agts_log_fp, '\n')
                print("Outputs: ", bin_fp, '\n', viidl_fp, '\n', vidl_fp, '\n')

                end_time = time.time()

                print(end_time - start_time, ' s')
                print('\n')


# Executed only if run as a script
if __name__ == "__main__":
    main(strt=args.strategy,
         pop_sizes=[args.nagts],
         duration=args.duration,
         nb_execs=args.nbexecs,
         maps=[args.map],
         variant=args.variant,
         logs_rep=args.dirpath_logs,
         binpos_rep=args.dirpath_logs_bin,
         viidls_rep=args.dirpath_logs_viidls,
         vidls_rep=args.dirpath_logs_vidls)
