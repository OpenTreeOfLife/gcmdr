"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""
import load_synth_extract
from general_tm_utils import *
from general_utils import *

studytreelist=["2539_6294",#Soltis et al. 2011
               "715_1289", #Barnadesioideae
               "329_324", #Hieracium
               "9_1",#Campanulidae
               "709_1276", # Lobelioideae, very non monophyletic
               "41_1396",#Feddea
               "82_5792",#Campanula , very non monophyletic campanula
               "932_1831" #Goodeniaceae, tons of non monophyly
               ]

studytreelistTF = [True] * len(studytreelist)

if __name__ == "__main__":
    treemloc = "treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar" #treemachine location
    javapre = "java -Xmx8g -jar" #java running information
    dott = "example/asterales_taxonomy.db" #database location for taxonomy
    taxfile = "example/aster/taxonomy.tsv" #location of taxonomy loading file
    synfile = "example/aster/synonyms.tsv" #location of synonyms file
    dload = "example/asterales_loading.db" #database location for loading studies
    dsynth = "example/asterales_synth.db" #databsae location for synthesis
    synthottolid="1042120" #ott id for starting synthesis
    treefn = "example/asterales_synth.tre" #filename for tree
    generallogfileloc = "example/logfile" #log file for spitting out lots of information
    studyloc = "example/nexsons/" #location for the nexsons

    delete_database(dott)
    print "loading taxonomy"
    load_taxonomy(treemloc,javapre,dott,taxfile,synfile)

    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist

    load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
                 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)
