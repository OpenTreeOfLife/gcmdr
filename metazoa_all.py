"""
these are the studies identified by Chris, plus others from JWB
"""

"""
*** problems ***
"2333_4915" # from Chris. Junk. Everything mapped to the same genus "Serdia".

"1346_2678", # Mollusca. Kocot et al. 2011. Nature
- Error: Exception in thread "main" java.lang.IllegalStateException: this child is mapped the same graph node (Node[3573188]) as its parent [Ilyanassa obsoleta, Crepidula fornicata]

"1345_6256" # *** Dactylanthus antarcticus is mapping to Ptychodactiaria instead of Actiniaria. OTT problem

"1785_6248" # Leptomedusae. Leclere et al. 2009. Syst. Biol. *** SLeptomedusae and Leptothecatae are synonymns, but are split in the taxonomy.




"""


"""
*** good, but minor problems with taxonomy. check these ***

"2707_6281", # Icteridae. Powell et al. 2013. MPE *** Hypopyrrhus not mapped to Icteridae
"2702_6274", # core Corvoidea. Aggerbeck et al. 2014. MPE *** mapping back to Passeroidea
"2332_4912" # Sylvia. Voelker and Light. 2011. BMC Evol. Biol. *** Pseudoalcippe should be in the family Silviidae rather than Timaliidae



"2696_6249", # Demospongiae. Hill et al. 2013. PLoS ONE *** Ingroup is currently set to Porifera rather than Demospongiae


"1337_6167", # Holometabola (insect). Wiegmann et al. 2009. BMC Evol. Biol. *** mapping to Endopterygota
"1217_2455", # Metazoa. Delsuc et al. 2008. Genesis *** mapping to Eumetazoa
"1366_6166", # Annelida. Struck et al. 2011. Nature *** mapping to Lophotrochozoa
"2418_6152", # Metazoa. Evans and Cartwright. 2010. MBE *** mapping to Holozoa
"2672_6218", # Gnathostomata. Zhu et al. 2013. Nature *** mapping to Bilateria

"""


"""
*** vetted (JWB) ***

"2577_5980", # Galliformes. Wang et al. 2013. PLoS ONE
"2658_6192", # Trochilidae. McGuire et al. 2007. Syst. Biol.
"1966_4019", # Maluridae. Lee et al. 2011. Syst. Biol.
"2600_6022", # Paridae. Johansson et al. 2013. MPE
"2599_6021", # Alaudidae (larks). Alstrom et al. 2013. MPE
"2591_6008", # Parulidae (warblers). Lovette et al. 2008. MPE
"2454_5247", # Thamnophilus. Brumfield and Edwards. 2007. Evolution
"2692_6245", # Fringillidae. Zuccon et al. 2012. MPE
"2575_5974", # Passeriformes. Barker et al. 2013. Syst. Biol.
"2015_4152", # Passeriformes. Odeen et al. 2011. Evolution
"420_522",   # Aves. Hackett et al. 2008. Science
"2695_6250", # Ursidae. Krause et al. 2008. BMC Evol. Biol.
"1600_3231", # Euarchontoglires (Primates). Perelman et al. 2011. PloS Genetics
"2656_6185", # Primates. Springer et al. 2012. PLoS ONE
"2688_6240", # Rodentia. Fabre et al. 2012. BMC Evol. Biol.
"2359_4962", # Antilopinae. Barmann et al. 2013. MPE
"2687_6239", # Phocidae. Fulton and Strobeck. 2009. Proc. Roy. Soc.
"2691_6244", # Procyonidae. Koepfli et al. 2007. MPE
"2685_6235", # Mustelidae. Koepfli et al. 2008. BMC Evol. Biol.
"1634_3303", # Chiroptera. Agnarsson et  al. 2011. PLoS Currents Tree of Life
"1927_6215", # Cetacea. Steeman et al. 2009. Syst. Biol.
"1981_4052", # Felidae. Johnson et al. 2006. Science
"2684_6229", # Hyaenidae. Koepfli et al. 2006. MPE
"1797_3635", # Tenrecidae. Poux et al. 2008. BMC Evol. Biol.
"1428_2855", # Mammals. Meredith et al. 2011. Science
"1646_6231", # Caniformia (Pinnipeds). Higdon et al. 2007. BMC Evol. Biol.
"2589_6001", # Gobioidei. Agorreta et al. 2013. MPE
"2655_6181", # Cichlidae. Friedman et al. 2013. Proc. Roy. Soc.
"2657_6191", # Percomorpha. Near et al. 2012. MPE
"2653_6178", # Percomorpha. Miya et al. 2013. PLoS ONE
"1997_6183", # Percidae. Near et al. 2011. Syst. Biol.
"2551_6180", # Holacanthopterygii. Wainwright et al. 2012. Syst. Biol.
"2654_6179", # Leiognathidae. Chakrabarty et al. 2011. Mol. Ecol.
"2585_5994", # Tetraodontiformes. Santini et al. 2013. MPE
"2576_5975", # Euteleostei. Near et al. 2013. PNAS
"1870_3769", # Cyprinidae. Ruber et al. 2007. BMC Evol. Biol.
"2659_6195", # Otophysi. Chen et al. 2013. Evolution
"2415_5096", # Turtles. Guillon et al. 2012. Contributions to Zoology
"423_2857",  # Amphibia. Pyron and Weins. 2011. MPE
"2573_5959", # Sauria. Crawford et al. 2012. Biology Letters
"2460_5285", # Squamata. Pyron et al. 2013. BMC Evol. Biol.
"1988_4074", # Mantodea. Svenson et al. 2009. CLadistics
"2593_6247", # Dermaptera. Kocarek et al. 2013. PLoS ONE
"1563_6170", # Hymenoptera. Sharkey et al. 2011. Cladistics
"1849_3731", # Formicidae. Brady et al. 2006. PNAS
"1776_3581", # Ditrysia. Cho et al. 2011. Syst. Biol.
"2629_6162", # Hexapoda. Letsch and Simon. 2013. Syst. Ent.
"2604_6043", # Apoidea. Hedtke et al. 2013. BMC Evol. Biol.
"2686_6238", # Arthropoda. Lee et al. 2013. Curr. Biol.
"421_523",   # Mollusca. Smith et al. 2011. Nature
"1482_5228", # Eumetazoa. Evans et al. 2008. BMC Evol. Biol.
"1761_6151", # Scleractinia (corals). Huang nad Roy. 2013. Ecology and Evolution
"2407_6390", # Bilateria. Anderson et al. 2004. JME
"2647_6169", # Plancentalia. O'Leary et al. 2013. Science
"435_5995",  # Neornithes. Brown et al. 2008. BMC Biol.
"2651_6177", # Actinopterygii (Bony fishes). Betancur-R et al. 2013. PLoS Currents
"2664_6201", # Ditrysia. Regier et al. 2013. PLoS ONE
"2710_6291", # Metazoa. Ryan et al. 2013. Science
"2711_6295", # Henophidia. Reynolds et al. 2014. MPE
"2796_6491", # Pipridae. Ohlson et al. 2013. MPE
"2797_6493", # Neoaves. McCormack et al. 2013. PLoS ONE
"2797_6493", # Neoaves. McCormack et al. 2013. PLoS ONE
"2798_6497", # Spheniscidae. Subramanian et al. 2013. Biol. Lett.
"1979_6300", # Psittacidae. Tavares et al. 2006. Syst. Biol.
"2583_5989", # Galloanserae. Eo et al. 2009. Zool. Scripta.
"2799_6500", # Aves. Chojnowski et al. 2008. Gene
"2419_6023", # Neognathae. Thuiller et al. 2011. Nature
"2058_4241", # Crocodylia. Harshman et al. 2003. Syst. Biol.
"2800_6502", # Paleognathae. Harshman et al. 2008. PNAS
"2801_6503", # Galliformes. Cox et al. 2007. Auk
"2802_6506", # Galliformes. Kimball and Braun. 2008. J. Avian Biol.
"2803_6508", # Galliformes. Bonilla et al. 2010. MPE
"2804_6511", # Galliformes. Kimball et al. 2011. Int. J. Evol. Biol.
"2805_6512", # Psittaciformes. Wright et al. 2008. MBE
"2809_6521", # Marmota. Steppan and Akhverdyan. 1999. Syst. Biol.
"2023_6523", # Sciurognathi. Herron et al. 2004. MPE
"1812_3667", # Sciuridae. Steppan et al. 2004. MPE
"2087_4323", # Austrogoniodes. Banks and Paterson. 2004. Invert. Syst.
"2616_6485", # Neoaves. Gibb et al. 2013. MPE
"2444_6526", # Columbiformes. Pereira et al. 2007. Syst. Biol.
"2811_6533", # Vespinae. Lopez-Osorio et al. 2014. MPE
"2806_6529", # Psittaciformes. Joseph et al. 2011. MPE
"437_6242",  # Diptera. Wiegmann et al. 2011. PNAS
"1786_6257", # Hydrozoa. Cartwright et al. 2008. J. Marine Biol. Assoc. UK
"2678_6224", # Echinodermata. Janies et al. 2011. Syst. Biol.
"2587_5998", # Cetacea. McGowen et al. 2009. MPE
"2581_5987", # Membracidae. Cryan et al. 2004. Syst. Ent.
"2087_4323", # Austrogoniodes. Banks and Paterson. 2004. Invert. Syst.
"1788_6534", # Siphonophora. Dunn et al. 2005. Syst. Biol.
"1343_6255", # Hexactinella. Dohrmann et al. 2009. MPE
"1980_6254", # Calcarea. Dohrmann et al. 2006. MPE
"1338_2666", # Pterygota. Simon et al. 2009. MBE
"2374_6380", # Batrachuperus. Lu et al. 2012. Mol. Ecol.
"2335_6536", # Oplurus. Chan et al. 2012. Mol. Ecol.
"2456_5267", # Carnivora. Bininda-Emonds et al. 1999. Biol. Rev.
"2371_4985", # Scolopacidae. Corl and Ellegren. 2013. MPE
"2350_4948", # Galaxiella. Unmack et al. 2012. PLoS ONE
"2330_6378", # Brachymeles. Siler and Brown. 2011. Evolution
"2322_6376", # Grania. Wit et al. 2011. Zool. Scripta
"2324_6377", # Pteropus. Chan et al. 2011. PLoS Current Tree of Life
"2326_4904", # Brachymeles. Siler et al. 2011. MPE
"2329_4907", # Lepus. Melo-Ferreira et al. 2011. Syst. Biol.
"2353_4952", # Satanoperca. Willis et al. 2012. MPE










"""

"""
*** Possible for synthesis ***


"2323_6537", # Bombyliidae. Lambkin and Bartlett. 2011. ZooKeys <- check sampling
"2357_6538", # Evaniscus. Mullins et al. 2012. ZooKeys <- 2 new species are not in OTT

"""


"""
*** Chris Owen studies. Need to check each one of these for problems. ***


"2358_4960",
"2360_4963",
"2373_6379",
"2376_4993",
"2384_6381",
"2387_6382",
"2396_6383",
"2399_5042",
"2401_6387",
"2404_6388",
"2405_5070",
"2406_6389",
"2407_6390",
"2408_6391",
"2409_6401",
"2411_6402",
"2412_6403",
"2417_5098",
"2418_6152",
"2419_6023",
"2421_5109",
"2422_5117",
"2423_5119",
"2426_5122",
"2428_5137",
"2437_5173",
"2445_5215",
"2446_5220",
"2447_6406",
"2451_6407",
"2453_5240",
"2454_5247",
"2455_6408",
"2457_6416",
"2458_6436",
"2459_6437",
"2461_5286",
"2506_5398",
"2514_6439",
"2516_6440",
"2524_6441",
"2528_5446",
"2535_5460",
"2543_5481",
"2544_6482",
"2545_5489",
"2547_6483",
"2550_5513",
"2551_6180",
"2578_5982",
"2579_5983",
"2580_5986",
"2586_5996",
"2588_6484",
"2593_6247",
"2595_6015",
"2604_6043",
"2614_6121",
"2619_6131",
"2628_6143",
"2667_6209",
"2156_5953",
"2143_4505",
"2145_5952",
"2149_6486",
"2150_4541",
"2136_4477",
"2114_4379",
"2092_4335",
"2098_6487",
"2067_4258",
"2068_6488",
"2061_4246",
"2063_4251",
"1985_4069",
"1986_6489",
"1990_4076",
"2579_5984"

"1252_2661", # maps to: Anomura
"1336_2660", # maps to: Brachyura
"1948_6513", # maps to: Anomura
"1796_6514", # maps to: Typhlatya
"2243_6515", # maps to: Paramunida
"2670_6214", # maps to: Atyidae
"2671_6216", # maps to: Caridina
"2673_6219", # maps to: Astacidea
"2674_6220", # maps to: Cambaridae
"2675_6221", # maps to: Cambaridae
"2676_6222", # maps to: Scyllaridae
"2677_6223", # maps to: Anomura
"2682_6227", # maps to: Decapoda
"2683_6228", # maps to: Dendrobranchiata
"2807_6519", # maps to: Alpheidae
"2808_6522", # maps to: Alpheoidea
"2667_6211", # maps to: Galatheoidea

"""

studytreelist=[








            ]
