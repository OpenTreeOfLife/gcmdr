synthottolid="93302"

studytreelist=[

## Bacteria + Archaea

               "pg_2542_5590",   # Bacteria + Archaea. Lang et al. 2013. PLoS ONE

## Cyanobacteria
               "pg_2737_6322", # Nostocales. Werner et al. 2012. Phycologia
               #"pg_2425_6602", # Nostocales. Fewer et al. 2002. MPE # Was supposed to be in last round. See what is wrong. ***
               "pg_2738_6323", # Oscillatoriales, pseudanabaenales. Kling et al. 2012. Fottea Olomouc
               "pg_2738_6324", # Oscillatoriales, pseudanabaenales. Kling et al. 2012. Fottea Olomouc
               "pg_2554_5580", # Oscillatoriales. Engene and Paul. 2013. J. Phycology
               "pg_2892_6700", # Cyanobacteria. Rigonato et al. 2013. Envir. Microbiol.
               "pg_2891_6699", # Cyanobacteria. Rigonato et al. 2012. FEMS Microbiol. Ecol.
               "pg_2739_6601", # Cyanobacteria. Schirrmeister et al. 2011. BMC Evol. Biol. # ToL level study

## Archaea
               "ot_106_1",       # Archaea. Matte-Tailliez et al. 2002. MBE
               "pg_2731_6428",   # Archaea. Barns et al. 1996. PNAS
               "pg_2715_6308",   # Archaea. Groussin. 2011. MBE

## From last round:
               "pg_263_149",
               "pg_2713_6309",
               #"2413_5093",
     #          "pg_2715_6308", # currently not working for some reason, but was in last round
     #          "pg_2739_6601", # currently not working for some reason, but was in last round
               #"2737_6322",
               #"2738_6323",
               "pg_2753_6360",
               "pg_2742_6342",
               "pg_2757_6369",
               #"2760_6375",#Exception in thread "pg_main" java.lang.IllegalStateException: this child is mapped the same graph node (Node[3114879]) as its parent [Alexandrium tamarense]
               "pg_2553_5579",
               "pg_2556_5586",
               #"2484_5346",
               "pg_312_264",
               "pg_313_6681", # fixed Grant et al. tree (topology)
               "pg_2484_6607",
               "pg_2849_6615",
               "pg_2822_6569",   # Parfrey et al. 2011. PNAS not included in last round, but it is good. right?

               ]
studytreelistTF = [True] * len(studytreelist)

if __name__ == "___main__":
	import load_synth_extract
	from stephen_laptop_conf import *

	synthottolid="93302"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)
