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
    "574_840"]

general_utils.delete_database(dload)
general_utils.copy_database(dott,dload)

for i in studytreelist:
    general_tm_utils.test_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
append = True
general_tm_utils.run_synth(javapre,treemloc,dsynth,"10218",studytreelist,generallogfileloc,append)
general_tm_utils.extract_synth(javapre,treemloc,dsynth,"10218",generallogfileloc,append)

