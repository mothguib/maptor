# test2.py: tests the conversion from SimPatrol's log to Pytrol's log:

from maptor.control.XMLLogProcessor import Processor

xml_log_input_path = "../logs/xml/map_a/hpcc/hpcc-map_a-soc_1_1/" + \
                     "hpcc-map_a-soc_1_1-1.log"
json_log_path = "../logs/json/map_a/hpcc/hpcc-map_a-soc_1_1/" + \
                "hpcc-map_a-soc_1_1-1.log.json"

Processor.sp_to_p_log(xml_log_input_path, json_log_path)
