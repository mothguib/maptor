# -*- coding: utf-8 -*-

# Converting logs of 3D positions to binary positions

# ## USAGE

# `python main2.3d2bin.py`

# import os
# import sys
# Adds the current package to the Python's path to run it from anywhere in the
# terminal
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import time

from maptor import Paths
import maptor.control as control


def main(strt,
         pop_sizes,
         duration,
         nb_execs,
         maps,
         socname: str = None,
         binpos_rep: str = Paths.BIN,
         logs_rep: str = Paths.LOGS):

    for m in maps:
        for p in pop_sizes:
            dyn_socname = socname
            if dyn_socname is None:
                # Dynamic society name
                dyn_socname = "soc_hpcc_" + str(p)

            config = "{}-{}-{}-".format(strt, m, dyn_socname)
            configpath = m + '/' + strt + '/' + str(p) + '/' + str(duration) \
                         + '/'
            # Dir path of the logs for the current configuration
            logdirpath = logs_rep + '/' + configpath + '/'

            config += "{}-{}-".format(str(p), duration)

            for i in range(nb_execs):
                execution = config + str(i)
                # Log file path
                log_fp = logdirpath + '/' + execution + ".log.json"

                start_time = time.time()

                binlog_fp = control.BinaryProcessor.generate_binpos(log_fp,
                                                                   binpos_rep)

                print("Input: ", log_fp)
                print("Output: ", binlog_fp)

                end_time = time.time()

                print(end_time - start_time, ' s')
                print('\n')


# Execute only if run as a script
if __name__ == "__main__":
    strt = "hpcc_0.2"
    pop_sizes = [1, 5, 10, 15, 25]
    # pop_sizes = [10]
    nb_execs = 100
    maps = ["map_b", "circle"]
    # maps = ["islands"]
    duration = 3000
    # Map name
    # m = sys.argv[1]

    main(strt=strt, pop_sizes=pop_sizes, duration=duration,
         nb_execs=nb_execs, maps=maps)
