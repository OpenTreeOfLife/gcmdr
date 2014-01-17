import os
import sys

"""
this will process the taxa_study.log
files

it will also record the mapcompat information
"""

filepre = "taxa_"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "python "+sys.argv[0]+" directory"
        sys.exit(0)
    id_name = {}
    id_studies = {}
    directory = sys.argv[1]
    for i in os.listdir(directory):
        if filepre in i:
            study = ""
            try:
                study = i.strip().split(filepre)[1].split(".")[0]
                int(study.split("_")[0])
                int(study.split("_")[1])
            except:
                continue
            tfile = open(i,"r")
            for j in tfile:
                spls = j.strip().split()
                num = spls[0].replace('"','')
                name = spls[1].replace('"','')
                if num not in id_name:
                    id_name[num] = name
                    id_studies[num] = []
                id_studies[num].append(study)
            tfile.close()
    for i in id_name:
        print i+"\t"+id_name[i]+"\t"+str(len(id_studies[i]))+"\t"+",".join(id_studies[i])
