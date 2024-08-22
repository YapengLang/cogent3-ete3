from cogent3.app.composable import define_app
from ete3 import NodeStyle, PhyloTree, TextFace, TreeStyle


@define_app
class ete3_colour_edge:
    """colour certain edges based on a edge mapping"""

    def __init__(
        self,
        edge_to_cat: dict[str, str],
        cat_to_colour: dict[str, str],
        line_width: int = 2,
    ) -> None:
        """
        Args:
            edge_to_cat: keys are ete3 tree node names, values are category names
            cat_to_colour: category name to colour mapping
        """
        self._edge_to_cat = edge_to_cat
        self._cat_to_colour = cat_to_colour
        self._line_width = line_width

    def main(self, ete_tree: PhyloTree) -> PhyloTree:
        ete_tree = ete_tree.copy()
        for node in ete_tree.traverse():  # type: ignore
            if node.name in self._edge_to_cat:
                # add colour
                style = NodeStyle()
                cat = self._edge_to_cat[node.name]
                style["hz_line_color"] = self._cat_to_colour[cat]
                style["hz_line_width"] = self._line_width
                node.set_style(style)

        return ete_tree


def show_legend(
    ete_tree_coloured: PhyloTree,
    cat_to_colour: dict[str, str],
    legend_title: str,
    legend_size: int = 14,
    legend_colour: str = "black",
    legend_font: str = "Arial",
    entry_size: int = 14,
    entry_font: str = "Arial",
) -> None:  # pragma: no cover
    # Create a custom face for the caption
    ts = TreeStyle()
    ts.show_leaf_name = False
    title_textface = TextFace(
        legend_title, fsize=legend_size, fgcolor=legend_colour, ftype=legend_font
    )
    ts.legend.add_face(title_textface, column=0)

    edge_colours = {
        node.img_style["hz_line_color"]
        for node in ete_tree_coloured.traverse()  # type: ignore
    }

    for k, v in cat_to_colour.items():
        if v in edge_colours:
            entry_textface = TextFace(k, fsize=entry_size, fgcolor=v, ftype=entry_font)
            ts.legend.add_face(entry_textface, column=0)

    ete_tree_coloured.show(tree_style=ts)
