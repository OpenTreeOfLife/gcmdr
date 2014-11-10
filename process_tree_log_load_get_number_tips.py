"""
this is intended to process the files from the load_studies.py script
where we can get loaded names of the tips and internal nodes

this will also extract the compatible information from the log file
"""
import os

import tree_reader
import node

directory = "files_for_submission_v2.0/Inf-mono_log/"
tend = ".tre"
lend = ".log"

outfilen = "all.numtips.results"

if __name__ == "__main__":
    studies = []
    
    outfile = open(outfilen,"w")

    for i in os.listdir(directory):
        if lend in i:
            studies.append(i[0:len(i)-len(lend)])
    sl = set(studies)
    for i in sl:
        try:
            fl = open(directory+"/"+i+tend,"r")
            ts = fl.readline()
            if "WARN" in ts:
                ts = fl.readline()
            fl.close()
            if len(ts) > 1:
                #read the tree first
                tr = tree_reader.read_tree_string(ts)
                outfile.write(str(len(list(tr.leaves())))+"\n")
        except:
            print "some problem with "+i
    
    outfile.close()
