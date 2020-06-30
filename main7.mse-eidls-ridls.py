# -*- coding: utf-8 -*-

import sys
import torch

from maptor import Paths
import maptor.util.argsparser as parser
from torch.nn.modules.loss import MSELoss

sys.path.append(Paths.LOCALPTRN)
from lstmpathmaker.data.IPDataLoader import IPDataLoader


args = parser.parse_args()

ipdl = IPDataLoader(nagts=args.nagts, tpl=args.map, datasrc=args.datasrc,
                    strt=args.strategy, strt_variant=args.variant,
                    duration=args.duration, soc_name=args.society,
                    inf_exec_id=args.inf_exec_id, sup_exec_id=args.sup_exec_id)

ipdl.load_data()
viidls = ipdl.domain_data
vidls = ipdl.target_data
veidls = ipdl.load_veidls()

zeros = torch.zeros(veidls.size())

# Corrected veidls
c_veidls = torch.min(viidls, torch.max(veidls, zeros))

criterion = MSELoss()

print("{} {}: {}, {}".format(args.strategy, args.variant, args.map,
                             args.nagts))
print(criterion(vidls, veidls))
print(criterion(vidls, c_veidls))


