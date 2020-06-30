import json
import os
import numpy as np
from lxml import etree

from maptor.control.XMLReader import XMLReader
from maptor.control.MetricComputer import MetricComputer


class XMLLogProcessor:
    @classmethod
    def sp_to_p_log(cls, xml_log_path: str, json_log_path: str,
                    prcss_xml_log_path: str = ''):
        cls.refined_xml_log_to_iterable(cls.drop_excess_actions(
            xml_log_path, prcss_xml_log_path), json_log_path)

    @classmethod
    def refined_xml_log_to_iterable(cls, xml: str, json_log_path: str):
        root = etree.fromstring(xml)

        nbperiodss = int(float(root.findall("./event")[-1].get("time")))

        vertices, edges = XMLReader.map_xml_to_iterable(xml)[2:4]
        socs, socs_to_ids = XMLReader.socs_xml_to_dicts(xml, "hpcc")
        soc_name = socs[0]["id"]

        # Starting positions
        agts = socs[0]["agents"]
        pos_agts = [(-1, -1, -1)] * len(agts)

        for i in range(len(agts)):
            pos_agts[i] = (vertices[agts[i]["vertex_id"]], -1, 0)

        pos_agtss = [pos_agts]

        # Starting idlenesses
        idlss = np.zeros((nbperiodss, len(vertices)), dtype=np.int16)
        idls = np.zeros(len(vertices), dtype=np.int16)

        m_cptr = MetricComputer()

        t = 0
        for t in range(1, nbperiodss):
            pos_agts, idls = cls.load_step(root, t, soc_name,
                                           socs_to_ids,
                                           vertices, edges,
                                           pos_agts,
                                           idls)

            pos_agtss += [pos_agts]
            idlss[t] = idls

            # Computation of the intervals
            m_cptr.get_intvls(t, idlss)

        m_cptr.compute_metrics(t, idlss)

        directory = os.path.dirname(json_log_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(json_log_path, 'w') as s:
            json.dump([[pos_agtss, idlss.tolist()],
                       m_cptr.metrics.tolist()], s)

    @classmethod
    def load_step(cls, root_elmt: etree.Element, t: int, soc_name: str,
                  socs_to_ids: dict, vertices: dict, edges: dict,
                  prev_pos_agts: list, idls: np.ndarray):
        """
        Loads and returns positions of agents and real idlenesses for the
        time t

        :param root_elmt:
        :param t:
        :param soc_name:
        :param socs_to_ids:
        :param vertices:
        :param edges:
        :param prev_pos_agts:
        :param idls:
        :return:
        """

        evts = root_elmt.findall("./event[@time='" + str(float(t)) +
                                 "']")

        pos_agts = prev_pos_agts[:]

        idls += 1

        for e in evts:
            pos_agts[socs_to_ids[soc_name]["agt_ids"][e.get("agent_id")]] = \
                (vertices[e.get("node_id")], edges[e.get("edge_id")] if \
                    "edge_id" in e.attrib else -1, int(float(e.get(
                    "length"))) if "length" in e.attrib else 0)

            idls[vertices[e.get("node_id")]] = 0

        return pos_agts, idls

    @classmethod
    def drop_excess_actions(cls, log_input_path: str, \
                            log_output_path: str = '') -> str:
        """
        Return the xml log with only the moving events (type 5)

        :param log_input_path: the path of the log xml file to process
        :type log_input_path: str
        :param log_output_path: the path of the log xml file processed
        :type log_output_path: str
        :return: The log to the format XML string removed of excess moves
        :rtype: str
        """

        tree = etree.parse(log_input_path)
        root = tree.getroot() # etree.root correponds to the root element
        # node (the top element node) and not the XPath root node

        root = cls.drop_visit_actions(root)
        tree = etree.ElementTree(root)

        cls.drop_excess_moves(root)

        evts = root.findall("./event")

        for e in evts:
            root.remove(e)

        # Events sorting by time
        def getkey(elem: etree.Element):
            return float(elem.get("time"))
            # return float(elem.attrib["time"])

        # Events sorting by time
        evts = sorted(evts, key=getkey)

        root.extend(evts)

        nbperiodss = int(float(evts[-1].attrib["time"]))
        agts = root.findall("./society/agent")
        agts_nb = len(agts) if len(root.findall(".society/agent["
                                                "@id='coordinator']")) == 0 \
            else len(agts) - 1

        for t in range(nbperiodss, 0, -1):
            # Time-stamped events
            ts_evts = root.findall("./event[@time='" + str(float(t)) + "']")
            if len(ts_evts) < agts_nb:
                for e in ts_evts:
                    root.remove(e)
            else:
                break

        if log_output_path != '':
            tree.write(log_output_path)

        return etree.tostring(root, encoding="unicode")

    @staticmethod
    def drop_visit_actions(root: etree.Element):

        t6_t0_evts = root.xpath("./event[@type='6' and @time='0.0']")
        for e in t6_t0_evts:
            root.remove(e)

        t6_evts = root.findall("./event[@type='6']")
        for e in t6_evts:
            # Events to reschedule
            etrs = root.xpath("./event[@type='6"
                              "' and @time='" + e.attrib["time"] +
                              "' and @agent_id='" + e.attrib["agent_id"] + "']"
                              "/following::event[@type='5' " +
                              "and @agent_id='" + e.attrib["agent_id"] + "']")
            root.remove(e)

            for f in etrs:
                f.attrib["time"] = str(float(f.attrib["time"]) - 1.0)
        evts_to_delete = root.xpath("./event[@type!='5']")

        for e in evts_to_delete:
            root.remove(e)

        return root

    @staticmethod
    def drop_excess_moves(root: etree.Element):
        evts = root.findall("./event")

        for e in evts:
            if "edge_id" in e.attrib:
                if float(e.attrib["length"]) >= np.round(float(root.find(
                                        ".//edge[@id='" + e.attrib["edge_id"] +
                                        "']").attrib["length"])):
                    # Events to reschedule
                    etrs = root.xpath("./event[@time='" + e.attrib[
                        "time"] + "' and @agent_id='" + e.attrib["agent_id"] +
                                      "' and @node_id='" + e.attrib[
                                          "node_id"] +
                                      "' and @edge_id='" + e.attrib[
                                          "edge_id"] +
                                      "' and @length='" + e.attrib["length"] +
                                      "']/following::event[@agent_id='" +
                                      e.attrib["agent_id"] + "']")
                    root.remove(e)

                    for f in etrs:
                        f.attrib["time"] = str(float(f.attrib["time"]) - 1.0)
