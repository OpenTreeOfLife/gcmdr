"""
You don't have to keep these names. This is just to demonstrate that the configuration can be like this.
"""

PREFIX="life"

#location of studies
studyloc="/home/smitty/TEMP/phylesystem/"
#location of just ott database
dott="/home/smitty/apps/neo4j-community-1.9.7/data/gol.ott_2_8_5.db_just_ott"
#taxonomy file
taxfile = "/home/smitty/TEMP/ott26/ott/taxonomy.tsv"
synfile = "/home/smitty/TEMP/ott26/ott/synonyms.tsv"
taxversion = "2.8_5"
#location of loading database
dload="/home/smitty/apps/neo4j-community-1.9.7/data/"+PREFIX+"_loading.db"
#location of test output
outl="/home/smitty/TEMP/testloc"
#trashing the log file
generallogfileloc = "/home/smitty/TEMP/gcmdr_TEMP"
#location of synth database
dsynth="/home/smitty/apps/neo4j-community-1.9.7/data/"+PREFIX+"_synth.db"
#location of synth treefile
treefn="/home/smitty/TEMP/"+PREFIX+"_synth.tre"
#java prefix
javapre="java -XX:+UseConcMarkSweepGC -Xmx14g -server -jar"
#location of treemachine
treemloc="/home/smitty/Dropbox/programming/eclipse/opentree-treemachine/target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar"
