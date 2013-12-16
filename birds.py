studytreelist=[
     ## Birds
               "2577_5980", # Galliformes. Wang et al. 2013. PLoS ONE
               "2658_6192", # Trochilidae. McGuire et al. 2007. Syst. Biol.
               "2707_6281", # Icteridae. Powell et al. 2013. MPE
               "1966_4019", # Maluridae. Lee et al. 2011. Syst. Biol.
               "2600_6022", # Paridae. Johansson et al. 2013. MPE
               "2599_6021", # Alaudidae (larks). Alstrom et al. 2013. MPE
               "2591_6008", # Parulidae (warblers). Lovette et al. 2008. MPE
               "2454_5247", # Thamnophilus. Brumfield and Edwards. 2007. Evolution
               "2692_6245", # Fringillidae. Zuccon et al. 2012. MPE
               "2702_6274", # core Corvoidea. Aggerbeck et al. 2014. MPE
               "2575_5974", # Passeriformes. Barker et al. 2013. Syst. Biol.
               "2015_4152", # Passeriformes. Odeen et al. 2011. Evolution
               "420_522",   # Aves. Hackett et al. 2008. Science
            ]

studytreelistTF = [True] * len(studytreelist)

if __name__ == "__main__":
	import load_synth_extract
	from stephen_desktop_conf import *

	synthottolid="81461"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)

