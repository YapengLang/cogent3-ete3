from enum import Enum

from ete3 import NodeStyle, PhyloTree


class McatColour(Enum):
    identity = "#FAC71D"
    sympathetic = "#2065F7"
    limit = "#2065F7"
    chainsaw = "#FF0000"
    dlc = "#000000"


class colour_edge:
    """colour certain edges based on mtx type"""

    def __call__(self, ete_tree: PhyloTree, mcats: dict) -> None:

        for node in ete_tree.traverse():
            if node.name in mcats:
                style = NodeStyle()
                style["hz_line_color"] = McatColour[mcats[node.name]].value
                style["vt_line_color"] = McatColour[mcats[node.name]].value
                style["vt_line_width"] = 2
                style["hz_line_width"] = 2
                node.set_style(style)
                node.set_style(style)
