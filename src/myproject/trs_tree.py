from cogent3 import PhyloNode, make_tree
from cogent3.app.composable import define_app
from ete3 import PhyloTree


@define_app
class C3ToEte3Tree:
    """convert a c3 tree to ete3 tree"""

    def _get_support(self, tree):
        return {
            edge.name: edge.params.get("support", None)
            for edge in tree.get_edge_vector(include_root=True)
        }

    def _apply_support(self, ete_tree):
        for node in ete_tree.traverse():
            support_value = self._support_values.get(
                node.name or "root"
            )  # in ete3, the root always named as an empty str
            if support_value is not None:  # intrude whenever support exists
                node.support = support_value

    def main(self, tree: PhyloNode) -> PhyloTree:
        self._newick_str = tree.get_newick(
            with_distances=True, with_node_names=True, semicolon=True, escape_name=True
        )  # a newick str with no root name
        self._support_values = self._get_support(tree)
        ete_tree = PhyloTree(
            self._newick_str, format=3
        )  # incoporate newick str into ete3 as indicated by `format`
        self._apply_support(ete_tree)
        return ete_tree


@define_app
class Ete3ToC3Tree:
    """convert an ete3 tree to c3 tree"""

    def _get_support(self, _ete_tree):
        return {node.name: node.support for node in _ete_tree.traverse()}

    def _apply_support(self, tree):
        for node in tree.traverse():
            name = "" if node.name == "root" else node.name
            node.params["support"] = self._support_values[name]

    def _assign_names(self, _ete_tree):
        count = 0
        for node in _ete_tree.traverse():
            if node.name == "" and not node.is_root():
                node.name = f"edge.{count}"
                count += 1

    def main(self, ete_tree: PhyloTree) -> PhyloNode:

        _ete_tree = ete_tree.copy()
        self._assign_names(_ete_tree)  # assign all internal nodes names
        self._newick_str = _ete_tree.write(format=3)
        self._support_values = self._get_support(_ete_tree)
        tree = make_tree(self._newick_str)
        self._apply_support(tree)
        return tree
