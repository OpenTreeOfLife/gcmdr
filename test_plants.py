import general_tm_utils
import general_utils

#this is my conf, make your own -- no need to commit
from stephen_laptop_conf import *

studytreelist=["562_817",
    "1916_3902",
    "588_878",
    "2539_5465",
    "14_12",
    "180_794",
    #"574_840",
    "576_849",
    "581_859",
    "582_862",
    "598_926",
    "599_927",
    "603_940",
    "704_1266",
    "721_1298",
    "723_1300",
    #"724_3212",
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
    "1116_2217"]

general_utils.delete_database(dload)
general_utils.copy_database(dott,dload)

for i in studytreelist:
    general_tm_utils.test_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
append = True
general_tm_utils.run_synth(javapre,treemloc,dsynth,"10218",studytreelist,generallogfileloc,append)
general_tm_utils.extract_synth(javapre,treemloc,dsynth,"10218",generallogfileloc,append)

