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

if __name__ == "__main__":
    studies = []
    for i in os.listdir(directory):
        studies.append(i[0:len(i)-len(lend)])
    sl = set(studies)
    for i in sl:
        try:
            fl = open(directory+"/"+i+tend)
            ts = fl.readline()
            fl.close()
            if len(ts) > 1:
                tr = tree_reader.read_tree_string(ts)
                for j in tr.iternodes():
                    if len(j.label) > 1:
                        print i,j.label
        except:
            print "some problem with "+i
