from general_tm_utils import *
from general_utils import *

#this is my conf, make your own -- no need to commit
from stephen_laptop_conf import *

studytreelist=["562_817",
    "1916_3902",
    "588_878",
    "2539_5465",
    "14_12",
    "180_794",
    "574_840"]

delete_database(dload)
copy_database(dott,dload)

for i in studytreelist:
    load_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)

