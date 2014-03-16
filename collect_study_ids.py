"""
Creates a list of studies currently being used for synthesis. 
"""
import re

#from stephen_desktop_conf import *

from microbes import studytreelist as microbelist
from plants import studytreelist as plantslist
from metazoa import studytreelist as metalist
from fungi import studytreelist as fungilist

studytreelist = []
studytreelist.extend(plantslist)
studytreelist.extend(metalist)
studytreelist.extend(fungilist)
studytreelist.extend(microbelist)

for i in studytreelist:
    studyid=i.split('_')[0]
    print studyid+".json"

