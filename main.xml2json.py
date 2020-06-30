# Converting XML logs into JSON

import os
import sys
import time

# Adds the current package to the Python's path to run it from anywhere in the
# terminal
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from maptor import Paths
import maptor.control as control


# Executes only if run as a script
if __name__ == "__main__":
    pop_sizes = [1, 5, 10, 15, 25]

    # Map name
    m = sys.argv[1]
    # m = "islands"

    root_xml_path = Paths.PCKGROOT + "data/logs/xml/" + m + "/hpcc/"
    config = "hpcc-" + m + "-soc_1_"

    for p in pop_sizes:
        for i in range(10):
            xml_path = root_xml_path + config + str(p) + "/" + config + str(
                p) + \
                       "-" + str(i) + ".log"
            json_path = xml_path.replace("xml", "json").replace(".log",
                                                                ".log.json")
            print("Input: ", xml_path)
            print("Output: ", json_path)

            start_time = time.time()

            control.XMLLogProcessor.sp_to_p_log(xml_path, json_path)

            end_time = time.time()

            print(end_time - start_time, 's')
            print('\n')
