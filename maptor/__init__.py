# -*- coding: utf-8 -*-

import os

from .model import *

NAGTS = [1, 5, 10, 15, 25]
MAPS = ["islands", "map_a", "grid", "map_b", "circle", "corridor"]
MAPSIDS = {"islands": 0, "map_a": 1, "grid": 2, "map_b": 3, "circle": 4,
           "corridor": 5}
MTRSNAMES = ["Average Idleness", "MI", "QMI", "Worst Idleness",
             "Variance of interval", "Standard Deviation"]

# LINESCLRS = ['g', "blue", "orange", "black", "grey", "brown", "#007399",
#              "#0066ff",'y', 'c', 'm', 'k', 'w', "#3333ff", "#000066"]
LINESCLRS = ['g', 'r', "blue", "orange", "black", "grey", "brown", "#007399",
             "#0066ff",'y', 'c', 'm', 'k', 'w', "#3333ff", "#000066"]

LINESMRKS = ['o', 's', 'P', 'v', '^', '<', '>', '1', '2', '3', '4', '8']

LINEWIDTH = 2.5
FONTSIZE = 24
LGDFONTSIZE = 24
TITLEFONTSIZE = 24
