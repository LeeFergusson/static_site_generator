"""Test cases for the HTMLNode class."""
import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()
