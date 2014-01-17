synthottolid="805080"

studytreelist=["425_5976"] # Eukaryota. Katz et al. 2012. Syst Biol.

if __name__ == "__main__":
	import load_synth_extract
	from stephen_desktop_conf import *

	synthottolid="805080"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn)
