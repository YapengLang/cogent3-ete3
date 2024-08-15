from cogent3 import get_app, make_tree
from cogent3.app.composable import define_app
from cogent3.core.tree import PhyloNode
from ete3 import PhyloTree


# this app sets the min branch length for branch with no length
_fillin_length = get_app("scale_branches")


@define_app
def cogent3_to_ete3(tree: PhyloNode) -> PhyloTree:
    """convert a c3 tree to ete3 tree"""
    # handle empty branch length in c3 to satisfy the fixed format of ete3
    tree = _fillin_length(tree)
    newick = tree.get_newick(
        with_distances=True, with_node_names=True, semicolon=True, escape_name=True
    )  # a newick str with no root name
    support = {
        edge.name: edge.params.get("support", None)
        for edge in tree.get_edge_vector(include_root=True)
    }
    ete_tree = PhyloTree(
        newick, format=3, quoted_node_names=True
    )  # incoporate newick str into ete3 as indicated by `format`

    for node in ete_tree.traverse():  # type: ignore
        support_value = support.get(
            node.name or "root"
        )  # in ete3, the root always named as an empty str
        if support_value is not None:  # intrude whenever support exists
            node.support = support_value

    return ete_tree


@define_app
def ete3_to_cogent3(ete_tree: PhyloTree) -> PhyloNode:
    """convert an ete3 tree to c3 tree"""
    ete_tree = ete_tree.copy()
    # assign all internal nodes names
    count = 0
    for node in ete_tree.traverse():  # type: ignore
        if node.name == "" and not node.is_root():
            node.name = f"edge.{count}"
            count += 1

    newick = ete_tree.write(format=3)
    support = {node.name: node.support for node in ete_tree.traverse()}  # type: ignore
    tree = make_tree(newick)

    for node in tree.traverse():
        name = "" if node.name == "root" else node.name
        node.params["support"] = support[name]

    return tree
