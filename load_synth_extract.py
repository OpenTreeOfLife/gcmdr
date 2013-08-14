from general_tm_utils import *
from general_utils import *

#this is my conf, make your own -- no need to commit
from stephen_desktop_conf import *

#getting the studytreelist from this file
#getting the synthottolid from here as well
from plants_sm import *

print "loading synthottolid:",synthottolid
print "loading studytreelist:",studytreelist

delete_database(dload)
copy_database(dott,dload)

print "loading trees"
for i in studytreelist:
    load_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)

append = True

delete_database(dsynth)
copy_database(dload,dsynth)

print "synthesizing"
run_synth(javapre,treemloc,dsynth,synthottolid,studytreelist,generallogfileloc,append)

print "extracting"
extract_synth(javapre,treemloc,dsynth,synthottolid,treefn,append)

