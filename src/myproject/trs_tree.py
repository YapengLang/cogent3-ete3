from cogent3 import PhyloNode
from cogent3.app.composable import define_app
from ete3 import PhyloTree


@define_app
class C3ToEte3Tree:

    def main(self, tree: PhyloNode) -> PhyloTree:
        newick_str = tree.get_newick(
            with_distances=True, with_node_names=True, semicolon=True, escape_name=True
        )
        return PhyloTree(newick_str, format=1)
