from cogent3 import load_aligned_seqs, load_tree
from ete3 import PhyloTree
from numpy import allclose, array, float64

from myproject.trs_tree import C3ToEte3Tree, Ete3ToC3Tree


class TestsC3ToEte3Tree:
    def test_tip_names(self):
        tree = load_tree("data/test_tree.newick")
        trs = C3ToEte3Tree()
        ete_tree = trs(tree)
        assert set(tree.get_tip_names()) == set(ete_tree.get_species())

    def test_tip2tip_dist(self):
        tree = load_tree("data/test_tree.newick")
        trs = C3ToEte3Tree()
        ete_tree = trs(tree)
        assert allclose(
            array(ete_tree.cophenetic_matrix()[0]),
            tree.tip_to_tip_distances()[0],
        )

    def test_topology(self):
        tree = load_tree("data/test_tree.newick")
        trs = C3ToEte3Tree()
        ete_tree = trs(tree)
        output = ete_tree.write(format=8)
        expected = tree.get_newick(with_node_names=True)
        assert output == expected

    def test_branch_support(self):
        algn = load_aligned_seqs("../tests/data/algn.fasta", moltype="protein")
        tree = algn.quick_tree(bootstrap=10, show_progress=False)
        trs = C3ToEte3Tree()
        ete_tree = trs(tree)

        support = {
            node.name: node.params.get("support", 1.0)
            for node in tree.get_edge_vector()
        }

        assert all(
            allclose(support[node.name], node.support)
            for node in ete_tree.traverse()
            if node.name
        )


class TestsEte3ToC3Tree:
    def test_topology(self):
        ete_tree = PhyloTree("data/test_tree.newick", format=5)
        trs = Ete3ToC3Tree()
        tree_output = trs(ete_tree)
        tree_expected = load_tree("data/test_tree.newick")
        assert tree_expected.same_topology(tree_output)

    def test_branch_support(self):
        ete_tree = PhyloTree("data/test_tree_withsupport.newick", format=2)
        expected = {node.support for node in ete_tree.traverse()}
        trs = Ete3ToC3Tree()
        tree = trs(ete_tree)
        output = {node.params["support"] for node in tree.get_edge_vector()}
        assert expected == output
