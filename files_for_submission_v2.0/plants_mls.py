"""
this is the stuff specific to the plant studies that are loaded. It can include comments and all that. The studytreelist will be read from the load_synth_extract file. Other variables in the conf could be overridden here. 
"""
import general_tm_utils
import load_synth_extract


studytreelist=[
               
               ### core eudicots
               "pg_2827_6577",#Ilex NEW
               "pg_761_1415", #   Drosera
               "pg_77_5878", #  Anaxagorea
               "pg_754_1392", #   Ribes               
               "pg_330_325", #    Santalum
               "pg_1131_2265", #Saxifragaceae
               "pg_2608_6288", #saxifrigales
               "pg_2539_6294",#Soltis et al. 2011 ML tree
               "pg_2645_6165",#Menispermaceae
               "pg_2644_6164",#Ranunculales
               "pg_2642_6161",#Cayophyllales; not sure if you have a better study here)
               #"pg_84_1014",#Pereskia,Cactaceae
               "pg_2140_4483",#Annonaceae
               "pg_2626_6142",#Amaranthaceae
               "pg_30_2281",#Illicium
               "pg_332_333", #    Polygonaceae
               "pg_2832_6586",#Sedum    
               "pg_1866_3765",#Thesium (Santalaceae)
               "pg_59_5731",#Aristolochiaceae
               "pg_704_1266",#Molluginaceae
               "pg_2638_6157",#Santalales
               "pg_1974_4038",#PolygonaceaeS
               "pg_1974_4039",#Rheum
               "pg_2901_6721",#Thalictrum
               "pg_2906_6730",#Aquilegia                                
               "pg_2165_4564", # Dryopteris
               "pg_1524_3046", # Rhipsalideae; 4 Cactus genera, all monophyletic...
               "pg_1443_2917", # Peperomia


               ### monocots
               #"pg_1414_2837", # Satyrium
               #"pg_1411_5110", # Galeandra
               #"pg_1409_2822", # 2 monophyletic orchid genera
               #"pg_1408_2821", # Hexalectris
               #"pg_1407_2818", # Pleione
               #"pg_1401_2812", # Dactylorhiza
               #"pg_1391_2795", # Dioscorea
               #"pg_1434_2876", # Puya
               #"pg_2633_6153", # Narcissus
               #"pg_1539_3088", # Carex
               #"pg_2634_6154",#galanthus
               #"pg_1022_1967",#Pontederiaceae
               #"pg_562_817", #Poales
               #"pg_588_878", #Asparagales
               #"pg_2048_4220", #  allium
               #"pg_1137_2295", #  Erythronium
               #"pg_62_2878", #  Lymania
               #"pg_2841_6597", #    Sparganium
               #"pg_2085_4317",#Araceae
               #"pg_180_794",#Araceae
               #"pg_576_849",#Alocasia (Araceae)
               #"pg_581_859",#Crocus (Iridaceae)
               #"pg_582_862",#Mermuellera (Poaceae)
               #"pg_598_926",#Poeae (Poaceae)
               #"pg_599_927",#Costaceae
               #"pg_603_940",#Maxillaria (orchidaceae)
               #"pg_721_1298",#Commelinaceae
               #"pg_723_1300",#Triticum
               #"pg_921_4103",#Oryzeae (Poaceae)
               #"pg_61_816",#Bromeliaceae
               #"pg_573_839", # Aponogeton
               #"pg_566_832", # Orchidantha

               
               ### asterids
               "pg_1522_3044", # Columnea 
               "pg_1570_3142", # Eupatorium
               "pg_1583_3194", # Gaillardia
               "pg_1572_3145", # Metalasia
               "pg_2909_6735",#exochaenium
               "pg_43_3862",#hoya
               "pg_38_1750",#heliotropium
               "pg_2878_6673", # Lepechinia; generic level. Drew et al. 2013. Bot. J. Linn. Soc.
               "pg_2624_6139", #Veronica
               "pg_2128_4437",#Plantago
               "pg_1102_2177",#Collinsia
               "pg_1129_2251", #  Solanum
               "pg_1109_2201", #  Castilleja
               "pg_2004_4118",#cyrtandra
               "pg_53_1280", #  Euryops
               "pg_1118_2226", #Mentheae,lamiaceae
               "pg_2669_6213", #Lamiaceae
               "pg_2032_5922",#Ruella
               "pg_1901_3877",#Lentibulariaceae
               "pg_713_1287", #Lamiales
               "pg_2912_6740",	# Calliandra
               ##fabales MLS
               #"pg_259_142", #Cercis FABALES!
               #"pg_264_150", #Coursetia FABALES!
               #"pg_267_161", #Ateleia (Swartzieae-Leguminosae) FABALES!
               #"pg_2077_4291", #Podalyria (Fabaceae, Podalyrieae) FABALES!
               #"pg_293_201", #Mimosa FABALES!
               #"pg_197_784", #Phaseolus FABALES!
               #"pg_595_896", #Senna FABALES!
               #"pg_131_6236", #Trifolium FABALES!
               #"pg_2689_6241", #Lupinus FABALES!
               #"pg_597_906", #Machaerium (Leguminosae) FABALES!
               #"pg_2001_4100", #Astragalus FABALES!
               #"pg_606_5290", #Trifolieae and Vicieae FABALES!
               #"pg_270_159", #Indigofereae FABALES!
               #"pg_596_901", #Genisteae (Leguminosae) FABALES!
               #"pg_294_202", #Detarieae (Caesalpinioideae) FABALES!
               #"pg_292_199", #(Diocleinae: Papilionoideae) FABALES!
               #"pg_58_775", #Crotalarieae (Fabaceae) FABALES!
               #"pg_548_798", #Vigna FABALES!
               #"pg_2055_4234",  #Genistoid legumes FABALES!
               #"pg_2057_4240", #papilionoid FABALES!
               #"pg_2127_4426", #Papilionoideae; Vataireoid Clade FABALES!
               #"pg_594_890", #robinioid legumes FABALES!
               #"pg_261_145", #Caesalpinieae FABALES!
               #"pg_57_777", #Podalyrieae (Fabaceae) FABALES!
               #"pg_1087_2114", #phaseoloid FABALES!
               #"pg_1087_2115", #phaseoloid FABALES!
               #"pg_2690_6243", #Fabaceae FABALES!
               #"pg_2045_4213", #Acacia FABALES!
               #"pg_605_947", #Strophostyles (Fabaceae) FABALES!
               #"pg_271_5017", #Polygalaceae FABALES!
               "pg_2661_6198", #Ericales
               "pg_2052_4228",#Lundia
               "pg_1103_2178",#Bignonieae
               "pg_14_12", #Bignoniaceae
               "pg_2598_6020",#Boraginaceae
               "pg_2000_4098",#Coffea
               "pg_20_2162",#Gallium
               "pg_1101_2172",#Rubieae
               "pg_2565_5708",#Ericoideae
               "pg_1094_2138",#Apocynaceae
               "pg_2641_6160",#Rubiaceae
               "pg_99_5885",#Barnadesioideae
               "pg_93_1411",#Symplocos
               "pg_898_1732",#Schefflera
               "pg_216_5865",#Hedera
               "pg_901_1740",#Meryta
               "pg_2830_6583",#brassaiopsis
               "pg_2831_6584",#Escallonia
               "pg_719_1296",#Nymphoides
               "pg_1975_4041",#Tragopogon
               "pg_1821_3678",#Helichrysum
               "pg_1581_3188",#Dubautia
               "pg_1575_3164",#Tolpis
               "pg_1573_3144",#Onoseris
               "pg_934_1832",#Echinops
               "pg_200_6585",#Encelia
               "pg_152_5743",#Coreopsis
               "pg_53_1281",#Euryops
               "pg_2076_4282",#Garrya 
               "pg_50_1397",#Anagallis 
               "pg_80_5881",#Rhododendron
               "pg_424_532", #Lonicera
               "pg_82_5792",#Campanula
               "pg_1962_6580",#Viburnum Clement and Donoghue 2011
               "pg_915_1802",#Viburnum
               "pg_32_1775",#Valeriana
               "pg_915_1803",#Valerianaceae
               "pg_2625_6140",#Utricularia
               "pg_1130_2258",#Nicotiana
               "pg_2047_4217",#Cuscuta
               "pg_386_459",#Brunsfelisia
               "pg_139_5860",#Nierembergia
               "pg_126_2233",#Solanum
               "pg_136_5857",#cestrum               
               "pg_1944_3959",#Campanulidae
               "pg_2828_6578",#caprifolieae Smith 2009 NEW
               "pg_142_38",#Asclepias
               "pg_21_37",#Solanaceae
               "pg_75_1743",#Apioideae
               "pg_41_1396",#Feddea
               "pg_2044_4212",#Orobanchaceae

               ### rosids
               "pg_1916_3902", #Brassicaceae
               "pg_926_1825",#rosaceae
               "pg_1133_5647", #Rosales
               "pg_625_1016", #   Hoheria
               "pg_1842_3724", #  Oxalis
               "pg_288_5028", #   Croton
               "pg_385_458", #    Begonia
               "pg_1843_3725", #  Euphorbia
               "pg_1858_3754", #  Euphorbia
               "pg_394_483", #   Cucumis
               "pg_52_463",# Cucumis
               "pg_2712_6296", #Rosids
               "pg_2610_6117", #malpighiales tree, the best one we have right now, we think6
               "pg_650_1147",#Meliaceae, Sapindales
               "pg_275_167",#Celastraceae
               "pg_37_5871",#Rhus 
               "pg_73_5787",#Passiflora
               "pg_88_5848",#Erodium
               "pg_72_801",#Malpighiaceae
               "pg_283_184",#Celastrales
               
               ##deep plants
               "pg_2820_6566",#Streptophyta
               "pg_1483_2983", # Dioon
               "pg_1478_2974", # 3 genera from Polypodiaceae
               "pg_1474_2969", # Brown Algae; "dark" part of tree
               "pg_1473_2967", # Elaphoglossum
               "pg_1453_2932", #Isoetes
               "pg_1450_2926", # Huperzia
               "pg_1384_2766", # Gracilaria
               "pg_1382_2763", # Antithamnion
               "pg_1318_2634", # Polypodiaceae (family)
               "pg_1312_2628", # Asplenium

               "pg_1518_6333", # Parmelina
               "pg_2898_6713",#Osmolindsaea
               "pg_2896_6709", # Selaginellaceae
               "pg_1264_2544",#isoetes
               "pg_56_5821", #  Tsuga
               "pg_2648_6171",#Marchantiales
               "pg_2564_5699",#Polystichum
               "pg_81_5863",#Pinus
               "pg_1996_4089", # Lomariopsis
               "pg_1446_2921",#Hymenophyllum (Hymenophyllaceae)
               "pg_2039_4198", # Hymenophyllum
               "pg_2042_4202",#Bartramiaceae
               "pg_1942_3962", # Azolla
               "pg_1868_3767", # Marsilea
               "pg_1567_3137", # Equisetum
               "pg_244_3855",  # Gnetum, generic level. Won and Renner. 2006. Syst. Biol.
               "pg_2879_6674", # Almost all Bryophyta genera. Cox et al. 2010. Phytotaxa
               "pg_412_2166",  # Coniferophyta; 492 taxa; almost all genera monophyletic. Leslie et al. 2012. PNAS

               "pg_225_5991",#deep plants
               "pg_1867_3766", #cycads
               "pg_1278_2572",#Liverworts
               "pg_1268_2560",#hornworts
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
    """
    for i in studytreelist:
        tstudy_list = [i]
        generallogfileloc = "/home/smitty/TEMP/"+i+".log"
        ttfntreefn = "/home/smitty/TEMP/"+i+".tre"
        load_synth_extract.run_load_single_ttfn(dott,dload,studyloc,tstudy_list,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,ttfntreefn)
    """
    load_synth_extract.run(dott,dload,studyloc,studytreelist,javapre,treemloc,generallogfileloc,dsynth,synthottolid,treefn,studytreelistTF)

