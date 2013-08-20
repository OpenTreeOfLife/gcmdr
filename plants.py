"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""

import load_synth_extract
from stephen_joseph_conf import *

synthottolid="10218"

studytreelist=["1022_1967",
               "562_817",
               "424_532",
               "1916_3902",
               "588_878",
               "2539_5465",
               "14_12",
               "180_794",
               #"574_840", upload problems
               "576_849",
               "581_859",
               "582_862",
               "598_926",
               "599_927",
               "603_940",
               "704_1266",
               "721_1298",
               "723_1300",
               #"724_3212", upload problems
               "921_4103",
               "1300_2613",
               "1302_2616",
               "915_1802",
               "915_1803",
               "9_1",
               "142_38",
               "21_37",
               "57_777",
               "58_775",
               "72_801",
               "75_1743",
               "535_768",
               "61_816",
               "284_185",
               "2546_5493",
               "1086_2111",
               "283_184",
               "713_1284",
               "54_949",
               "1116_2217",
               "412_2166"#conifers
               ]

print "loading synthottolid:",synthottolid
print "loading studytreelist:",studytreelist

load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
             treemloc,generallogfileloc,dsynth,synthottolid,treefn)
