"""
These shouldn't really ever change, except possibly the taxonomy.
"""

#location of studies
studyloc="/home/josephwb/Work/OToL/phylesystem"

#base directory
bdir="/home/josephwb/Work/OToL/treemachine/Synthesis/"

#location of just ott database
dott=bdir+"Life.2.8draft5.db"
#taxonomy file
taxfile=bdir+"ott2.8draft5/taxonomy.tsv"
synfile=bdir+"ott2.8draft5/synonyms.tsv"
#location of loading database
dload=bdir+"Loading.db"
#location of test output
outl=bdir+"gcmdr_testoutput"
#trashing the log file
generallogfileloc=bdir+"gcmdr_TRASHLOG"
#java prefix
javapre="java -XX:+UseConcMarkSweepGC -Xmx32g -server -jar"
#location of treemachine
treemloc="/home/josephwb/Work/OToL/treemachine/target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar"


