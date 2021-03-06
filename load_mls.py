import general_tm_utils
import tree_reader
import sys

"""
commands
#java -jar target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar taxtree UID OUTFILE ~/apps/neo4j-community-1.9.7/data/gol.ott_2_8_5.db_just_ott
this file
ANALYSIS
java -jar /home/smitty/Dropbox/programming/eclipse/opentree-treemachine/target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar labeltipsottol TREEFILE ~/apps/neo4j-community-1.9.7/data/gol.ott_2_8_5.db_just_ott > TREEFILEOUT

THEN for synthesis you do delete_knees.py infile outfile
java -jar target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar pgloadindnew ~/apps/neo4j-community-1.9.7/data/life_loading.db ~/Downloads/MLS-1.0/mls_noknees.tre > test.out
java -jar target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar synthesizedrafttreelist_ottid 1058517 /home/smitty/Downloads/MLS-1.0/mls_noknees.tre,taxonomy ~/apps/neo4j-community-1.9.7/data/life_synth.db > temp
java -jar target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar extractdrafttree_ottid 1058517 test.tre ~/apps/neo4j-community-1.9.7/data/life_synth.db
"""

"""
this is how you load from another folder
"""
sys.path.insert(0, 'files_for_submission_v2.0/MLS_MPR_files')
#from fungi import studytreelist
from plants_mls_groups import deepplants_studytreelist as studytreelist

taxtreefile = "tax.tree"
mlsout = "mls.test"
tgenerallogfileloc = "/home/smitty/TEMP/"

if __name__ == "__main__":
    from stephen_laptop_conf import *
    download = True
    if download:
        general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc)
    taxalist = set()
    treestrings = []
    for i in studytreelist:
        glog = tgenerallogfileloc+i+".log"
        ttfntreefn = tgenerallogfileloc+i+".tre"
        tstudy_list = [i]
        general_tm_utils.load_nexson(studyloc,i,javapre,treemloc,dload,glog,False,True)
        fl = open(glog,"r")
        fl2 = open(ttfntreefn,"w")
        treestring = ""
        start = False
        for i in fl:
            if i.strip() == "MRP":
                break
            if start:
                fl2.write(i)
                treestring = i.strip()
                break
            if i.strip() == "TREEUID":
                start = True
        fl2.close()
        fl.close()
        print treestring
        treestrings.append(treestring)
        tree = tree_reader.read_tree_string(treestring)
        for i in tree.leaves():
            taxalist.add(i.label)
    general_tm_utils.extract_taxonomy_from_ids(javapre,treemloc,dload,",".join(taxalist),taxtreefile)
    outfile = open(mlsout,"w")
    outfile.write("#NEXUS\n")
    outfile.write("BEGIN TAXA;\n\tDIMENSIONS NTAX=");
    ttf = open(taxtreefile,"r")
    taxstring = ttf.readline()
    tree = tree_reader.read_tree_string(taxstring);
    taxs = []
    for i in tree.iternodes():
        taxs.append(i.label)
    ttf.close()
    outfile.write(str(len(taxs))+";\n\ttaxlabels\n")
    for i in taxs:
        outfile.write(i+"\n")
    outfile.write(";\nend;\n\nBEGIN TREES;\n\tproperties partialtrees=yes;\n")
    count = 0
    for i in treestrings:
        outfile.write("\ttree "+studytreelist[count]+" = [&R] "+i+"\n")
        count += 1
    outfile.write("\ttree taxonomy = [&R] "+taxstring+"\nend;\n")
    outfile.close()
