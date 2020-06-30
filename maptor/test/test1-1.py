# test1.py: test of:
#   - Processor.drop_excess_actions (commented)
#   - Processor.refined_xml_log_to_iterable (commented)
#   - Processor.sp_to_p_log

import time

from maptor import Paths
from maptor.control.XMLLogProcessor import Processor

start = time.time()

'''
inpt = PCKGROOT + "data/logs/xml/islands/hpcc/hpcc-islands-soc_1_10/" + \
                     "hpcc-islands-soc_1_10-0.log"
'''

inpt = Paths.VARIOUS + "test_logs/hpcc-islands-soc_1_10-7-trunc.log"
output = Paths.VARIOUS + "test_logs/hpcc-islands-soc_1_10-7-trunc.prcss.xml"

json_log_path = Paths.VARIOUS + "test_logs/hpcc-islands-soc_1_10-7-trunc.log.prcss" \
                          ".json"

# xml = Processor.drop_excess_actions(input, output)
# Processor.refined_xml_log_to_iterable(xml, json_log_path)

Processor.sp_to_p_log(inpt, json_log_path, output)

end = time.time()

print(end - start)





