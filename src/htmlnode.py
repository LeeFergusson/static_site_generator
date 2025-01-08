"""HTMLNode class for representing HTML nodes """
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
