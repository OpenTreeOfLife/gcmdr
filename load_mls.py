import general_tm_utils
import tree_reader

"""
commands
java -jar target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar taxtree UID OUTFILE ~/apps/neo4j-community-1.9.7/data/gol.ott_2_8_5.db_just_ott
this file
ANALYSIS
java -jar /home/smitty/Dropbox/programming/eclipse/opentree-treemachine/target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar labeltipsottol TREEFILE ~/apps/neo4j-community-1.9.7/data/gol.ott_2_8_5.db_just_ott > TREEFILEOUT
"""

if __name__ == "__main__":
    from stephen_laptop_conf import *
    
    studytreelist = [
               "pg_2876_6670" # Tinamidae. Bertelli, Sara, Ana Luz Porzecanski
               ]
    download = True
    if download:
        general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc)
    cpcmd = "cat "
    taxalist = set()
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "/home/smitty/TEMP/"+i+".log"
        ttfntreefn = "/home/smitty/TEMP/"+i+".tre"
        cpcmd += ttfntreefn+" "
        general_tm_utils.load_nexson(studyloc,i,javapre,treemloc,dload,generallogfileloc,False,True)
        fl = open(generallogfileloc,"r")
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
        tree = tree_reader.read_tree_string(treestring)
        for i in tree.leaves():
            taxalist.add(i.label)
    general_tm_utils.extract_taxonomy_from_ids(javapre,treemloc,dload,",".join(taxalist),"t")
    print cpcmd +" > mls.trees"
