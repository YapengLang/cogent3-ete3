from cogent3 import load_tree
from numpy import allclose, array, float64

from myproject.trs_tree import C3ToEte3Tree


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
