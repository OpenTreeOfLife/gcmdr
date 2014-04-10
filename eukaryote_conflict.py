from general_tm_utils import *
from general_utils import *

studytreelist=[
        "2847_6609",#He et al, 2014
        "2826_6574",#Burki et al., 2007
        "2826_6575",#Burki et al., 2007
        "2822_6569",#Parfrey et al., 2011
        "425_5976",#Katz et al., 2012
        "2413_5093"#Derelle and Lang 2011
            ]

studytreelistTF = [False] * len(studytreelist)

if __name__ == "__main__":
    synthottolid ="304358" #"93302" #cellular organisms
    print "loading studytreelist:",studytreelist
    depth = 2
    #location of studies
    studyloc="/media/data/avatol_nexsons"
    #location of just ott database
    dott="/media/data/neo4j-community-1.8/data/gol.ott_2_6_draft2.db_just_ott"
    dload="/media/data/neo4j-community-1.8/data/eukaryote_conflict_loading_no_map.db"
    #java prefix
    javapre="java -XX:+UseConcMarkSweepGC -Xmx32g -server -jar"
    #location of treemachine
    treemloc="/media/data/Dropbox/programming/eclipse/opentree-treemachine/target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar"
    generallogfileloc = "TEMP"
    outfn = "/media/data/eukaryote_conflict_no_map.graphml" #name of the graph figure file
    delete_database(dload)
    copy_database(dott,dload)
    mapcompat = studytreelistTF
    print "loading trees"
        
    for i in studytreelist:
        load_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
    count = 0
    for i in studytreelist:
        if mapcompat[count] == True: 
            mapcompat_one_study(studyloc,i,javapre,treemloc,dload,generallogfileloc,"TEST",False)
        count += 1
    print "extracting"
    extract_graphml(javapre,treemloc,dload,synthottolid,outfn,depth)
