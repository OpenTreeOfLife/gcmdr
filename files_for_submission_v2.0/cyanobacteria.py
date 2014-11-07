synthottolid="225495"

studytreelist=[
               "pg_2737_6322", # Nostocales. Werner et al. 2012. Phycologia
               #"pg_2425_6602", # Nostocales. Fewer et al. 2002. MPE # Was supposed to be in last round. See what is wrong. ***
               "pg_2738_6323", # Oscillatoriales, pseudanabaenales. Kling et al. 2012. Fottea Olomouc
               "pg_2738_6324", # Oscillatoriales, pseudanabaenales. Kling et al. 2012. Fottea Olomouc
               "pg_2554_5580", # Oscillatoriales. Engene and Paul. 2013. J. Phycology
               "pg_2892_6700", # Cyanobacteria. Rigonato et al. 2013. Envir. Microbiol.
               "pg_2891_6699", # Cyanobacteria. Rigonato et al. 2012. FEMS Microbiol. Ecol.
               "pg_2739_6601", # Cyanobacteria. Schirrmeister et al. 2011. BMC Evol. Biol. # ToL level study
               "pg_2713_6309", # Arthrospira. Dadheech et al. 2010. Phycologia
               ]
studytreelistTF = [True] * len(studytreelist)
if __name__ == "___main__":
	import load_synth_extract
	from wopr_conf import *

	synthottolid="225495"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)
