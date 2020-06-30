# -*- coding: utf-8 -*-
import math
import sys
import glob
import json
import numpy as np

import matplotlib.pyplot as plt  # `matplotlib.pyplot` is a state-based
# interface to matplotlib. See the state pattern in computing
import matplotlib.lines as lines

from maptor import *

sys.path.append(Paths.LOCALPYTROL)
from pytrol.util import pathformatter as pf


# matplotlib.rc('font', **font)

def plot_all(strts: list,
             statpath: str,
             datasrcs: list = None,
             legend_strts: list = None,
             maps: list = None,
             nagts: list = None,
             mtr: int = 1,
             duration: int = 3000,
             handles: list = None,
             nrm: bool = True,
             display_value: bool = True):
    """
    Plots the metric of id `mtr` for all strategies `strts` passed as argument
    w.r.t number of agents.

    :param legend_strts:
    :type legend_strts:
    :param strts: strategies' statistics to plot
    :type strts: str
    :param statpath:
    :type statpath:
    :param datasrcs: strategy source having generated data
    :type datasrcs: list
    :param maps:
    :type maps:
    :param nagts:
    :type nagts:
    :param display_value:
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int
    :param display_value:
    :type display_value:
    :return:
    :rtype:
    """

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    if datasrcs is None:
        datasrcs = [''] * len(strts)

    if handles is None:
        # A list of `pyplot.Artists` (lines, patches) to be added to the
        # legend
        handles = []

    prepare_plot(strts, statpath=statpath, maps=maps, nagts=nagts,
                 mtr_handler=get_means, mtr=mtr, nrm=nrm,
                 duration=duration, handles=handles,
                 display_value=display_value, adpc=datasrcs,
                 strts_names=legend_strts)

    # plt.subplots_adjust(left=0.07, right=0.99, top=0.99, bottom=0.07)
    plt.subplots_adjust(left=0.11, right=0.99, top=0.98, bottom=0.11)
    # plt.subplots_adjust(left=0.085, right=0.99, top=0.99, bottom=0.085)

    plt.show()


def plot_bar_chart_all(strts: list,
                       statpath: str,
                       maps: list = None,
                       nagts: list = None,
                       mtr: int = 1,
                       duration: int = 3000,
                       handles: list = None,
                       nrm: bool = True):
    """
    Plots on a bar chart the metric of id `mtr` for all strategies `strts`
    passed as argument w.r.t number of agents.

    :param strts: strategies' statistics to plot
    :type strts: str
    :param statpath:
    :type statpath: str
    :param adpc: additional directory path component
    :type adpc:
    :param maps:
    :type maps:
    :param nagts:
    :type nagts:
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int
    :return:
    :rtype:
    """

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    if handles is None:
        # A list of `pyplot.Artists` (lines, patches) to be added to the
        # legend
        handles = []

    prepare_bar_chart_plot(strts,
                           statpath=statpath,
                           maps=maps,
                           nagts=nagts,
                           mtr_handler=get_means,
                           mtr=mtr,
                           nrm=nrm,
                           duration=duration)

    plt.show()


def best_of_vars(reps: list,
                 strts: list,
                 statpath: str,
                 ds_reps: list = None,
                 ds_strts: list = None,
                 legend_strts: list = None,
                 maps: list = None,
                 nagts: list = None,
                 mtr: int = 0,
                 duration: int = 3000,
                 handles: list = None,
                 xoffset: float = 0,
                 yoffset: float = 3,
                 nrm: bool = True,
                 display_value: bool = True,
                 dsn: bool = False,
                 value_fontsize: int = FONTSIZE):
    """
    Plots values of the metric `mtr` w.r.t number of agents
    for all representative strategies populating `reps` and for the best
    variant of the strategies populating `best_of`.

    :param reps: representative strategies
    :type reps: list
    :param strts: strategies whose the best variant will be depicted,
    for each strategy
    :type strts:  list
    :param statpath:
    :type statpath: str
    :param ds_strts:
    :type ds_strts:
    :param ds_reps:
    :type ds_reps:
    :param maps:
    :type maps:
    :param nagts:
    :type nagts:
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param yoffset:
    :type yoffset:
    :param xoffset:
    :type xoffset:
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param display_value:
    :type display_value:
    :param duration: number of periods
    :type duration: int
    :param value_fontsize: Font size of the values
    :type value_fontsize:

    :return:
    :rtype:
    """

    if ds_reps is None:
        ds_reps = [''] * len(reps)

    if ds_strts is None:
        ds_strts = [''] * len(strts)

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    if handles is None:
        # A list of `pyplot.Artists` (lines, patches) to be added to the
        # legend
        handles = []

    prepare_plot(reps, statpath=statpath, adpc=ds_reps,
                 mtr_handler=get_means, maps=maps, nagts=nagts,
                 mtr=mtr, nrm=nrm, duration=duration, handles=handles,
                 display_value=False, value_fontsize=value_fontsize,
                 xoffset=xoffset, yoffset=yoffset, dsn=False)

    prepare_plot(strts, statpath=statpath,
                 mtr_handler=best_variant_metric, maps=maps, nagts=nagts,
                 mtr=mtr, nrm=nrm, duration=duration, handles=handles,
                 dsn=dsn, strts_names=legend_strts,
                 display_value=display_value, adpc=ds_strts)

    # plt.subplots_adjust(left=0.07, right=0.99, top=0.99, bottom=0.07)
    plt.subplots_adjust(left=0.11, right=0.99, top=0.98, bottom=0.11)
    # plt.subplots_adjust(left=0.085, right=0.99, top=0.99, bottom=0.085)

    plt.show()


# This function is a hack to avoid texts on the plot overlap
# TODO: creating a generic procedure to handle that
def plot_reps_and_best_of_vars_norm_max_idleness(reps: list,
                                                 strts: list,
                                                 statpath: str,
                                                 ds_strts: list = None,
                                                 ds_reps: list = None,
                                                 maps: list = None,
                                                 nagts: list = None,
                                                 mtr: int = 1,
                                                 duration: int = 3000,
                                                 handles: list = None,
                                                 xoffset: float = 0,
                                                 yoffset: float = 3,
                                                 nrm: bool = True,
                                                 display_value: bool = True,
                                                 value_fontsize: int
                                                 = FONTSIZE):
    """
    Plots values of the metric `mtr` w.r.t number of agents
    for all representative strategies populating `reps` and for the best
    variant of the strategies populating `best_of`.

    :param reps: representative strategies
    :type reps: list
    :param strts: strategies whose the best variant will be depicted,
    for each strategy
    :type strts:  list
    :param statpath:
    :type statpath: str
    :param ds_strts:
    :type ds_strts:
    :param ds_reps:
    :type ds_reps:
    :param maps:
    :type maps:
    :param nagts:
    :type nagts:
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param yoffset:
    :type yoffset:
    :param xoffset:
    :type xoffset:
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param display_value:
    :type display_value:
    :param duration: number of periods
    :type duration: int
    :param value_fontsize: Font size of the values
    :type value_fontsize:

    :return:
    :rtype:
    """

    if ds_reps is None:
        ds_reps = [''] * len(reps)

    if ds_strts is None:
        ds_strts = [''] * len(strts)

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    if handles is None:
        # A list of `pyplot.Artists` (lines, patches) to be added to the
        # legend
        handles = []

    prepare_plot_norm_max_idleness(reps, statpath=statpath, adpc=ds_reps,
                                   mtr_handler=get_means, maps=maps,
                                   nagts=nagts,
                                   mtr=mtr, nrm=nrm, duration=duration,
                                   handles=handles,
                                   display_value=display_value,
                                   value_fontsize=value_fontsize,
                                   xoffset=xoffset, yoffset=yoffset)

    prepare_plot_norm_max_idleness(strts, statpath=statpath, adpc=ds_strts,
                                   dsn=True, mtr_handler=best_variant_metric,
                                   maps=maps, nagts=nagts, mtr=mtr, nrm=nrm,
                                   duration=duration, handles=handles,
                                   display_value=display_value,
                                   value_fontsize=value_fontsize,
                                   xoffset=xoffset, yoffset=yoffset)
    plt.show()


def best_var_best_strt(reps: list,
                       strts_1: list,
                       strts_2: list,
                       statpath: str,
                       legend_reps: list = None,
                       legend_strts_1: list = None,
                       legend_strts_2: list = None,
                       ds_strts_1: list = None,
                       ds_strts_2: list = None,
                       ds_reps: list = None,
                       maps: list = None,
                       nagts: list = None,
                       mtr: int = 1,
                       duration: int = 3000,
                       handles: list = None,
                       nrm: bool = True,
                       dsn: bool = True,
                       display_value: bool = True):
    """
    Plots values of the metric `mtr` w.r.t number of agents
    of:
        * all the representative strategies populating `reps`,
        * the best strategy of `strts_1`,
        * the best variant for each strategy populating `strts_2`.

    :param reps:
    :type reps: list
    :param strts_1: groups of strategies amongst which the best one of
    each group will be plot,
    two-dimensional list
    :type strts_1:
    :param strts_2:  strategies that for each one the best variant will be plot
    :type strts_2:  list
    :param legend_strts_1: names to use in the legend for each group of
    strategies populating `strts_1`
    :type legend_strts_1: list
    :param legend_strts_2:
    :type legend_strts_2:
    :param statpath: directory path of statistic file
    :type statpath: str
    :param ds_reps: data source of `reps`
    :type ds_reps:
    :param ds_strts_1: data source of `ds_strts_2`, one for each group of
    strategies of `strts_1`
    :type ds_strts_1:
    :param ds_strts_2: data source of `ds_strts_2`
    :type ds_strts_2:
    :param maps:
    :type maps: list
    :param nagts:
    :type nagts: list
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param duration: number of periods
    :type duration: int
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param dsn: displays strategie names on the plot
    :type dsn: bool
    :param display_value:
    :type display_value:
    :return:
    :rtype:
    """

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    if handles is None:
        # A list of `pyplot.Artists` (lines, patches) to be added to the
        # legend
        handles = []

    if legend_strts_1 is None:
        legend_strts_1 = []

    if ds_reps is None:
        ds_reps = [''] * len(reps)

    if ds_strts_1 is None:
        ds_strts_1 = [''] * len(strts_1)

    if ds_strts_2 is None:
        ds_strts_2 = [''] * len(strts_2)

    # dpi = 100
    # fig = plt.figure(figsize=(1400 / dpi, 800 / dpi), dpi=dpi)

    prepare_plot(reps, strts_names=legend_reps, mtr_handler=get_means,
                 maps=maps, nagts=nagts, mtr=mtr,
                 nrm=nrm, duration=duration,
                 handles=handles, dsn=False,
                 display_value=display_value, statpath=statpath,
                 adpc=ds_reps)

    for i, ba in enumerate(strts_1):
        prepare_best_strategy_plot(ba,
                                   strt_name=legend_strts_1[i],
                                   maps=maps,
                                   nagts=nagts,
                                   mtr=mtr,
                                   nrm=nrm,
                                   duration=duration,
                                   handles=handles,
                                   dsn=dsn,
                                   display_value=display_value,
                                   statpath=statpath,
                                   adpc=ds_strts_1[i])

    prepare_plot(strts_2, strts_names=legend_strts_2, statpath=statpath,
                 mtr_handler=best_variant_metric, maps=maps, nagts=nagts,
                 mtr=mtr, nrm=nrm, duration=duration, handles=handles,
                 dsn=False, display_value=display_value, adpc=ds_strts_2)

    # plt.subplots_adjust(left=0.07, right=0.99, top=0.99, bottom=0.07)
    plt.subplots_adjust(left=0.11, right=0.99, top=0.98, bottom=0.11)
    # plt.subplots_adjust(left=0.085, right=0.99, top=0.99, bottom=0.085)

    # fig.savefig('/home/mehdi/Downloads/my_fig.png')
    plt.show()
    # plt.savefig('/home/mehdi/Downloads/my_fig.png', dpi=my_dpi)


def plot_metric_space_reps_best_of_var(reps: list,
                                       best_variant: list = None,
                                       maps: list = None,
                                       nagts: list = None,
                                       duration: int = 3000,
                                       handles: list = None,
                                       nrm: bool = True,
                                       display_value: bool = True):
    """
    Plots the best variant for each strategy populating `best_of`
    in the criterion space of metrics.

    :param display_value:
    :type display_value:
    :param maps:
    :type maps:
    :param nagts:
    :type nagts:
    :param reps: reference strategies
    :type reps: list
    :param best_variant:  strategies whose the best variant will be plot
    :type best_variant:  list
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int
    :return:
    :rtype:
    """

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    if handles is None:
        # A list of `pyplot.Artists` (lines, patches) to be added to the
        # legend
        handles = []

    if reps is not None:
        prepare_metric_space_plot(reps,
                                  mtr_handler=get_means,
                                  maps=maps, nrm=nrm,
                                  duration=duration,
                                  handles=handles, xoffset=1.5,
                                  yoffset=4,
                                  display_value=display_value)

    prepare_metric_space_plot(best_variant,
                              mtr_handler= \
                                  best_variant_metric,
                              maps=maps, nrm=nrm,
                              duration=duration,
                              handles=handles, xoffset=1.5, yoffset=4,
                              display_value=display_value)

    plt.show()


def plot_metric_space_reps_and_compared(compared: list,
                                        reps: list = None,
                                        maps: list = None,
                                        nagts: list = None,
                                        duration: int = 3000,
                                        handles: list = None,
                                        nrm: bool = True,
                                        display_value: bool = True):
    """
    Plots all the compared strategies populating the list`compared` in
    the criterion space of metrics.

    :param display_value:
    :type display_value:
    :param compared: compared strategies
    :type compared: list
    :param maps:
    :type maps:
    :param nagts:
    :type nagts:
    :param reps:
    :type reps:
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int
    :return:
    :rtype:
    """

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    if handles is None:
        # A list of `pyplot.Artists` (lines, patches) to be added to the
        # legend
        handles = []

    prepare_metric_space_plot(compared,
                              mtr_handler=get_means,
                              maps=maps, nrm=nrm,
                              duration=duration,
                              handles=handles, xoffset=1, yoffset=1,
                              display_value=display_value)

    if reps is not None:
        prepare_metric_space_plot(reps,
                                  mtr_handler=get_means,
                                  maps=maps, nrm=nrm,
                                  duration=duration,
                                  handles=handles, xoffset=1,
                                  yoffset=1,
                                  display_value=display_value)

    plt.show()


def plot_metric_space_av_reps_and_compared(compared: list,
                                           reps: list = None,
                                           maps: list = None,
                                           duration: int = 3000,
                                           handles: list = None,
                                           nrm: bool = True,
                                           display_value: bool = True):
    """
    Plots all the compared strategies populating the list`compared` in
    the criterion space of metrics averaged over the population sizes.

    :param compared: compared strategies
    :type compared: list

    Optional (keyword) arguments:
    :param maps:
    :type maps:
    :param reps:
    :type reps:
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int
    :param display_value:
    :type duration: bool
    :return:
    :rtype:
    """

    if maps is None:
        maps = MAPS

    # A list of `pyplot.Artists` (lines, patches) to be added to the legend

    prepare_metric_space_plot_av_nagts(compared,
                                       mtr_handler=get_means,
                                       maps=maps, nrm=nrm,
                                       duration=duration,
                                       handles=handles, xoffset=1,
                                       yoffset=1,
                                       display_value=display_value)
    if reps is not None:
        prepare_metric_space_plot_av_nagts(reps,
                                           mtr_handler=get_means,
                                           maps=maps, nrm=nrm,
                                           duration=duration,
                                           handles=handles, xoffset=1,
                                           yoffset=1,
                                           display_value=display_value)
    plt.show()


def plot_bar_chart_a_15(strts: list,
                        statpath: str,
                        maps: list = None,
                        nagts: list = None,
                        adpcs: list = None,
                        mtr: int = 1,
                        duration: int = 3000,
                        handles: list = None,
                        nrm: bool = True):
    """
    Plots values of the metric `mtr` for all strategies `strts` passed in
    argument w.r.t number of agents.

    :param strts: strategies' statistics to plot
    :type strts: str
    :param statpath:
    :type statpath:
    :param maps:
    :type maps:
    :param nagts:
    :type nagts:
    :param adpcs: additional statistic directory path components, one for each strategy
    :type adpcs: str
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int
    :return:
    :rtype:
    """

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    if adpcs is None:
        adpcs = [''] * len(strts)

    if handles is None:
        # A list of `pyplot.Artists` (lines, patches) to be added to the
        # legend
        handles = []

    prepare_bar_chart_plot_a_15(strts, statpath=statpath, maps=maps,
                                nagts=nagts, adpcs=adpcs,
                                mtr_handler=get_means, mtr=mtr, nrm=nrm,
                                duration=duration)

    plt.show()


# Metric handlers

# TODO: changing metric handlers to return the standard deviation as well,
#  and impacting this changes on plot preparers

def get_means(tpl: str,
              strt: str,
              nagts: int,
              duration: int,
              mtr: int,
              nrm: bool,
              statpath: str,
              adpc: str = None) -> (float, str):
    """
    Handles the way the metrics' means are retrieved and returned for a given
    scenario `{<map>, <number of agents>, <strategy>}`. This method returns
    the mean and the std of the  metric `mtr` associated with the strategy
    `strt` passed in arguments.

    :param tpl:
    :type tpl:
    :param strt:
    :type strt:
    :param nagts:
    :type nagts:
    :param duration:
    :type duration:
    :param mtr:
    :type mtr:
    :param nrm:
    :type nrm:
    :param statpath:
    :type statpath:
    :param adpc: additional directory path component, e.g. `hpcc_0.5`
    :type adpc: str
    :return:
    :rtype:
    """

    if adpc is None:
        adpc = ''

    path = pf.build_stat_path(tpl=tpl, strt=strt, nagts=nagts,
                              statpath=statpath,
                              datasrc=adpc, nrm=nrm,
                              duration=duration)

    with open(path, 'r') as s:
        stats = json.load(s)
        std = 0 if len(stats) < 2 else stats[1][mtr]

        return stats[0][mtr], std, strt


def best_variant_metric(tpl: str,
                        strt: str,
                        nagts: int,
                        duration: int,
                        mtr: int,
                        nrm: bool,
                        statpath: str,
                        adpc: str = None) -> (float, str):
    """
    Handles the way the metric values of id `mtr` of the best variant of
    the strategy `strt` are returned .

    :param tpl:
    :type tpl:
    :param strt:
    :type strt:
    :param nagts:
    :type nagts:
    :param duration:
    :type duration:
    :param mtr:
    :type mtr:
    :param nrm:
    :type nrm:
    :param statpath:
    :type statpath:
    :param adpc: additional directory path component
    :type adpc: str
    :return:
    :rtype:
    """

    if adpc is None:
        adpc = ''

    # The file's directory path
    dirpath = "{}/{}/".format(statpath, adpc)

    # Pattern of the file path
    fp_pattern = \
        "{}/{}-{}*-{}-{}{}{}".format(dirpath, tpl, strt, nagts, duration,
                                     (".norm" if nrm else ""), ".stat")

    fps = sorted(glob.glob(fp_pattern))

    # Metrics for each strategy variant of the current scenario
    v_mtrs = []
    # Standard deviation of metrics for each strategy variant of the current
    # scenario
    std_v_mtrs = []
    # Strategies'names
    strts = []

    for fp in fps:
        strt = fp.split("/")[-1].split("-")
        strt = "{}-{}".format(strt[1], strt[2])

        # TODO: fixing this hack
        if strt not in ["rlpm_1-1", "rlpm_2-2", "rlpm_50-2"]:
            strts += [strt]
            with open(fp, 'r') as s:
                # Hack to handle the old statistic files containing only
                # 1-dimensional array (the new ones contain 2-dim arrays,
                # the second dimension standing for the std deviation)
                # TODO: converting all statistic files to the new format
                stats = json.load(s)
                if len(np.array(stats).shape) > 1:
                    v_mtrs += [stats[0][mtr]]
                    std_v_mtrs += [stats[1][mtr]]
                else:
                    v_mtrs += [stats[mtr]]

    argmin = np.argmin(v_mtrs)

    return v_mtrs[argmin], std_v_mtrs[argmin], strts[argmin]


def best_strategy_metric(tpl: str,
                         strts: list,
                         nagts: int,
                         duration: int,
                         mtr: int,
                         nrm: bool,
                         statpath: str,
                         adpc: str = None) -> (float, str):
    """
    Handles the way the metric values of id `mtr` of the best variant of the
    strategy `strt` are returned.

    :param tpl:
    :type tpl:
    :param strts:
    :type strts:
    :param nagts:
    :type nagts:
    :param duration:
    :type duration:
    :param mtr:
    :type mtr:
    :param nrm:
    :type nrm:
    :param statpath:
    :type statpath:
    :param adpc: additional directory path component
    :type adpc: str
    :return:
    :rtype:
    """

    if adpc is None:
        adpc = ''

    # Metrics for each strategy variant of the current scenario
    v_mtrs = []

    std_v_mtrs = []

    for strt in strts:
        fp = "{}/{}/{}-{}-{}-{}{}{}".format(statpath, adpc, tpl, strt, nagts,
                                            duration, (".norm" if nrm
                                                       else ""), ".stat")
        with open(fp, 'r') as s:
            # Hack to handle the old statistic files containing only
            # 1-dimensional array (the new ones contain 2-dim arrays,
            # the second dimension standing for the std deviation)
            # TODO: converting all statistic files to the new format
            stats = json.load(s)
            if len(np.array(stats).shape) > 1:
                v_mtrs += [stats[0][mtr]]
                std_v_mtrs += [stats[1][mtr]]
            else:
                v_mtrs += [stats[mtr]]

    argmin = np.argmin(v_mtrs)

    return v_mtrs[argmin], std_v_mtrs[argmin], strts[argmin]


# Plot preparers

def prepare_plot(strts: list,
                 statpath: str,
                 strts_names: list = None,
                 adpc: list = None,
                 maps: list = None,
                 nagts: list = None,
                 duration: int = 3000,
                 mtr: int = 1,
                 handles: list = None,
                 nrm: bool = True,
                 xoffset: float = 0,
                 yoffset: float = 3,
                 mtr_handler=None,
                 dsn: bool = False,
                 display_value: bool = True,
                 value_fontsize: int = FONTSIZE):
    """
    Prepares a plot with the number of agents in abscissa and the metric
    with the metric id `mtr` in ordinate.

    :param strts: strategies' statistics to plot
    :type strts: str
    :param statpath:
    :type statpath:
    :param strts_names:
    :type strts_names:
    :param adpc: additional directory path component
    :type adpc: str
    :param maps:
    :type maps:
    :param nagts:
    :type nagts:
    :param mtr_handler: metric handler, a function reference that handles
    the way the metric values are retrieved and returned for a given
    scenario `{<map>, <strategy>, <number of agents>}`
    :type mtr_handler:
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int
    :param yoffset:
    :type yoffset:
    :param xoffset:
    :type xoffset:
    :param dsn: displays strategie names on the plot
    :type dsn: bool
    :param display_value:
    :type display_value:
    :param value_fontsize: Font size of the values
    :type value_fontsize:

    :return:
    :rtype:
    """

    if adpc is None:
        adpc = [''] * len(strts)

    if strts_names is None:
        strts_names = strts

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    # Metric handler
    if mtr_handler is None:
        mtr_handler = get_means
    # A list of `pyplot.Artist` (lines, patches) to be added to the legend
    if handles is None:
        handles = []

    # Number of handles if others have been already set beforehand
    nbh = len(handles)
    # Number of strategy handles
    nbstrth = 0

    # If nbh > 0 then the legends concerning the maps have already been
    # defined in a previous call to `prepare_plot`
    if nbh == 0:
        for m in maps:
            map_line = lines.Line2D([], [], color="black",
                                    marker=LINESMRKS[MAPSIDS[m]], label=m,
                                    linewidth=LINEWIDTH, linestyle=':')
            handles += [map_line]
    else:
        nbstrth = nbh - len(maps)

    # Counting starts at `nbstrth` to take into account previous
    # strategy handles already set
    i = nbstrth

    for j, strt in enumerate(strts):
        strt_line = lines.Line2D([], [], color=LINESCLRS[i],
                                 label=strts_names[j], linewidth=LINEWIDTH,
                                 linestyle=':')
        handles += [strt_line]
        i += 1

    plt.xlabel("Number of agents", fontsize=TITLEFONTSIZE)
    plt.ylabel(("Norm. " if nrm else '') + MTRSNAMES[mtr],
               fontsize=TITLEFONTSIZE)

    # The title
    # plt.title("{} as a function of the number of agents".format(MTRSNAMES[
    #                                                                 mtr]),
    #           fontsize=TITLEFONTSIZE)

    # Setting the axes' label font size
    '''
    ax = plt.gca()  # Get the current `matplotlib.axes.Axes` instance on
    # the current figure matching the given keyword args, or create one.
    ax.tick_params(labelsize=FONTSIZE)
    '''
    plt.xticks(fontsize=FONTSIZE)
    plt.yticks(fontsize=FONTSIZE)

    for m in maps:
        # Counting starts at `nbstrth` to take into account previous handles
        # already set
        j = nbstrth

        # For each map, all metric values are stored, for all strategy and
        # number of agents
        all_vals = []

        # Each strategy population `strts` is depicted according to
        # `mtr_handler`
        for i, strt in enumerate(strts):
            # Current metric's values to display for each number of agents
            vals = []
            svals = []
            # Current strategies associated to the current metric's values
            # populating `mvals`
            cstrts = []

            for na in nagts:
                # `mval`: mean of the current metric's value
                # `sval`: `mval`'s std
                # `cstrt`: current strategy's name returned by the
                # metric handler

                val, sval, cstrt = mtr_handler(strt=strt, statpath=statpath,
                                               tpl=m,
                                               nagts=na, duration=duration,
                                               mtr=mtr, nrm=nrm, adpc=adpc[i])
                vals += [val]
                svals += [sval]
                cstrts += [cstrt]

            all_vals += [vals]

            plt.plot(nagts, vals, color=LINESCLRS[j],
                     marker=LINESMRKS[MAPSIDS[m]], markersize=12,
                     linewidth=LINEWIDTH, linestyle=':')

            plt.errorbar(nagts, vals, svals, linestyle='None', marker='^',
                         color=LINESCLRS[j])

            plt.legend(handles=handles, prop={'size': LGDFONTSIZE})

            text = ''

            for k, (a, b, c) in enumerate(zip(nagts, vals, cstrts)):
                # TODO: creating a variable to handle the displaying of
                #  `adpc`
                if dsn:
                    # text = "{}-{}".format(c, adpc) if adpc \
                    #     else "{}".format(c)
                    # Not displaying `adpc`
                    text = "{}".format(c)

                if display_value:
                    # if a != 5 and c != "rhpme_0.2":
                    # If the current text is that of the last value on the
                    # x-axis, it will be displayed upon several lines
                    # if a == nagts[-1]:
                    #     text = "{}:\n {}".format(str(int(b)), text) if dsn \
                    #         else str(int(b))
                    # else:
                    text = "{}: {}".format(text, str(int(b))) if dsn \
                        else "{}".format(str(int(b)))

                # Hack to not display strategy names
                # TODO: removing this hack by integrating a mecanism
                #  which handles this behaviour
                text = text.replace("rmaplpm_", ''). \
                    replace("rlpm_", ''). \
                    replace(": hcc_0.2", ''). \
                    replace(": hpcc_0.5", ''). \
                    replace(": cr", ''). \
                    replace("sgd_pre_100_", '')

                if i > 0:
                    plt.text(a + xoffset,
                             b + (yoffset if b > all_vals[i - 1][k]
                                  else - yoffset),  # offset to avoid the
                             # overlapping of the values of the strategies
                             # to plot
                             text,
                             size=value_fontsize)
                else:
                    plt.text(a + xoffset, b,
                             text,
                             size=value_fontsize)
            j += 1


# This function is a hack to avoid texts on the plot overlap
# TODO: creating a generic procedure to handle that
def prepare_plot_norm_max_idleness(strts: list,
                                   statpath: str,
                                   adpc: list = None,
                                   maps: list = None,
                                   nagts: list = None,
                                   duration: int = 3000,
                                   mtr: int = 1,
                                   handles: list = None,
                                   nrm: bool = True,
                                   xoffset: float = 0,
                                   yoffset: float = 3,
                                   mtr_handler=None,
                                   dsn: bool = False,
                                   display_value: bool = True,
                                   value_fontsize: int = FONTSIZE):
    """
    Prepares a plot with the number of agents in abscissa and the metric
    with the metric id `mtr` in ordinate.

    :param strts: strategies' statistics to plot
    :type strts: str
    :param statpath:
    :type statpath:
    :param adpc: additional directory path component
    :type adpc: str
    :param maps:
    :type maps:
    :param nagts:
    :type nagts:
    :param mtr_handler: metric handler, a function reference that handles
    the way the metric values are retrieved and returned for a given
    scenario `{<map>, <strategy>, <number of agents>}`
    :type mtr_handler:
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int
    :param yoffset:
    :type yoffset:
    :param xoffset:
    :type xoffset:
    :param dsn: displays strategie names on the plot
    :type dsn: bool
    :param display_value:
    :type display_value:
    :param value_fontsize: Font size of the values
    :type value_fontsize:

    :return:
    :rtype:
    """

    if adpc is None:
        adpc = [''] * len(strts)

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    # Metric handler
    if mtr_handler is None:
        mtr_handler = get_means
    # A list of `pyplot.Artist` (lines, patches) to be added to the legend
    if handles is None:
        handles = []

    # Number of handles if others have been already set beforehand
    nbh = len(handles)
    # Number of strategy handles
    nbstrth = 0

    # If nbh > 0 then the legends concerning the maps have already been
    # defined in a previous call to `prepare_plot`
    if nbh == 0:
        for m in maps:
            map_line = lines.Line2D([], [], color="black",
                                    marker=LINESMRKS[MAPSIDS[m]], label=m,
                                    linewidth=LINEWIDTH, linestyle=':')
            handles += [map_line]
    else:
        nbstrth = nbh - len(maps)

    # Counting starts at `nbstrth` to take into account previous
    # strategy handles already set
    i = nbstrth

    for strt in strts:
        strt_line = lines.Line2D([], [], color=LINESCLRS[i],
                                 label=strt, linewidth=LINEWIDTH,
                                 linestyle=':')
        handles += [strt_line]
        i += 1

    plt.xlabel("Number of agents", fontsize=TITLEFONTSIZE)
    plt.ylabel(("Norm. " if nrm else '') + MTRSNAMES[mtr],
               fontsize=TITLEFONTSIZE)

    # The title
    # plt.title("{} as a function of the number of agents".format(MTRSNAMES[
    #                                                                 mtr]),
    #           fontsize=TITLEFONTSIZE)

    # Setting the axes' label font size
    '''
    ax = plt.gca()  # Get the current `matplotlib.axes.Axes` instance on
    # the current figure matching the given keyword args, or create one.
    ax.tick_params(labelsize=FONTSIZE)
    '''
    plt.xticks(fontsize=FONTSIZE)
    plt.yticks(fontsize=FONTSIZE)

    i = 0
    for m in maps:
        # Counting starts at `lhid` to take into account previous handles
        # already set
        j = nbstrth

        # TDL
        all_vals = []
        for i, strt in enumerate(strts):
            # Current metric's values to display for each number of agents
            vals = []
            svals = []
            # Current strategies associated to the current metric's values
            # populating `mvals`
            cstrts = []

            for na in nagts:
                # `mval`: mean of the current metric's value
                # `sval`: `mval`'s std
                # `cstrt`: current strategy's name returned by the
                # metric handler

                val, sval, cstrt = mtr_handler(strt=strt, statpath=statpath,
                                               tpl=m,
                                               nagts=na, duration=duration,
                                               mtr=mtr, nrm=nrm, adpc=adpc[i])
                vals += [val]
                svals += [sval]
                cstrts += [cstrt]

            all_vals += [vals]

            plt.plot(nagts, vals, color=LINESCLRS[j],
                     marker=LINESMRKS[MAPSIDS[m]], markersize=12,
                     linewidth=LINEWIDTH, linestyle=':')

            plt.errorbar(nagts, vals, svals, linestyle='None', marker='^',
                     color=LINESCLRS[j])

            plt.legend(handles=handles, prop={'size': LGDFONTSIZE})

            text = ''

            for k, (a, b, c) in enumerate(zip(nagts, vals, cstrts)):
                # TODO: creating a variable to handle the displaying of
                #  `adpc`
                if dsn:
                    # text = "{}-{}".format(c, adpc) if adpc \
                    #     else "{}".format(c)
                    # Not displaying `adpc`
                    text = "{}".format(c)

                if display_value:
                    # If the current text is that of the last value on the
                    # x-axis, it will be displayed upon several lines
                    if a == nagts[-1]:
                        text = "{}:\n {}".format(str(int(b)), text) if dsn \
                            else str(int(b))
                    else:
                        text = "{}: {}".format(str(int(b)), text) if dsn \
                            else str(int(b))

                # Hack to avoid texts on the plot overlap
                # TODO: creating a generic procedure to handle that
                if i > 0:
                    print(cstrts[i])
                    if cstrts[i] == "cr":
                        plt.text(a + xoffset,
                                 b + (yoffset if b > all_vals[i - 1][k]
                                      else - yoffset),  # offset to avoid the
                                 # overlapping of the values of the strategies
                                 # to plot
                                 "",
                                 size=value_fontsize)
                    elif cstrts[i].startswith("rlpm"):
                        print(cstrts[i])
                        plt.text(a + xoffset,
                                 b + 200,  # offset to avoid the
                                 # overlapping of the values of the strategies
                                 # to plot
                                 text.replace(
                                     "rmaplpm_", '').replace("rlpm_", ''),
                                 size=value_fontsize)
                    elif cstrts[i].startswith("rmaplpm"):
                        print(cstrts[i])
                        plt.text(a + xoffset,
                                 b - 400,  # offset to avoid the
                                 # overlapping of the values of the strategies
                                 # to plot
                                 text.replace(
                                     "rmaplpm_", '').replace("rlpm_", ''),
                                 size=value_fontsize)
                    else:
                        plt.text(a + xoffset,
                                 b + (yoffset if b > all_vals[i - 1][k]
                                      else - yoffset),  # offset to avoid the
                                 # overlapping of the values of the strategies
                                 # to plot
                                 text.replace(
                                     "rmaplpm_", '').replace("rlpm_", ''),
                                 size=value_fontsize)
                else:
                    if cstrts[i] == "cr":
                        plt.text(a + xoffset,
                                 b + (yoffset if b > all_vals[i - 1][k]
                                      else - yoffset),  # offset to avoid the
                                 # overlapping of the values of the strategies
                                 # to plot
                                 "",
                                 size=value_fontsize)
                    elif cstrts[i].startswith("rlpm"):
                        print(cstrts[i])
                        plt.text(a + xoffset,
                                 b + 400,  # offset to avoid the
                                 # overlapping of the values of the strategies
                                 # to plot
                                 text.replace(
                                     "rmaplpm_", '').replace("rlpm_", ''),
                                 size=value_fontsize)
                    elif cstrts[i].startswith("rmaplpm"):
                        print(cstrts[i])
                        plt.text(a + xoffset,
                                 b - 600,  # offset to avoid the
                                 # overlapping of the values of the strategies
                                 # to plot
                                 text.replace(
                                     "rmaplpm_", '').replace("rlpm_", ''),
                                 size=value_fontsize)
                    else:
                        plt.text(a + xoffset, b,
                                 text.replace(
                                     "rmaplpm_", '').replace("rlpm_", ''),
                                 size=value_fontsize)
            j += 1

        i += 1


def prepare_bar_chart_plot(strts: list,
                           statpath: str,
                           adpc: str = None,
                           maps: list = None,
                           nagts: list = None,
                           duration: int = 3000,
                           mtr: int = 1,
                           nrm: bool = True,
                           mtr_handler=None):
    """
    Prepares a plot with the number of agents in abscissa and the metric value
    of metric id `mtr` in ordinate.

    :param strts: strategies' statistics to plot
    :type strts: str
    :param statpath:
    :type statpath: str
    :param adpc: additional directory path component
    :type adpc: str
    :param maps:
    :type maps:
    :param nagts:
    :type nagts:
    :param mtr_handler: metric handler, a function reference that handles
    the way the metric values are retrieved and returned for a given
    scenario `{<map>, <strategy>, <number of agents>}`
    :type mtr_handler:
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int

    :return:
    :rtype:
    """

    if adpc is None:
        adpc = ''

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    # Metric handler
    if mtr_handler is None:
        mtr_handler = get_means

    # Current metric's values to display for each number of agents
    mvals = []
    svals = []
    svals = []
    # Legends: current strategies with the map and the number of agents bound
    # to the current metric's values populating `mvals`
    xticks = []

    for m in maps:
        for strt in strts:
            for na in nagts:
                # `mval`: current metric's value
                # `sval`: current metric's value
                # `cstrt`: current strategy's name returned by the
                # metric handler
                mval, sval, cstrt = mtr_handler(strt=strt, statpath=statpath,
                                                tpl=m, nagts=na,
                                                duration=duration,
                                                mtr=mtr, nrm=nrm, adpc=adpc)
                mvals += [mval]
                svals += [sval]
                xticks += ["{}-{}-{}".format(m, na, cstrt)]

    ids = np.arange(len(xticks))  # the x locations for the strategies

    ax = plt.gca()  # Get the current `matplotlib.axes.Axes` instance on
    # the current figure matching the given keyword args, or create one.

    bars = plt.bar(ids, mvals)

    # Setting the axes' label font size
    # ax.tick_params(labelsize=FONTSIZE)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=FONTSIZE)
    plt.xticks(ids, xticks, rotation=70)
    # ax.set_xticks(x, legends, rotation=70)

    # plt.xlabel("Number of agents")
    plt.ylabel(MTRSNAMES[mtr])

    plt.title("{} as a function of the number of agents".
              format(MTRSNAMES[mtr]), fontsize=TITLEFONTSIZE)

    def autolabel(bars_arg):
        """
        Attach a text label above each bar displaying its height
        """
        for i, bar in enumerate(bars_arg):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., 1. * height,
                    format_value(height),
                    ha='center', va='bottom', fontsize=21)

    def format_value(value):
        return "%2.1f" % value

    autolabel(bars)

    plt.subplots_adjust(left=0.055, right=0.99, top=0.99, bottom=0.08)
    plt.show()


def prepare_best_strategy_plot(strts: list,
                               strt_name: str,
                               statpath: str,
                               adpc: str = None,
                               maps: list = None,
                               nagts: list = None,
                               duration: int = 3000,
                               mtr: int = 1,
                               handles: list = None,
                               nrm: bool = True,
                               xoffset: float = 0,
                               yoffset: float = 3,
                               dsn: bool = False,
                               display_value: bool = True):
    """
    Prepares a plot of the metric id `mtr` in ordinate of the best strategy
    displayed w.r.t. the number of agents in abscissa.

    :param strts: strategies' statistics to plot
    :type strts: str
    :param strt_name:
    :type strt_name:
    :param statpath:
    :type statpath: str
    :param adpc: additional directory path component
    :type adpc: str
    :param maps:
    :type maps:
    :param nagts:
    :type nagts:
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int
    :param yoffset:
    :type yoffset:
    :param xoffset:
    :type xoffset:
    :param dsn: displays the strategies' names upon the plot
    :type dsn: bool
    :param display_value:
    :type display_value: bool

    :return:
    :rtype:
    """

    if adpc is None:
        adpc = ''

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    # A list of `pyplot.Artist` (lines, patches) to be added to the legend
    if handles is None:
        handles = []

    # `strts`'s counter
    strts_cnt = {}
    for i, s in enumerate(strts):
        strts_cnt[strts[i]] = i

    # Number of handles if others have been already set beforehand
    nbh = len(handles)
    # Number of strategy handles
    nbstrth = 0

    # If nbh > 0 then the legends concerning the maps have already been
    # defined in a previous call to `prepare_plot`
    if nbh == 0:
        for m in maps:
            map_line = lines.Line2D([], [], color="black",
                                    marker=LINESMRKS[MAPSIDS[m]], label=m,
                                    linewidth=LINEWIDTH, linestyle=':')
            handles += [map_line]
    else:
        nbstrth = nbh - len(maps)

    strt_line = lines.Line2D([], [], color=LINESCLRS[nbstrth],
                             label=strt_name, linewidth=LINEWIDTH,
                             linestyle=':')
    handles += [strt_line]

    plt.xlabel("Number of agents")
    plt.ylabel(MTRSNAMES[mtr])
    # plt.title("{} as a function of the number of agents".
    #          format(MTRSNAMES[mtr]),
    #          fontsize=TITLEFONTSIZE)

    # Setting the axes' label font size
    '''
    ax = plt.gca()  # Get the current `matplotlib.axes.Axes` instance on
    # the current figure matching the given keyword args, or create one.
    ax.tick_params(labelsize=FONTSIZE)
    '''
    plt.xticks(fontsize=FONTSIZE)
    plt.yticks(fontsize=FONTSIZE)

    for m in maps:
        # Current metric's values to display for each number of agents
        mvals = []
        svals = []
        # Current strategies bound to the current metric's values
        # populating `mvals`
        cstrts = []
        for na in nagts:
            # `mval`: current metric's value
            # `cstrt`: current strategy's name returned by the
            # metric handler
            mval, sval, cstrt = best_strategy_metric(tpl=m, strts=strts,
                                                     nagts=na,
                                                     duration=duration,
                                                     mtr=mtr, nrm=nrm,
                                                     statpath=statpath,
                                                     adpc=adpc)
            mvals += [mval]
            svals += [sval]
            cstrts += [cstrt]

        plt.plot(nagts, mvals, color=LINESCLRS[nbstrth],
                 marker=LINESMRKS[MAPSIDS[m]], markersize=12,
                 linewidth=LINEWIDTH, linestyle=':')

        plt.errorbar(nagts, mvals, svals, linestyle='None', marker='^',
                     color=LINESCLRS[nbstrth])

        plt.legend(handles=handles, prop={'size': LGDFONTSIZE})

        for a, b, c in zip(nagts, mvals, cstrts):
            text = ''
            if display_value:
                text = "{}".format(str(int(b)))
            if dsn:
                text = "{}: {}".format(text, c) \
                    if display_value else "{}".format(c)
                # Hack to not display parameters of IEs
                # TODO: handling this issue to remove the hack
                text = text.replace("_0.2_i_14", ''). \
                    replace("_0.2", ''). \
                    replace("_0.5_i_14", ''). \
                    replace("_0.5", ''). \
                    replace("rhp", ''). \
                    replace("hp", '')

            plt.text(a + xoffset, b + yoffset,
                     text, size=FONTSIZE)


def prepare_metric_space_plot(strts: list,
                              statpath: str,
                              adpc: str = None,
                              maps: list = None,
                              duration: int = 3000,
                              handles: list = None,
                              nrm: bool = True,
                              xoffset: float = 2.0,
                              yoffset: float = 3.0,
                              mtr_handler=None,
                              display_value: bool = True):
    """
    Prepares a plot representing of the criterion space composed of MI
    in abscissa and QMI in ordinate, for each map, each number of agents
    and each strategy passed as argument.

    :param strts: strategies' statistics to plot
    :type strts: str
    :param statpath:
    :type statpath: str
    :param adpc: additional directory path component
    :type adpc: str

    Optional arguments:
    :param maps:
    :type maps:
    :param mtr_handler: metric handler, a function reference that handles
    the way the metric values are retrieved and returned for a given
    scenario `{<map>, <strategy>, <number of agents>}`
    :type mtr_handler:
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int
    :param yoffset:
    :type yoffset:
    :param xoffset:
    :type xoffset:
    :param display_value:
    :type display_value: bool

    :return:
    :rtype:
    """

    if adpc is None:
        adpc = ''

    if maps is None:
        maps = MAPS

    # Metric handler
    if mtr_handler is None:
        mtr_handler = get_means

    # A list of `pyplot.Artist` (lines, patches) to be added to the legend
    if handles is None:
        handles = []

    # Number of handles if others have been already set beforehand
    nbh = len(handles)
    # Number of strategy handles
    nbstrth = 0

    # If nbh > 0 then the legends concerning the maps have already been
    # defined in a previous call to `prepare_plot`
    if nbh == 0:
        for m in maps:
            map_line = lines.Line2D([], [], color="black",
                                    marker=LINESMRKS[MAPSIDS[m]], label=m,
                                    linewidth=LINEWIDTH, linestyle='')
            handles += [map_line]
    else:
        nbstrth = nbh - len(maps)

    # Counting starts at `nbstrth` to take into account previous
    # strategy handles already set
    i = nbstrth

    for strt in strts:
        strt_line = lines.Line2D([], [], color=LINESCLRS[i],
                                 label=strt, linewidth=LINEWIDTH,
                                 linestyle=':')
        handles += [strt_line]
        i += 1

    plt.xlabel(MTRSNAMES[1])
    plt.ylabel(MTRSNAMES[2])
    plt.title("Values of MI and QMI criteria as a function of the "
              "tested architectures", fontsize=TITLEFONTSIZE)

    # Setting the axes' label font size
    '''
    ax = plt.gca()  # Get the current `matplotlib.axes.Axes` instance on
    # the current figure matching the given keyword args, or create one.
    ax.tick_params(labelsize=FONTSIZE)
    '''
    plt.xticks(fontsize=FONTSIZE)
    plt.yticks(fontsize=FONTSIZE)

    i = 0
    for m in maps:
        # Counting starts at `lhid` to take into account previous handles
        # already set
        j = nbstrth
        for strt in strts:
            # Values of MI to display for each number of agents
            mis = []
            # Values of QMI to display for each number of agents
            qmis = []
            # Current strategies bound to the values of MI populating `mis`
            mi_cstrts = []
            # Current strategies bound to the values of QMI populating
            # `qmis`
            qmi_cstrts = []
            for na in NAGTS:
                # `mval`: current metric's value
                # `mi_cstrt`: current strategy's name returned by the
                # metric handler for MI
                # `qmi_cstrt`: current strategy's name returned by the
                # metric handler for QMI
                mi, smi, mi_cstrt = mtr_handler(tpl=m, strt=strt, nagts=na,
                                                duration=duration, mtr=1,
                                                nrm=nrm,
                                                statpath=statpath, adpc=adpc)
                mis += [mi]
                qmi, smi, qmi_cstrt = mtr_handler(tpl=m, strt=strt, nagts=na,
                                                  duration=duration, mtr=1,
                                                  nrm=nrm,
                                                  statpath=statpath, adpc=adpc)
                qmis += [qmi]
                mi_cstrts += [mi_cstrt]
                qmi_cstrts += [qmi_cstrt]

            plt.plot(mis, qmis, color=LINESCLRS[j],
                     marker=LINESMRKS[MAPSIDS[m]], markersize=12,
                     linestyle='')

            plt.legend(handles=handles, prop={'size': LGDFONTSIZE})

            if display_value:
                for a, b, na in zip(mis, qmis, NAGTS):
                    text = str(na)
                    plt.text(a + xoffset, b + yoffset, text, size=FONTSIZE)

            j += 1

        i += 1


def prepare_metric_space_plot_av_nagts(strts: list,
                                       statpath: str,
                                       adpc: str = None,
                                       maps: list = MAPS,
                                       duration: int = 3000,
                                       handles: list = None,
                                       nrm: bool = True,
                                       xoffset: float = 2.0,
                                       yoffset: float = 3.0,
                                       mtr_handler=None,
                                       display_value: bool = True):
    """
    Prepares a plot representing of the criterion space composed of MI
    in abscissa and QMI in ordinate, averaged over the population sizes for
    each map, each number of agents and each strategy passed as argument.

    :param strts: strategies' statistics to plot
    :type strts: str
    :param statpath:
    :type statpath:
    :param adpc: additional directory path component
    :type adpc: str

    Optional (keyword) arguments:
    :param maps:
    :type maps:
    :param mtr_handler: metric handler, a function reference that handles
    the way the metric values are retrieved and returned for a given
    scenario `{<map>, <strategy>, <number of agents>}`
    :type mtr_handler:
    :param handles: A list of `pyplot.Artist` (lines, patches) to be added
    to the legend
    :type handles: pyplot.Artist
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int
    :param yoffset:
    :type yoffset:
    :param xoffset:
    :type xoffset:
    :param display_value:
    :type display_value:

    :return:
    :rtype:
    """

    if adpc is None:
        adpc = ''

    # Metric handler
    if mtr_handler is None:
        mtr_handler = get_means
    # A list of `pyplot.Artist` (lines, patches) to be added to the legend
    if handles is None:
        handles = []

    # Number of handles if others have been already set beforehand
    nbh = len(handles)
    # Number of strategy handles
    nbstrth = 0

    # If nbh > 0 then the legends concerning the maps have already been
    # defined in a previous call to `prepare_plot`
    if nbh == 0:
        for m in maps:
            map_line = lines.Line2D([], [], color="black",
                                    marker=LINESMRKS[MAPSIDS[m]], label=m,
                                    linewidth=LINEWIDTH, linestyle='')
            handles += [map_line]
    else:
        nbstrth = nbh - len(maps)

    # Counting starts at `nbstrth` to take into account previous
    # strategy handles already set
    i = nbstrth

    for strt in strts:
        strt_line = lines.Line2D([], [], color=LINESCLRS[i],
                                 label=strt, linewidth=LINEWIDTH,
                                 linestyle=':')
        handles += [strt_line]
        i += 1

    plt.xlabel(MTRSNAMES[1])
    plt.ylabel(MTRSNAMES[2])
    plt.title("Values of MI and QMI criteria averaged over the numbers "
              "of agents as a function of the tested architectures",
              fontsize=TITLEFONTSIZE)
    # Setting the axes' label font size
    '''
    ax = plt.gca()  # Get the current `matplotlib.axes.Axes` instance on
    # the current figure matching the given keyword args, or create one.
    ax.tick_params(labelsize=FONTSIZE)
    '''
    plt.xticks(fontsize=FONTSIZE)
    plt.yticks(fontsize=FONTSIZE)

    i = 0
    for m in maps:
        # Counting starts at `lhid` to take into account previous handles
        # already set
        j = nbstrth
        for strt in strts:
            # Values of MI to display for each number of agents
            mis = []
            # Values of QMI to display for each number of agents
            qmis = []
            # Current strategies bound to the values of MI populating `mis`
            mi_cstrts = []
            # Current strategies bound to the values of QMI populating
            # `qmis`
            qmi_cstrts = []
            for na in NAGTS:
                # `mval`: current metric's value
                # `mi_cstrt`: current strategy's name returned by the
                # metric handler for MI
                # `qmi_cstrt`: current strategy's name returned by the
                # metric handler for QMI
                mi, smi, mi_cstrt = mtr_handler(tpl=m, strt=strt, nagts=na,
                                                duration=duration, mtr=1,
                                                nrm=nrm,
                                                statpath=statpath, adpc=adpc)

                mis += [mi]
                qmi, sqmi, qmi_cstrt = mtr_handler(tpl=m, strt=strt, nagts=na,
                                                   duration=duration, mtr=1,
                                                   nrm=nrm,
                                                   statpath=statpath,
                                                   adpc=adpc)

                qmis += [qmi]
                mi_cstrts += [mi_cstrt]
                qmi_cstrts += [qmi_cstrt]

            mis = [np.mean(mis)]
            qmis = [np.mean(qmis)]

            plt.plot(mis, qmis, color=LINESCLRS[j],
                     marker=LINESMRKS[MAPSIDS[m]], markersize=12,
                     linewidth=LINEWIDTH, linestyle='')

            plt.legend(handles=handles, prop={'size': LGDFONTSIZE})

            if display_value:
                for a, b, na in zip(mis, qmis, NAGTS):
                    text = "({}, {})".format(int(mis[0]), int(qmis[0]))
                    plt.text(a + xoffset, b + yoffset, text, size=FONTSIZE)

            j += 1

        i += 1


def prepare_bar_chart_plot_a_15(strts: list,
                                statpath: str,
                                maps: list = None,
                                nagts: list = None,
                                adpcs: list = None,
                                duration: int = 3000,
                                mtr: int = 1,
                                nrm: bool = True,
                                mtr_handler=None):
    """
    Prepares a bar chart plot of the metric `mtr`  for all the strategies
    `strts `the topology A and 15 agents

    :param strts: strategies' statistics to plot
    :type strts: str
    :param statpath:
    :type statpath: str
    :param maps:
    :type maps:
    :param nagts:
    :type nagts:
    :param adpcs: additional statistic directory path components, one for each
    strategy
    :type adpcs: str
    :param mtr_handler: metric handler, a function reference that handles
    the way the metric values are retrieved and returned for a given
    scenario `{<map>, <strategy>, <number of agents>}`
    :type mtr_handler:
    :param mtr: the metric whose values are to be plot
    :type mtr: int
    :param nrm: Metric must be normalised or not
    :type nrm: bool
    :param duration: number of periods
    :type duration: int

    :return:
    :rtype:
    """

    fontsize = 24

    if maps is None:
        maps = MAPS

    if nagts is None:
        nagts = NAGTS

    if adpcs is None:
        adpcs = [''] * len(strts)

    # Metric handler
    if mtr_handler is None:
        mtr_handler = get_means

    # Current metric's values to display for each number of agents
    mvals = []
    svals = []
    # Legends: current strategies with the map and the number of agents bound
    # to the current metric's values populating `mvals`
    xticks = []

    for m in maps:
        for i, strt in enumerate(strts):
            for na in nagts:
                # `mval`: current metric's value
                # `cstrt`: current strategy's name returned by the
                # metric handler
                mval, sval, cstrt = mtr_handler(strt=strt, statpath=statpath,
                                                tpl=m, nagts=na,
                                                duration=duration,
                                                mtr=mtr, nrm=nrm,
                                                adpc=adpcs[i])
                mvals += [mval]
                svals += [sval]
                xticks += ["{}".format(cstrt.
                                       replace("_100", '').
                                       replace("sgd_no_pre", "snp")).
                               replace("sgd_pre_", '').
                               replace("adagrad_pre_", '').
                               replace("--1", '').replace("rlpm_", '')]

    ids = np.arange(len(xticks))  # the x locations for the strategies

    ax = plt.gca()  # Get the current `matplotlib.axes.Axes` instance on
    # the current figure matching the given keyword args, or create one.

    bars = plt.bar(ids, mvals, color=["green", "red", "blue", "blue",
                                      "blue", "blue", "blue", "purple",
                                      "purple", "purple", "purple",
                                      "purple", "#0080ff", "#0080ff",
                                      "#0080ff", "#0080ff", "#0080ff"])

    plt.errorbar(nagts, mvals, svals, linestyle='None', marker='^')

    # Setting the axes' label font size
    # ax.tick_params(labelsize=FONTSIZE)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.xticks(ids, xticks)  # , rotation=70)
    # ax.set_xticks(x, legends, rotation=70)

    # plt.xlabel("Number of agents")
    plt.ylabel(("Normalised " if nrm else "") + MTRSNAMES[mtr],
               fontsize=fontsize)

    # plt.title("{} for the RLPM strategies as a function of the "
    #           "architectures and optimisers, for the topology A and 15 "
    #           "agents".format(MTRSNAMES[mtr]), fontsize=TITLEFONTSIZE)

    plt.legend((bars[0], bars[1],
                bars[2], bars[7]),
               ("HPCC",
                "CR",
                "SGD optimisation",
                "Adagrad optimisation"),
               fontsize=LGDFONTSIZE)

    def autolabel(bars_arg):
        """
        Attach a text label above each bar displaying its height
        """
        for i, bar in enumerate(bars_arg):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., 1. * height,
                    format_value(height),
                    ha='center', va='bottom', fontsize=fontsize)

    def format_value(value):
        return "%2.1f" % value

    autolabel(bars)

    plt.subplots_adjust(left=0.055, right=0.99, top=0.99, bottom=0.08)
    plt.show()
