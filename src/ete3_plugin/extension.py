from enum import Enum

from cogent3.app.composable import define_app
from ete3 import NodeStyle, PhyloTree, TextFace, TreeStyle


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
        self._caption = {}

    def main(self, ete_tree: PhyloTree) -> PhyloTree:

        for node in ete_tree.traverse():  # type: ignore
            if node.name in self.mapping:
                # add colour
                style = NodeStyle()
                mcat = self.mapping[node.name]
                colour = McatColour[mcat].value
                style["hz_line_color"] = colour
                style["hz_line_width"] = 2
                node.set_style(style)
                if mcat not in self._caption:
                    self._caption[mcat] = colour

        return ete_tree

    def add_caption(self, ete_tree: PhyloTree) -> None:
        # Create a custom face for the caption
        ts = TreeStyle()
        caption_label = TextFace(
            "Matrix Category:", fsize=14, fgcolor="black", ftype="Arial"
        )
        ts.legend.add_face(caption_label, column=0)

        for k, v in self._caption.items():
            caption_face = TextFace(k, fsize=14, fgcolor=v, ftype="Arial")
            ts.legend.add_face(caption_face, column=0)

        ete_tree.show(tree_style=ts)
