import general_tm_utils

if __name__ == "__main__":
    from stephen_laptop_conf import *
    
    studytreelist = ["pg_2001_4100"]
    
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "/home/smitty/TEMP/"+i+".log"
        ttfntreefn = "/home/smitty/TEMP/"+i+".tre"
        general_tm_utils.load_nexson(studyloc,i,javapre,treemloc,dload,generallogfileloc,False,True)



