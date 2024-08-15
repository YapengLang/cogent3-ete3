from cogent3 import load_aligned_seqs, load_tree, make_tree
from ete3 import PhyloTree
from numpy import allclose, array

from cogent3_ete3.interconvert import cogent3_to_ete3, ete3_to_cogent3


def test_emtpy_branch_length_ete3():
    tree = make_tree("(a,b,c);")
    trs = cogent3_to_ete3()
    ete_tree = trs(tree)
    branch_lengths = [node.dist for node in ete_tree.traverse() if node.name]
    assert allclose(branch_lengths, [1e-06, 1e-06, 1e-06])


def test_tip_names_ete3():
    tree = load_tree("data/test_tree.newick")
    trs = cogent3_to_ete3()
    ete_tree = trs(tree)
    assert set(tree.get_tip_names()) == set(ete_tree.get_leaf_names())


def test_tip_names_ete3_large():
    tree = load_tree("data/test_tree_large_scale.newick")
    trs = cogent3_to_ete3()
    ete_tree = trs(tree)
    assert set(tree.get_tip_names()) == set(ete_tree.get_leaf_names())


def test_tip2tip_dist_ete3():
    tree = load_tree("data/test_tree.newick")
    trs = cogent3_to_ete3()
    ete_tree = trs(tree)
    assert allclose(
        array(ete_tree.cophenetic_matrix()[0]),
        tree.tip_to_tip_distances()[0],
    )


def test_topology_ete3():
    tree = load_tree("data/test_tree.newick")
    trs = cogent3_to_ete3()
    ete_tree = trs(tree)
    output = ete_tree.write(format=8)
    expected = tree.get_newick(with_node_names=True)
    assert output == expected


def test_branch_support_ete3():
    algn = load_aligned_seqs("data/algn.fasta", moltype="protein")
    tree = algn.quick_tree(bootstrap=10, show_progress=False)
    trs = cogent3_to_ete3()
    ete_tree = trs(tree)

    support = {
        node.name: node.params.get("support", 1.0) for node in tree.get_edge_vector()
    }

    assert all(
        allclose(support[node.name], node.support)
        for node in ete_tree.traverse()
        if node.name
    )


def test_topology_c3():
    ete_tree = PhyloTree("data/test_tree.newick", format=5)
    trs = ete3_to_cogent3()
    tree_output = trs(ete_tree)
    tree_expected = load_tree("data/test_tree.newick")
    assert tree_expected.same_topology(tree_output)


def test_branch_support_c3():
    ete_tree = PhyloTree("data/test_tree_withsupport.newick", format=2)
    expected = {node.support for node in ete_tree.traverse()}  # type: ignore
    trs = ete3_to_cogent3()
    tree = trs(ete_tree)
    output = {node.params["support"] for node in tree.get_edge_vector()}
    assert expected == output
