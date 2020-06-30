# -*- coding: utf-8 -*-

import os


def is_log(p: str):
    """

    :param p: the file path
    :type p: str
    :return:
    :rtype: bool
    """

    return p.endswith("log.json")


def is_agts_log(p: str):
    """

    :param p: the file path
    :type p: str
    :return:
    :rtype: bool
    """

    return p.endswith("log.agts.json")
