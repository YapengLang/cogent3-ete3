from enum import Enum

from cogent3.app.composable import define_app
from ete3 import NodeStyle, PhyloTree, TextFace


class McatColour(Enum):
    identity = "#FAC71D"
    sympathetic = "#2065F7"
    limit = "#2065F7"
    chainsaw = "#FF0000"


@define_app
class colour_edge:
    """colour certain edges based on mtx type"""

    def __init__(self, mapping: dict[str, str]) -> None:
        self.mapping = mapping

    def main(self, ete_tree: PhyloTree) -> PhyloTree:

        for node in ete_tree.traverse():
            if node.name in self.mapping:
                # add colour
                style = NodeStyle()
                style["hz_line_color"] = McatColour[self.mapping[node.name]].value
                style["vt_line_color"] = McatColour[self.mapping[node.name]].value
                style["vt_line_width"] = 2
                style["hz_line_width"] = 2
                node.set_style(style)
                node.set_style(style)

                # add caption
                label = TextFace(f"{self.mapping[node.name]}")
                label.opacity = 0.5  # from 0 to 1
                label.inner_border.width = 1  # 1 pixel border
                label.inner_border.type = 1  # dashed line
                label.border.width = 1
                label.background.color = "grey"
                node.add_face(label, column=0, position="branch-top")
        return ete_tree
