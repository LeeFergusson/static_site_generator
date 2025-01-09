"""HTMLNode class for representing HTML nodes """
from textnode import TextNode, TextType


class HTMLNode:
    """Class for representing HTML nodes"""
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """Convert the node to an HTML string"""
        raise NotImplementedError()

    def props_to_html(self):
        """Convert the props to an HTML string"""
        result = ""
        if self.props:
            for prop in self.props:
                result += f" {prop[0]}=\"{prop[1]}\""
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

class LeafNode(HTMLNode):
    """Class for representing leaf nodes"""
    def __init__(self, value, tag, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    """Class for representing parent nodes"""
    def __init__(self, tag,  children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Parent nodes must have children")
        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    """Convert a TextNode to an HTMLNode"""
    result = None
    match text_node.text_type:
        case TextType.TEXT:
            result = LeafNode(text_node.text, None)
        case TextType.BOLD:
            result = LeafNode(text_node.text, "b")
        case TextType.ITALIC:
            result = LeafNode(text_node.text, "i")
        case TextType.CODE:
            result = LeafNode(text_node.text, "code")
        case TextType.LINK:
            result = LeafNode(text_node.text, "a", [("href", text_node.url)])
        case TextType.IMAGE:
            result = LeafNode("", "img", [("src", text_node.url), ("alt", "This is an image")])

    if result is None:
        raise ValueError("Invalid TextNode")

    return result

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Split nodes by delimiter and apply text type to each part"""
    if old_nodes is None or len(old_nodes) == 0:
        raise ValueError("Nodes cannot be empty")
    if len(delimiter) == 0:
        raise ValueError("Delimiter cannot be empty")
    if text_type is None:
        raise ValueError("Text type cannot be None")

    new_nodes = []
    for node in old_nodes:
        parts = node.text.split(delimiter)

        if len(parts) % 3 != 0 or len(parts) == 1:
            new_nodes.append(node)
            continue

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes
