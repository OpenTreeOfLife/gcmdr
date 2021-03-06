import general_tm_utils
import tree_reader
import sys

"""
sequence of commands:
1) run this file: python load_mls_JWB.py
2) perform MLS ANALYSIS: run.sh <aname>_mls.NEX
3) run this file: python mls_posttree_fix_JWB.py <in treename> <out treename>
4) convert OTTIDs back to names: java -jar /home/josephwb/Work/OToL/treemachine/target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar labeltipsottol TREEFILE /home/josephwb/Work/OToL/treemachine/Synthesis/Life.2.8draft5.db  | tail -n +2 > TREEFILEOUT
"""

sys.path.insert(0, 'files_for_submission_v2.0')

#from goo import studytreelist as goolist
#from mammals import studytreelist as mammalslist
from birds import studytreelist as birdslist
#from tetrapoda import studytreelist as tetrapodalist
#from decapods import studytreelist as decapodlist
#from plants import studytreelist as plantslist
#from metazoa import studytreelist as metalist
#from fungi import studytreelist as fungilist
#from microbes import studytreelist as microbelist

#studytreelist = ["pg_420_522", "pg_2015_4152"]
studytreelist = []

#studytreelist.extend(goolist)
#studytreelist.extend(mammalslist)
studytreelist.extend(birdslist)
#studytreelist.extend(tetrapodalist)
#studytreelist.extend(decapodlist)
#studytreelist.extend(plantslist)
#studytreelist.extend(metalist)
#studytreelist.extend(fungilist)
#studytreelist.extend(microbelist)

taxtreefile = "tax.tree"
aname = "Aves_7July2014"
mlsout = aname + "_mls.NEX"
tgenerallogfileloc = "/home/josephwb/TEMP/"

if __name__ == "__main__":
    from wopr_conf import *
    print "Processing studies: ", studytreelist
    download = False
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
