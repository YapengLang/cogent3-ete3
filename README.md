[![Coverage Status](https://coveralls.io/repos/github/YapengLang/cogent3-ete3/badge.svg?branch=main)](https://coveralls.io/github/YapengLang/cogent3-ete3?branch=main)

# A plugin for converting a [cogent3](https://cogent3.org/) tree to [ete3](http://etetoolkit.org/) tree object 

Developed an app that takes a cogent3 `PhyloNode` then returns an ete3 `PhyloTree`, plus an app for edge colouring.

## cogent3 to ete3 tree
```
from cogent3 import load_tree, get_app
from cogent3_ete3.style import show_legend

tree = load_tree("data/tree_large_scale.newick")

conv = get_app("cogent3_to_ete3")
t = conv(tree)
```
`t` is an ete3 `PhyloTree`.

## colour edges by a mapping
The `ete3_colour_edge` app allows you to colour information on selected edges. The app applies a colour to named edges. This means for colouring internal edges the node must have names.

```
edge_to_cat = {"Vombatidae_Vombatus_ursinus": "A",
 "Dasyuridae_Sarcophilus_harrisii": "B",
 "Peramelidae_Echymipera_kalubu" : "C",
 "Pseudochiridae_Pseudochirulus_forbesi": "D"}

cat_to_colour={"A":"blue", 
 "B":"blue", 
 "C":"red", 
 "D":"orange"}

cl = get_app("ete3_colour_edge", edge_to_cat=edge_to_cat, cat_to_colour=cat_to_colour)
t = cl(t)
```

You can use the convenient function to show a legend.

```
show_legend(t, cat_to_colour, legend_title="Your Category")
```

In the pop-up window, you can explore further and render the tree in a file as you progress:

![Tree Plot](data/coloured_tree.png)
