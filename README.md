gcmdr
=====

Graph of Life Commander

This repo contains scripts for loading trees into treemachine, as well as lists of studies currently being incorporated into the synthetic tree. 

Files
-----

Files with taxon names (fungi.py, birds.py, etc) contain study lists for import. Studies listed in """…""" comments are those that have been requested for synthesis but have not yet passed all of the import checks.

* collect\_input\_studies.py: prints a list of the json files that are currently being synthesized into the draft tree
* get\_name\_info.py: ultilty script to get information about a name from treemachine
* life.py: loads all of the studies into treemachine (imports other taxon_name.py files)
* tree\_utils.py: create consensus trees, calculate bipartitions, calculate distances

Tree identifiers
----------------

Within the lists found in the taxon files, trees (usually only one per study) are designated as "MMM_NNN" where MMM is the study id and NNN is the id of a tree within that study.
