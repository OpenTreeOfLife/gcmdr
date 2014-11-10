"""
this is intended to process the files from the load_studies.py script
where we can get loaded names of the tips and internal nodes

this will also extract the compatible information from the log file
"""
import os
import sys

import tree_reader
import node

directory = "files_for_submission_v2.0/Inf-mono_log"
lend = ".log"
tend = ".tre"

outfilen = "loadlog.results"

if __name__ == "__main__":
    studies = []
    
    outfile = open(outfilen,"w")

    for i in os.listdir(directory):
        if lend in i:
            studies.append(i[0:len(i)-len(lend)])
    sl = set(studies)
    for i in sl:
        print i
        try:
            fl = open(directory+"/"+i+tend,"r")
            ts = fl.readline()
            if "WARN" in ts:
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
                tl = open(directory+"/"+i+lend,"r")
                for j in tl:
                    if j[0] == "\t" and "compatible" in j:
                        spls = j.strip().split(" as compatible ")
                        spls2 = spls[0].split(" ")
                        if spls2[1] == spls2[-1]:
                            continue
                        name = spls2[2]
                        idd = spls2[3]
                        outfile.write(i+","+idd+"_c,"+name+"\n")
                tl.close()
        except:
            print "some problem with "+i
    
    outfile.close()
