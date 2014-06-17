"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""
import general_tm_utils
import load_synth_extract


studytreelist=[
               "pg_244_3855",  # Gnetum, generic level. Won and Renner. 2006. Syst. Biol.
               "pg_2879_6674", # Almost all Bryophyta genera. Cox et al. 2010. Phytotaxa
               "pg_2878_6673", # Lepechinia; generic level. Drew et al. 2013. Bot. J. Linn. Soc.
               "pg_412_2166",  # Coniferophyta; 492 taxa; almost all genera monophyletic. Leslie et al. 2012. PNAS
               "pg_2827_6577",#Ilex NEW
               "pg_1022_1967",#Pontederiaceae
               #"194_2284",#early and nymphaeles
               "pg_562_817", #Poales
               "pg_424_532", #Lonicera
               "pg_1916_3902", #Brassicaceae
               "pg_588_878", #Asparagales
#              "pg_826_1584", #rosaceae #this is actually a fungal tree
               "pg_926_1825",#rosaceae
               "pg_1133_5647", #Rosales
               "pg_2624_6139", #Veronica
               "pg_2128_4437",#Plantago
               "pg_1102_2177",#Collinsia
               "pg_625_1016", #   Hoheria
               "pg_761_1415", #   Drosera
               "pg_2048_4220", #  allium
               "pg_1264_2544",#isoetes
               "pg_1129_2251", #  Solanum
               "pg_1842_3724", #  Oxalis
               "pg_288_5028", #   Croton
               "pg_754_1392", #   Ribes
               "pg_1137_2295", #  Erythronium
               "pg_1109_2201", #  Castilleja
               "pg_2004_4118",#cyrtandra
               "pg_385_458", #    Begonia
               "pg_1843_3725", #  Euphorbia
               "pg_1858_3754", #  Euphorbia
               "pg_330_325", #    Santalum
               "pg_394_483", #   Cucumis
               "pg_56_5821", #  Tsuga
               "pg_53_1280", #  Euryops
               "pg_62_2878", #  Lymania
               "pg_77_5878", #  Anaxagorea
               "pg_2841_6597", #    Sparganium
               "pg_1118_2226", #Mentheae,lamiaceae
               "pg_2669_6213", #Lamiaceae
##               "pg_19_6175", #Verbenaceae
               "pg_2032_5922",#Ruella
               "pg_1901_3877",#Lentibulariaceae
               "pg_713_1287", #Lamiales
               "pg_1131_2265", #Saxifragaceae
               "pg_2608_6288", #saxifrigales
               "pg_2539_6294",#Soltis et al. 2011 ML tree
 #             "pg_2539_5465",#Soltis et al. 2011 bootstrap
 	       "pg_2820_6566",#Streptophyta
               "pg_2712_6296", #Rosids
               "pg_259_142", #Cercis FABALES!
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
               #"265_153", #Fabales FABALES!
               #"998_2313", #Fabales
               "pg_2661_6198", #Ericales
               "pg_2645_6165",#Menispermaceae
               "pg_2644_6164",#Ranunculales
               "pg_2610_6117", #malpighiales tree, the best one we have right now, we think6
               "pg_2642_6161",#Cayophyllales; not sure if you have a better study here)
               "pg_2052_4228",#Lundia
               "pg_1103_2178",#Bignonieae
               "pg_14_12", #Bignoniaceae
               "pg_2140_4483",#Annonaceae
               "pg_2648_6171",#Marchantiales
               "pg_650_1147",#Meliaceae, Sapindales
               "pg_2085_4317",#Araceae
               "pg_2044_4212",#Orobanchaceae
               "pg_2626_6142",#Amaranthaceae
               "pg_2598_6020",#Boraginaceae
               "pg_2564_5699",#Polystichum
               "pg_2042_4202",#Bartramiaceae
##               "pg_2034_4191",#Ruellieae
               "pg_2000_4098",#Coffea
               "pg_20_2162",#Gallium
               "pg_1101_2172",#Rubieae
               "pg_2565_5708",#Ericoideae
               "pg_1094_2138",#Apocynaceae
               "pg_2641_6160",#Rubiaceae
               "pg_99_5885",#Barnadesioideae
               "pg_275_167",#Celastraceae
               "pg_93_1411",#Symplocos
               "pg_30_2281",#Illicium
               #"36_36",#Dendropanax NOT ROOTED AND PROBABLY NOT GREAT
               "pg_898_1732",#Schefflera
               "pg_216_5865",#Hedera
               "pg_901_1740",#Meryta
               "pg_2830_6583",#brassaiopsis
               "pg_2831_6584",#Escallonia
               "pg_719_1296",#Nymphoides
               "pg_1975_4041",#Tragopogon
               "pg_1821_3678",#Helichrysum
               "pg_1583_3194",#Gaillardia
               "pg_1581_3188",#Dubautia
               "pg_1575_3164",#Tolpis
               "pg_332_333", #    Polygonaceae
               "pg_1573_3144",#Onoseris
               "pg_934_1832",#Echinops
               "pg_200_6585",#Encelia
               "pg_152_5743",#Coreopsis
               "pg_53_1281",#Euryops
               "pg_2076_4282",#Garrya 
               "pg_2832_6586",#Sedum    
               "pg_37_5871",#Rhus 
               "pg_50_1397",#Anagallis 
               "pg_1866_3765",#Thesium (Santalaceae)
               "pg_59_5731",#Aristolochiaceae
               "pg_73_5787",#Passiflora
               "pg_80_5881",#Rhododendron
               "pg_81_5863",#Pinus
               "pg_82_5792",#Campanula
               "pg_88_5848",#Erodium
               #"231_5505", #caryoph SOME SORT OF LOADING PROBLEM
               "pg_180_794",#Araceae
               #"574_840",#Asparagales upload problems
               "pg_576_849",#Alocasia (Araceae)
               "pg_581_859",#Crocus (Iridaceae)
               "pg_582_862",#Mermuellera (Poaceae)
               "pg_598_926",#Poeae (Poaceae)
               "pg_599_927",#Costaceae
               "pg_603_940",#Maxillaria (orchidaceae)
               "pg_704_1266",#Molluginaceae
               "pg_721_1298",#Commelinaceae
               "pg_723_1300",#Triticum
               #"724_3212",#Pleurothallidinae (Orchidaceae) upload problems
               "pg_921_4103",#Oryzeae (Poaceae)
               "pg_1446_2921",#Hymenophyllum (Hymenophyllaceae)
               #"1302_2616", make for weird euphyllophyta
               "pg_1962_6580",#Viburnum Clement and Donoghue 2011
               "pg_915_1802",#Viburnum
               "pg_915_1803",#Valerianaceae
               "pg_2625_6140",#Utricularia
               "pg_1130_2258",#Nicotiana
               "pg_2047_4217",#Cuscuta
               "pg_386_459",#Brunsfelisia
               "pg_139_5860",#Nierembergia
               "pg_126_2233",#Solanum
               "pg_136_5857",#cestrum               
               "pg_9_1",#Campanulidae
               "pg_2828_6578",#caprifolieae Smith 2009 NEW
               "pg_142_38",#Asclepias
               "pg_2638_6157",#Santalales
               "pg_21_37",#Solanaceae
               "pg_72_801",#Malpighiaceae
               "pg_75_1743",#Apioideae
               "pg_1974_4038",#PolygonaceaeS
               "pg_1974_4039",#Rheum
               #"535_768",#Eriogonoideae
               "pg_61_816",#Bromeliaceae
##               "pg_284_185",#Cucurbitaceae
               #"1086_2111",#Cactaceae
               "pg_41_1396",#Feddea
               "pg_283_184",#Celastrales
               #"1116_2217",#Lamiales (Oxelman 2005)
               "pg_225_5991",#deep plants
               "pg_1867_3766", #cycads
               "pg_1278_2572",#Liverworts
               "pg_1268_2560",#hornworts
               "pg_412_2166",#conifers
               "pg_787_1489", #   Ephedra
               "pg_2046_5928" #Trebouxiophyceae, Chlorophyta
               ]
studytreelistTF = [True] * len(studytreelist)

if __name__ == "__main__":
    from stephen_desktop_conf import *
    synthottolid="10218"

    print "loading synthottolid:",synthottolid
    print "loading studytreelist:",studytreelist
    
    download = True
    if download:
        general_tm_utils.get_all_studies_opentreeapi(studytreelist,studyloc)    

    load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,
				 treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)

