"""Test cases for the HTMLNode class."""
import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, split_nodes_delimiter, text_node_to_html_node
from textnode import TextNode, TextType

class TestHtmlNode(unittest.TestCase):
    """Test cases for the HTMLNode class."""
    def test_eq(self):
        """Test the equality of two HtmlNode objects."""
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node, node2)

    def test_repr(self):
        """Test the string representation of a HtmlNode object."""
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(
            repr(node),
            "HTMLNode(p, This is a paragraph, None, None)"
        )

    def test_props_to_html(self):
        """Test the props_to_html method of a HtmlNode object."""
        node = HTMLNode(
            "a",
            "This is a link",
            props=[
                ("href", "https://www.boot.dev"),
                ("target", "_blank")
            ]
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

    def test_props_to_html_none(self):
        """Test the props_to_html method of a HtmlNode object with no props."""
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.props_to_html(), "")

    def test_no_tag(self):
        """Test the tag attribute of a HtmlNode object with no tag."""
        node = HTMLNode(value="This is a paragraph")
        self.assertEqual(node.tag, None)

class TestLeafNode(unittest.TestCase):
    """Test cases for the LeafNode class."""
    def test_eq(self):
        """Test the equality of two LeafNode objects."""
        node1 = LeafNode("This is a paragraph", "p")
        node2 = LeafNode("This is a paragraph", "p")

        self.assertEqual(node1, node2)

    def test_leaf_node_has_no_children(self):
        """Test the children attribute of a LeafNode object."""
        node = LeafNode("This is a paragraph", "p")
        self.assertEqual(node.children, None)

    def test_leaf_node_to_html(self):
        """Test the to_html method of a LeafNode object."""
        node = LeafNode("This is a paragraph", "p")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")


class TestParentNode(unittest.TestCase):
    """Test cases for the ParentNode class."""
    def test_eq(self):
        """Test the equality of two ParentNode objects."""
        node1 = ParentNode("div", [LeafNode("This is a paragraph", "p")])
        node2 = ParentNode("div", [LeafNode("This is a paragraph", "p")])

        self.assertEqual(node1, node2)

    def test_parent_node_has_children(self):
        """Test the children attribute of a ParentNode object."""
        node = ParentNode("div", [LeafNode("This is a paragraph", "p")])
        self.assertEqual(node.children, [LeafNode("This is a paragraph", "p")])

    def test_parent_node_to_html(self):
        """Test the to_html method of a ParentNode object."""
        node = ParentNode("div", [LeafNode("This is a paragraph", "p")])
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph</p></div>")

    def test_parent_node_no_children(self):
        """Test the to_html method of a ParentNode object with no children."""
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_node_no_tag(self):
        """Test the to_html method of a ParentNode object with no tag."""
        node = ParentNode(None, children=[LeafNode("This is a paragraph", "p")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_nested_parents(self):
        """Test the to_html method of a ParentNode object with nested parents."""
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "div",
                    [LeafNode("This is a paragraph", "p")]
                )
            ]
        )
        self.assertEqual(node.to_html(), "<div><div><p>This is a paragraph</p></div></div>")

class TestFromTextNodeToHtmlNode(unittest.TestCase):
    """Test cases for the text_node_to_html_node function."""
    def test_normal_text_node(self):
        """Test the text_node_to_html_node function with a normal text node."""
        text_node = TextNode("This is a paragraph", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "This is a paragraph")

    def test_bold_text_node(self):
        """Test the text_node_to_html_node function with a bold text node."""
        text_node = TextNode("This is a paragraph", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>This is a paragraph</b>")

    def test_italic_text_node(self):
        """Test the text_node_to_html_node function with an italic text node."""

        text_node = TextNode("This is a paragraph", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>This is a paragraph</i>")

    def test_code_text_node(self):
        """Test the text_node_to_html_node function with a code text node."""
        text_node = TextNode("This is a paragraph", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>This is a paragraph</code>")

    def test_link_text_node(self):
        """Test the text_node_to_html_node function with a link text node."""
        text_node = TextNode("This is a paragraph", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            html_node.to_html(),
            '<a href="https://www.boot.dev">This is a paragraph</a>'
        )

    def test_image_text(self):
        """Test the text_node_to_html_node function with an image text node."""


        text_node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            html_node.to_html(),
            '<img src="https://www.boot.dev/image.png" alt="This is an image"></img>'
        )

class TestSplitNodesDelimiter(unittest.TestCase):
    """Test cases for the split_nodes_delimiter function."""
    def test_split_nodes_delimiter(self):
        """Test the split_nodes_delimiter function."""
        result = split_nodes_delimiter(
            [TextNode("This is *bold*", TextType.TEXT)],
            "*",
            TextType.BOLD
        )
        self.assertEqual(
            result,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD)
            ]
        )

    def test_split_nodes_delimiter_no_delimiter(self):
        """Test the split_nodes_delimiter function with no delimiter."""
        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [TextNode("This is bold", TextType.TEXT)],
                "",
                TextType.TEXT
            )

    def test_split_nodes_delimiter_no_nodes(self):
        """Test the split_nodes_delimiter function with no nodes."""
        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [],
                "*",
                TextType.BOLD
            )

    def test_split_nodes_delimiter_no_text(self):
        """Test the split_nodes_delimiter function with no text."""
        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [TextNode("", TextType.TEXT)],
                "*",
                TextType.BOLD
            )

    def test_split_nodes_delimiter_no_text_type(self):
        """Test the split_nodes_delimiter function with no text type."""
        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [TextNode("This is bold", TextType.TEXT)],
                "*",
                None
            )

if __name__ == "__main__":
    unittest.main()
