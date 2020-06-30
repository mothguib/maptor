# test1.py: test of:
#   - Processor.drop_excess_actions (commented)
#   - Processor.refined_xml_log_to_iterable (commented)
#   - Processor.sp_to_p_log

import time

from maptor import PCKGROOT, VARIOUS
from maptor.control.XMLLogProcessor import Processor

start = time.time()

inpt = PCKGROOT + "data/logs/xml/map_a/hpcc/hpcc-map_a-soc_1_1/hpcc-map_a" \
                   "-soc_1_1-0.log"

output = VARIOUS + "test_logs/hpcc-map_a-soc_1_1-0.log.prcss.xml"

json_log_path = VARIOUS + "test_logs/hpcc-map_a-soc_1_1-0.log" \
                          ".json"

# xml = Processor.drop_excess_actions(input, output)
# Processor.refined_xml_log_to_iterable(xml, json_log_path)

Processor.sp_to_p_log(inpt, json_log_path, output)

end = time.time()

print(end - start)





