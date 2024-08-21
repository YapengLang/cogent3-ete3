# A plugin for converting a [cogent3](https://github.com/cogent3/cogent3) tree to ete3 tree object 

Developed an app that takes a cogent3 `PhyloNode` then returns an ete3 `PhyloTree`, plus an app for edge colouring.

## cogent3 to ete3 tree
```
from cogent3 import load_tree, get_app
from cogent3_ete3.style import show_legend

tree = load_tree("data/tree_large_scale.newick")

conv = get_app("cogent3_to_ete3")
t = conv(tree)
```

## colour edges by a mapping
```
edge_to_cat = {"Vombatidae_Vombatus_ursinus": "limit",
 "Dasyuridae_Sarcophilus_harrisii": "sympathetic",
 "Peramelidae_Echymipera_kalubu" : "chainsaw",
 "Pseudochiridae_Pseudochirulus_forbesi": "identity"}

cat_to_colour={"limit":"blue", 
 "sympathetic":"blue", 
 "chainsaw":"red", 
 "identity":"yellow"}

cl = get_app("ete3_colour_edge", edge_to_cat=mcats, cat_to_colour=cat_to_colour)
t = cl(t)
```

user can add legend of matrix categories to the plot

```
show_legend(t, cat_to_colour, legend_title="Matrix Category")
```

will get:

![Tree Plot](data/coloured_tree.png)
