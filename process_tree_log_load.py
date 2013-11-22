"""
this is intended to process the files from the load_studies.py script
where we can get loaded names of the tips and internal nodes
"""
import os

import tree_reader
import node

directory = "loadlog"
lend = ".log"
tend = ".tre"

outfilen = "loadlog.results"

if __name__ == "__main__":
    studies = []
    
    outfile = open(outfilen,"w")

    for i in os.listdir(directory):
        studies.append(i[0:len(i)-len(lend)])
    sl = set(studies)
    for i in sl:
        try:
            fl = open(directory+"/"+i+tend,"r")
            ts = fl.readline()
            fl.close()
            if len(ts) > 1:
                #read the tree first
                tr = tree_reader.read_tree_string(ts)
                for j in tr.iternodes():
                    if len(j.label) > 1:
                        idd = j.label.split("_")[-1]
                        outfile.write(i+","+idd+","+j.label[0:-len(idd)-1]+"\n")
                #read the log next
                #for now, everything comes from the trees
        except:
            print "some problem with "+i
    
    outfile.close()
