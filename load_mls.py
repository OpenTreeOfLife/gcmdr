import general_tm_utils
import tree_reader

"""
commands
java -jar target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar taxtree UID OUTFILE ~/apps/neo4j-community-1.9.7/data/gol.ott_2_8_5.db_just_ott
this file
ANALYSIS
java -jar /home/smitty/Dropbox/programming/eclipse/opentree-treemachine/target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar labeltipsottol TREEFILE ~/apps/neo4j-community-1.9.7/data/gol.ott_2_8_5.db_just_ott > TREEFILEOUT
"""

taxtreefile = "tax.tree"
mlsout = "mls.test"
generallogfileloc = "/home/smitty/TEMP/"

if __name__ == "__main__":
    from stephen_laptop_conf import *
    
    studytreelist = [
               "pg_259_142", #Cercis FABALES!
               "pg_264_150", #Coursetia FABALES!
               "pg_267_161", #Ateleia (Swartzieae-Leguminosae) FABALES!
               "pg_2077_4291", #Podalyria (Fabaceae, Podalyrieae) FABALES!
               "pg_293_201", #Mimosa FABALES!
               "pg_197_784", #Phaseolus FABALES!
               "pg_595_896", #Senna FABALES!
               "pg_131_6236", #Trifolium FABALES!
               "pg_2689_6241", #Lupinus FABALES!
               "pg_597_906", #Machaerium (Leguminosae) FABALES!
               "pg_2001_4100", #Astragalus FABALES!
               "pg_606_5290", #Trifolieae and Vicieae FABALES!
               "pg_270_159", #Indigofereae FABALES!
               "pg_596_901", #Genisteae (Leguminosae) FABALES!
               "pg_294_202", #Detarieae (Caesalpinioideae) FABALES!
               "pg_292_199", #(Diocleinae: Papilionoideae) FABALES!
	       "pg_58_775", #Crotalarieae (Fabaceae) FABALES!
               "pg_548_798", #Vigna FABALES!
               "pg_2055_4234",  #Genistoid legumes FABALES!
               "pg_2057_4240", #papilionoid FABALES!
               "pg_2127_4426", #Papilionoideae; Vataireoid Clade FABALES!
               "pg_594_890", #robinioid legumes FABALES!
               "pg_261_145", #Caesalpinieae FABALES!
               "pg_57_777", #Podalyrieae (Fabaceae) FABALES!
               "pg_1087_2114", #phaseoloid FABALES!
               "pg_1087_2115", #phaseoloid FABALES!
               "pg_2690_6243", #Fabaceae FABALES!
               "pg_2045_4213", #Acacia FABALES!
               "pg_605_947", #Strophostyles (Fabaceae) FABALES!
               "pg_271_5017" #Polygalaceae FABALES!
               ]
    download = True
    if download:
        general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc)
    taxalist = set()
    treestrings = []
    for i in studytreelist:
        glog = generallogfileloc+i+".log"
        ttfntreefn = generallogfileloc+i+".tre"
        tstudy_list = [i]
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
    outfile.write("\ttree taxonomy = [&R] "+taxstring+"\nend;\n")
    outfile.close()
