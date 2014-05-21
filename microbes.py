synthottolid="93302"

"""
full list
study 425 tree 5976
study 239 tree 111 and 112  
study 263 tree  149
study 2413 tree 5093 and 5094 
study 2397 tree 5038 and 5039  
study 2398 tree 5040
from Dail
2739	6325	Bettina E Schirrmeister, Alexandre Antonelli, Homayoun C Bagheri. 2011. The origin of multicellularity in cyanobacteria. BMC Evolutionary Biology 11(1):45
2552	6326,6327, 6328, 6329	Theriot E., Cannone J., Gutell R., & Alverson A. 2009. The limits of nuclear-encoded SSU rDNA for resolving the diatom phylogeny. European Journal of Phycology, 44(3): 277-290.
2448	5223	Nicola Segata, Daniela Bornigen, Xochitl C. Morgan, and Curtis Huttenhower. PhyloPhlAn is a new method for improved phylogenetic and taxonomic placement of microbes
UPDATE THE INGROUP 2425	5121	Fewer D., Friedl T., & Budel B. 2002. Chroococcidiopsis and heterocyst differentiating cyanobacteria are each other's closest living relatives. Molecular Phylogenetics and Evolution, 23(1): 82-90..
2542	5471, 5588, 5590	Jenna Morgan Lang, Aaron E. Darling, Jonathan A. Eisen. 2013. Phylogeny of Bacterial and Archaeal Genomes Using Conserved Genes: Supertrees and Supermatrices. PLoS ONE 8(4):e62510.

"""
## A possible alternative to Katz et al. 2012:
studytreelist=["263_149",
               "2713_6309",
               #"2413_5093",
               "2715_6308",
               "2739_6601",
               #"2737_6322",
               #"2738_6323",
               "2753_6360",
               "2742_6342",
               "2757_6369",
               #"2760_6375",#Exception in thread "main" java.lang.IllegalStateException: this child is mapped the same graph node (Node[3114879]) as its parent [Alexandrium tamarense]
               "2553_5579",
               "2556_5586",
               #"2484_5346",
               "312_264",
               #"313_6019",
               "313_6681", # fixed Grant et al. tree (topology)
               "2554_5580",
               "2484_6607",
               "2849_6615"
               ]#"2822_6569"] # Parfrey et al. 2011. PNAS <- why not this one? it is good.
studytreelistTF = [True] * len(studytreelist)
"""
studytreelist=["425_5976", # Eukaryota. Katz et al. 2012. Syst Biol.
"239_111",
"239_112",
"263_149",
"2413_5093",
"2413_5094",
"2397_5038",
"2397_5039",
"2398_5040",
"2739_6325",
"2552_6326",
"2552_6327",
"2552_6328",
"2552_6329",
#"2448_5223",
"2425_5121",
"2542_5471",
"2542_5588",
"2542_5590"]
"""
if __name__ == "__main__":
	import load_synth_extract
	from stephen_laptop_conf import *

	synthottolid="93302"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)
