import untangle

from maptor.control.MAPLoader import MapLoader


class XMLReader:
    @classmethod
    def map_xml_to_iterable(cls, path: str):
        """
        Interprets the given string as a filename, URL or XML data string,
        parses it and returns a Python iterable

        :param path:
        :type path:
        :return:
        :rtype:
        """

        return MapLoader.map_dict_to_iterables(cls.map_xml_to_dict(path))

    @classmethod
    def map_xml_to_dict(cls, path: str):
        """
        Interprets the given string as a filename, URL or XML data string,
        parses it and returns a Python dict

        :param path:
        :type path:
        :return:
        :rtype:
        """
        return cls.map_untangle_to_dict(untangle.parse(path))

    @staticmethod
    def map_untangle_to_dict(doc: untangle.Element) -> dict:
        graph_elmt = doc.get_elements()[0].graph
        graph = {'label': graph_elmt['label'], 'vertices': []}

        for n in graph_elmt.node:
            node_dic = {}
            attrs = n._attributes

            for a in attrs:
                node_dic[a] = attrs[a]
            graph['vertices'] += [node_dic]

        graph['edges'] = []

        for e in graph_elmt.edge:
            edge_dic = {}
            attrs = e._attributes

            for a in attrs:
                edge_dic[a] = attrs[a]
            graph['edges'] += [edge_dic]

        return graph

    @classmethod
    def socs_xml_to_dicts(cls, path: str, agt_type: str = '') -> (dict, dict):
        """
        Interprets the given string as a filename, URL or XML data string
        with <society> as root element(s), parses it and returns two Python
        dicts: the first one representing the societies themselves and the
        second one the societies and agents' original ids to int ids

        :param agt_type:
        :type agt_type:
        :param path:
        :type path:
        :return:
        :rtype:
        """

        if agt_type == '':
            agt_type = path.split("/")[-1].split("-")[0]

        return cls.socs_untangle_to_dicts(untangle.parse(path), agt_type)

    @classmethod
    def socs_untangle_to_dicts(cls, doc: untangle.Element, agt_type: str) -> (
            dict, dict):
        socs = []
        socs_to_ids = {}

        counter_s = 0
        for s in doc.get_elements()[0].society:
            soc_dic = {}
            attrs = s._attributes

            for a in attrs:
                soc_dic[a] = attrs[a]

            socs_to_ids[soc_dic["id"]] = {"int_id": counter_s, "agt_ids": {}}

            soc_dic["agents"] = []

            counter_a = 0
            for agt in s.get_elements():
                attrs = agt._attributes
                agt_dic = {'type': agt_type, "id": attrs["id"], "vertex_id":
                    attrs["node_id"], "allowed_perceptions": []}

                socs_to_ids[soc_dic["id"]]["agt_ids"][agt_dic["id"]] = \
                    counter_a

                for pcp in agt.get_elements("allowed_perception"):
                    pcp_dic = {}
                    attrs = pcp._attributes

                    for a in attrs:
                        pcp_dic[a] = attrs[a]

                    agt_dic["allowed_perceptions"] += [pcp_dic]

                agt_dic['allowed_actions'] = []

                for act in agt.get_elements("allowed_action"):
                    act_dic = {}
                    attrs = act._attributes

                    for a in attrs:
                        act_dic[a] = attrs[a]

                    agt_dic['allowed_actions'] += [act_dic]

                soc_dic['agents'] += [agt_dic]

                counter_a += 1

            socs += [soc_dic]

            counter_s += 1

        return cls.swap_coord(socs, socs_to_ids)

    @staticmethod
    def swap_coord(socs: dict, socs_to_ids: dict) -> (dict, dict):
        """
        Puts the coordinator at the first position i.e. with id 0

        :param socs:
        :type socs:
        :param socs_to_ids:
        :type socs_to_ids:
        :return:
        :rtype:
        """

        for soc in socs:
            agts = soc["agents"]
            agts_to_ids = socs_to_ids[soc["id"]]["agt_ids"]

            for i in range(len(agts)):
                if agts[i]["id"] == "coordinator":
                    buffer = (agts_to_ids[agts[0]["id"]], agts[0])
                    agts_to_ids[agts[0]["id"]], agts[0] = agts_to_ids[agts[i][
                        "id"]], agts[i]
                    agts_to_ids[agts[i]["id"]], agts[i] = buffer
                    break

        return socs, socs_to_ids

