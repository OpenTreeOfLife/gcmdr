"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""

import load_synth_extract

studytreelist=[
	
"264_150", #Coursetia
"261_145", #Caesalpinieae
"259_142", #Cercis
"268_4777", #Coursetia
"267_161", #Ateleia (Swartzieae-Leguminosae)
"271_5017", #Polygalaceae
"609_961", #Fabaceae
"293_201", #Mimosa
"292_199", #(Diocleinae: Papilionoideae)
"294_202", #Detarieae (Caesalpinioideae)
"548_798", #Vigna
"197_784", #Phaseolus
"595_896", #Senna
"596_901", #Genisteae (Leguminosae)
"597_906", #Machaerium (Leguminosae)
"265_153", #Fabales
"9_1",#Campanulidaex
"14_12",#Bignoniaceaex
"15_4",#Rosids
"19_6175",#Verbenaceae
"21_37",#Solanaceaex
"30_2281",#Illicium
"33_704",#PoaceaeBAD
"36_36",#Dendropanax
"37_5871",#Rhus
"41_1396",#Feddea (Asteraceae)
"48_1144",#Biebersteiniaceae (Sapindales)
"50_1397",#Anagallis
"54_949",#Fabidsx
"55_5864",#SterculioideaeBAD
"57_777",#Podalyrieaex
"58_775",#Crotalarieaex
"59_5731",#Aristolochiaceae
"61_816",#Bromeliaceaex
"71_997",#MalpighialesBAD
"72_801",#MalpighiaceaeBAD
"73_5787",#Passiflora
"75_1743",#Apioideaex
"80_5881",#Rhododendron
"81_5863",#Pinus
"82_5792",#Campanula
"88_5848",#Erodium
"93_1411",#Symplocos
"99_5885",#Barnadesioideae
"142_38",#Asclepiasx
"180_794",#Araceaex
"212_234",#Eleocharis
"218_5730",#Cerinthe (Boraginaceae)
"224_40",#AngiospermsBAD
"225_5499",#Land plantsBAD
"233_72",#Land plantsBAD
"266_154",#LeguminosaeBAD
"283_184",#Celastralesx
"284_185",#Cucurbitaceaex
"319_273",#BrassicaceaeBAD
"327_5187",#BrassicaceaeADD
"436_552",#MonocotyleBAD
"535_768",#Eriogonoideaex
"562_817",#Poalesx
"574_840",#Asparagalesx
"576_849",#Alocasia (Araceae)x
"581_859",#Crocus (Iridaceae)x
"582_862",#Mermuellera (Poaceae)x
"588_878",#Asparagalesx
"594_890",#robinioid legumes
"598_926",#Poeae (Poaceae)BAD
"599_927",#Costaceaex
"603_940",#Maxillaria (orchidaceae)BAD
"605_948",#Strophostyles (Fabaceae)
"608_5332",#Astragalus
"650_1147",#Cedrela (Meliaceae)
"704_1266",#MolluginaceaeBAD
"713_1284",#Lamialesx
"721_1298",#Commelinaceaex
"723_1300",#Triticumx
"724_3212",#Pleurothallidinae (Orchidaceae)x
"915_1802",#Viburnumx
"915_1803",#Valerianaceaex
"921_4103",#Oryzeae (Poaceae)x
"998_2313",#Fabales
"1086_2111",#Cactaceaex
"1101_2172",#Tribe Rubiae (Rubiaceae)
"1109_2201",#Castilleja
"1116_2217",#Lamiales (Oxelman 2005)x
"1118_2225",#Mentheae
"1278_2572",#Liverworts
"1282_2574",#Polytrichopsida (mosses)
"1285_2578",#pleurocarpous mosses 
"1300_2613",#Hymenophyllum (Hymenophyllaceae)x
"1302_2616",#Cyatheaceaex
"1351_2692",#Polytrichales (Bryophytes)
"1356_2697",#land plants
"1385_2770",#some algaex
"1842_3724",#Oxalis
"1902_3878",#Mimosoideae
"1916_3902",#Brassicaceaex
"2001_4100",# Astragalus
"2009_4140",#Lamioideae
"2025_5918",#PoaceaeBAD
"2027_4176",#Acanthaceae
"2034_4191",#Ruellieae (Acanthaceae)
"2042_4202",#Bartramiaceae (Bryopsida)
"2044_4212",#Orobanchaceae
"2045_4213",# Acacia
"2046_5928",#Trebouxiophyceae (Chlorophyta)
"2049_4223",#Geonoma (Arecaceae)
"2055_4234",#Genistoid legumes
"2057_4240",#papilionoid
"2085_4317",#Araceae
"2127_4426",#Papilionoideae; Vataireoid Clade
"2140_4483",#Miliuseae (Annonaceae)
"2539_5465",#Angiospermsx
"2546_5493",#Sapindaceaex
"2549_5512",#Land plantsBAD
"2564_5699",#Polystichum
"2565_5708",#Ericoideae (Ericaceae)
"2598_6020",#Boraginaceae
"2624_6139",#Veronica
"2626_6142",#Amaranthaceae
"2631_6148",#Caesalpinioideae
"2641_6160",#Rubiaceae
"2642_6161",#Caryophyllales
"2644_6164",#Ranunculales
"2645_6165",#Menispermaceae
"2648_6171",#Marchantiales
"2650_6174",#Lithospermum
               ]

if __name__ == "__main__":
	from stephen_desktop_conf import *

	synthottolid="10218"

	print "loading synthottolid:",synthottolid
	print "loading studytreelist:",studytreelist

	load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn)
