import os

PCKGROOT = os.path.abspath(os.path.dirname(__file__)) + "/../../"

DATAROOT = os.environ['MAPDATA']

DATA = DATAROOT + "/Pytrol-Resources/"

LOCALLOGS = PCKGROOT + "/logs/logs/"

LOGS = DATA + "/logs/"

EXECS = DATA + "/execs/"

LOCALSTATS = PCKGROOT + "/stats/"

STATS = DATA + "/stats/"

LOCALPYTROL = PCKGROOT + "/../Pytrol/"

LOCALPTRN = PCKGROOT + "/../Pytorch-Trainer/"

# The LSTMPathMaker-Resources
PTRNR = os.environ["HOME"] + "/Data/Pytorch-Trainer-Resources/"

DIRPATHMODELS = PTRNR + "/models/"

Json = DATA + "xmlToJsonLogs/logs/json-processed/"

BIN = DATA + "/logs-bin/"

VIIDLS = DATA + "/logs-viidls/"

VIDLS = DATA + "/logs-vidls/"

EIDLS = DATA + "/logs-veidls/"

# Log repository for the on-vertex binary position paths
LOCALBIN = PCKGROOT + "/logs/logs-bin/"

# Log repository for the individual on-vertex individual idlenesses of
# agents
LOCALVIIDLS = PCKGROOT + "/logs/logs-viidls/"

# Log repository for the on-vertex real idlenesses of agents
LOCALVIDLS = PCKGROOT + "/logs/logs-vidls/"

# Log repository for the on-vertex estimated idlenesses of agents
LOCALVEIDLS = PCKGROOT + "logs/logs-veidls/"

MAPS = DATA + "/maps/json/"

LOC = DATA + "/maps/loc/"

BINMAPS = DATA + "/maps/json_bin/"

PROBMAPS = DATA + "/maps/json_prob/"
