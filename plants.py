"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""

import load_synth_extract

studytreelist=["1022_1967",#Pontederiaceae
               #"194_2284",#early and nymphaeles
               "562_817", #Poales
               "424_532", #Lonicera
               "1916_3902", #Brassicaceae
               "588_878", #Asparagales
#              "826_1584", #rosaceae #this is actually a fungal tree
               "926_1825",#rosaceae
               "1133_5647", #Rosales
               "2624_6139", #Veronica
               "1118_2226", #Mentheae,lamiaceae
               "2669_6213", #Lamiaceae
               "19_6175", #Verbenaceae
               "713_1287", #Lamiales
               "1131_2265", #Saxifragaceae
               "2608_6288", #saxifrigales
               "2539_6294",#Soltis et al. 2011 ML tree
 #             "2539_5465",#Soltis et al. 2011 bootstrap
               "2712_6296", #Rosids
               "259_142", #Cercis FABALES!
               "264_150", #Coursetia FABALES!
               "267_161", #Ateleia (Swartzieae-Leguminosae) FABALES!
               "2077_4291", #Podalyria (Fabaceae, Podalyrieae) FABALES!
               "293_201", #Mimosa FABALES!
               "197_784", #Phaseolus FABALES!
               "595_896", #Senna FABALES!
               "131_6236", #Trifolium FABALES!
               "2689_6241", #Lupinus FABALES!
               "597_906", #Machaerium (Leguminosae) FABALES!
               "2001_4100", #Astragalus FABALES!
               "606_5290", #Trifolieae and Vicieae FABALES!
               "54_949", #Indigofereae FABALES!
               "596_901", #Genisteae (Leguminosae) FABALES!
               "294_202", #Detarieae (Caesalpinioideae) FABALES!
               "292_199", #(Diocleinae: Papilionoideae) FABALES!
	       "58_775", #Crotalarieae (Fabaceae) FABALES!
               "548_798", #Vigna FABALES!
               "2055_4234",  #Genistoid legumes FABALES!
               "2057_4240", #papilionoid FABALES!
               "2127_4426", #Papilionoideae; Vataireoid Clade FABALES!
               "594_890", #robinioid legumes FABALES!
               "261_145", #Caesalpinieae FABALES!
               "57_777", #Podalyrieae (Fabaceae) FABALES!
               "78_6237", #phaseoloid FABALES!
               "78_5858", #phaseoloid FABALES!
               "2690_6243", #Fabaceae FABALES!
               "2045_4213", #Acacia FABALES!
               "605_947", #Strophostyles (Fabaceae) FABALES!
               "271_5017", #Polygalaceae FABALES!
               "265_153", #Fabales FABALES!
               #"998_2313", #Fabales
               "2661_6198", #Ericales
               "2645_6165",#Menispermaceae
               "2644_6164",#Ranunculales
               "2610_6117", #malpighiales tree, the best one we have right now, we think6
               "2642_6161",#Cayophyllales; not sure if you have a better study here)
               "14_12", #Bignoniaceae
               "2140_4483",#Annonaceae
               "2648_6171",#Marchantiales
               "650_1147",#Meliaceae, Sapindales
               "2085_4317",#Araceae
               "2044_4212",#Orobanchaceae
               "2626_6142",#Amaranthaceae
               "2598_6020",#Boraginaceae
               "2564_5699",#Polystichum
               "2042_4202",#Bartramiaceae
               "2034_4191",#Ruellieae
               "1101_2172",#Rubieae
               "2565_5708",#Ericoideae
               "2641_6160",#Rubiaceae
               "99_5885",#Barnadesioideae
               "275_167",#Celastraceae
               "93_1411",#Symplocos
               "30_2281",#Illicium
               "36_36",#Dendropanax
               "37_5871",#Rhus 
               "41_1396",#Feddea
               "50_1397",#Anagallis 
               "1866_3765",#Thesium (Santalaceae)
               "59_5731",#Aristolochiaceae
               "73_5787",#Passiflora
               "80_5881",#Rhododendron
               "81_5863",#Pinus
               "82_5792",#Campanula
               "88_5848",#Erodium
               #"231_5505", #caryoph SOME SORT OF LOADING PROBLEM
               "180_794",#Araceae
               #"574_840",#Asparagales upload problems
               "576_849",#Alocasia (Araceae)
               "581_859",#Crocus (Iridaceae)
               "582_862",#Mermuellera (Poaceae)
               "598_926",#Poeae (Poaceae)
               "599_927",#Costaceae
               "603_940",#Maxillaria (orchidaceae)
               "704_1266",#Molluginaceae
               "721_1298",#Commelinaceae
               "723_1300",#Triticum
               #"724_3212",#Pleurothallidinae (Orchidaceae) upload problems
               "921_4103",#Oryzeae (Poaceae)
               "1300_2613",#Hymenophyllum (Hymenophyllaceae)
               #"1302_2616", make for weird euphyllophyta
               "915_1802",#Viburnum
               "915_1803",#Valerianaceae
               "1901_3877",#Lentibulariaceae
               "9_1",#Campanulidae
               "142_38",#Asclepias
               "21_37",#Solanaceae
               "72_801",#Malpighiaceae
               "75_1743",#Apioideae
               "535_768",#Eriogonoideae
               "61_816",#Bromeliaceae
               "284_185",#Cucurbitaceae
               "2546_5493",#Sapindaceae
               #"1086_2111",#Cactaceae
               "283_184",#Celastrales
               #"1116_2217",#Lamiales (Oxelman 2005)
               "225_5991",#deep plants
               "1867_3766", #cycads
               "1278_2572",#Liverworts
               "1268_2560",#hornworts
               "412_2166",#conifers
               "2046_5928" #Trebouxiophyceae, Chlorophyta
               ]

studytreelistTF = [True] * len(studytreelist)

if __name__ == "__main__":
	from stephen_desktop_conf import *

	synthottolid="10218"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)

