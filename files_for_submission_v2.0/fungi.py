"""
This includes the studies and the ottolid
"""
import load_synth_extract
import general_tm_utils
"""
problems
300_217 mono
302_221 mono
303_225 mono
334_348 mono, euk
337_362 mono
350_385 mono
357_405 mono
371	428 mono
377_5555 mon
378	441
381 448
pg_390_471
pg_401_5569
"""

studytreelist=["pg_335_360", #Magnaporthe
               "pg_338_5527", #Cudonia and more
               "pg_339_365", # Phaesophaeria
               "pg_340_5532", #Neotyphodium
               "pg_343_5534", #Laboulbeniaceae
               "pg_348_381",#rhizopogon
               "pg_349_5539",#retiboletus
               "pg_353_5542",#aspergillus
               "pg_355_400",#Leotiomyceta
               "pg_358_406",#ceratocystis
               "pg_361_5551",#fusarium
               "pg_366_5552",#hypochnicium
               "pg_367_418",#armillaria
               "pg_368_5553",#Macrolepiota, Agaricaceae
               "pg_369_5554",#Rhizopogon
               "pg_370_426",#Cortinarius
               "pg_372_431",#Xerocomus
               "pg_373_432",#Penicillium
               "pg_374_433",#Penicillium
               "pg_375_436",#Colletotrichum
               "pg_376_438",#Neofusicoccum
               "pg_380_5560",#Lasiosphaeria
               "pg_382_449",#Cryphonectriaceae
               "pg_387_5562",#Ajellomycetaceae
               "pg_388_469",#Ophiocordycipitaceae
               "pg_389_470",#Leotiomycetidae
               "pg_393_482",#Helicobasidiaceae
               "pg_397_494",#Alternaria
               "pg_399_5565",#Parmeliaceae
               "pg_400_497",#Botryosphaeriaceae
               "pg_402_5570",#Aspergillus
               "pg_403_503",#Orbiliaceae
               "pg_404_506",#Nectriaceae
               "pg_405_507",#Botryosphaeriaceae
               "pg_407_513",#Penicillium
               "pg_408_5571",#Colletotrichum
               "pg_411_518",#Botryosphaeriaceae
               "pg_414_519",#Hypocreaceae
               "pg_415_5572",#Clavicipitaceae
               "pg_430_541",#Hebeloma
               "pg_441_5575",#Amphisphaeriaceae
               "pg_444_564",#Cryphonectriaceae
               "pg_446_565",#Cercospora
               "pg_447_5576",#Cryphonectriaceae
               "pg_448_5577",#Boletus
               "pg_449_570",#Sparassis
               "pg_450_574",#Physalacriaceae
               "pg_443_562",#Hypocreaceae
               "pg_463_604",#Clavicipitaceae
               "pg_470_615",#Lecania
               "pg_471_617",#Alternaria
               "pg_473_623",#Tilletia
               "pg_474_627",#Laetiporus
               "pg_475_5594",#Marasmiaceae
               "pg_477_633",#Agaricus
               "pg_479_636",#Flammulina
               "pg_480_637",#Vibrisseaceae
               "pg_481_644",#Neurospora
               "pg_482_5595",#Talaromyces
               "pg_483_647",#Neofusicoccum
               "pg_485_651"#Clavicipitaceae
               #"pg_494_666"#Aspicilia



               #"pg_2818_6563", # Fungi. Hibbett 2007
               #"pg_240_123",   # Pezizomycotina
               #"pg_827_1585",  # Blastocladiomycota
               #"pg_1144_5800", # Entomophthoromycota
               #"pg_439_5514",  # Glomeromycota
               ##"238_110",  # Ascomycota	<- mapped back to Eukaryota
               #"pg_1197_5822", # Fungi
               #"pg_2701_6271", # Basidiomycota	<- mapped back to Basidiomycota
               #"pg_1162_5805"  #Fungi
               ]
 
"""
studytreelist=["1162_5805",
               "1682_5491",
               "1665_5483",
               "1754_5492",
               "1692_3412",
               "1075_2094",
               "1079_5502",
               "1736_3492",
               "1737_3493",
               "736_1330",
               "1191_5507",
               "775_1445",
               "735_1328",
               "734_1325",
               "955_1877",
               "877_5506",
               "434_548",
               "744_5510",
               "439_5514",
               "1142_5799",
               #"238_109"
               ]
"""

studytreelistTF = [True] * len(studytreelist)

if __name__ == "__main__":
    from stephen_laptop_conf import *

	
    synthottolid="352914"

    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    download = True
    if download:
        general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc)    
    load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)
    """
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "/home/smitty/TEMP/"+i+".log"
        ttfntreefn = "/home/smitty/TEMP/"+i+".tre"
        load_synth_extract.run_load_single_ttfn(dott,dload,studyloc,tstudy_list,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,ttfntreefn)
    """
