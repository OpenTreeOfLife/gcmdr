import general_tm_utils

if __name__ == "__main__":
    from stephen_laptop_conf import *
    
    studytreelist = ["pg_259_142", #Cercis FABALES!
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
               "pg_271_5017", #Polygalaceae FABALES!
               ]
    
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "/home/smitty/TEMP/"+i+".log"
        ttfntreefn = "/home/smitty/TEMP/"+i+".mrp"
        general_tm_utils.load_nexson(studyloc,i,javapre,treemloc,dload,generallogfileloc,False,True)
        fl = open(generallogfileloc,"r")
        fl2 = open(ttfntreefn,"w")
        start = False
        for i in fl:
            if start:
                fl2.write(i)
            if i.strip() == "MRP":
                start =True
        fl2.close()
        fl.close()


