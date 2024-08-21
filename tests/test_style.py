from ete3 import PhyloTree

from cogent3_ete3.style import ete3_colour_edge


def test_ete3_colour_edge():
    tree = PhyloTree("data/test_tree.newick", format=5)
    edge_to_cat = {node.name: "cat1" for node in tree.traverse()}  # type: ignore
    cat_to_colour = {"cat1": "red"}
    colour_edge = ete3_colour_edge(edge_to_cat, cat_to_colour)
    coloured_tree = colour_edge(tree)
    assert all(
        node.img_style["hz_line_color"] == "red"
        for node in coloured_tree.traverse()
        # type: ignore
    )
