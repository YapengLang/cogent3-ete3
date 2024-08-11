# C3 plugin of converting to ete3 tree object

Develop an app that takes a cogent3 tree object and returns an ete3 "object"

## from cogent3 to ete3 tree
```
from ete3_plugin import trs_tree, extension
from cogent3 import load_tree

tree = load_tree("data/tree_large_scale.newick")

trs = trs_tree.cogent3_to_ete3()
t = trs(tree)
```

## colour edges by a mapping
```
mcats = {"Vombatidae_Vombatus_ursinus": "limit",
 "Dasyuridae_Sarcophilus_harrisii": "sympathetic",
 "Peramelidae_Echymipera_kalubu" : "chainsaw",
 "Pseudochiridae_Pseudochirulus_forbesi": "identity"}

cl = extension.colour_edge(mcats)
cl(t)
```

user can add legend of matrix categories to the plot

```
cl.add_legend(t)
```

![Tree Plot](data/coloured_tree.pdf)
