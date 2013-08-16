"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""
import load_synth_extract
from stephen_joseph_conf import *

synthottolid="805080"

studytreelist=["562_817",#plants start
               #"424_532", once next pull is done
               "1916_3902",
               "588_878",
               "2539_5465",
               "14_12",
               "180_794",
               "576_849",
               "581_859",
               "582_862",
               "598_926",
               "599_927",
               "603_940",
               "704_1266",
               "721_1298",
               "723_1300",
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
               "2577_5980",#metazoa start
               "420_522",
               "1600_3231",
               "1428_2855",
               "2415_5096",
               "423_2857",
               "1870_3769",
               "2589_6001",
               "2585_5994",
               "2576_5975",
               "2015_4152",
               "2460_5285",
               "421_523",
               "1344_2675",
               "1482_5228",
               "1217_2455",
               "1162_5805",#fungi start
               "1682_5491",
               "1665_5483",
               "1754_5492",
               "1692_3412",
               "1075_2094",
               "1079_5502",
               "1736_3492",
               "1737_3493",
               "736_1330",
               "1191_5507",
               "775_1445",
               "735_1328",
               "734_1325",
               "955_1877",
               "877_5506",
               "434_548",
               "744_5510",
               "439_5514",
               "1142_5799",
               "238_109"]


print "loading synthottolid:",synthottolid
print "loading studytreelist:",studytreelist

load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
             treemloc,generallogfileloc,dsynth,synthottolid,treefn)
