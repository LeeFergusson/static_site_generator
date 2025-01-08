"""Test cases for the TextNode class."""
import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    """Test cases for the TextNode class."""
    def test_eq(self):
        """Test the equality of two TextNode objects."""
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        """Test the string representation of a TextNode object."""
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_no_url(self):
        """Test the url attribute of a TextNode object with no url."""
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_with_url(self):
        """Test the url attribute of a TextNode object with a url."""
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node.url, "https://www.boot.dev")


if __name__ == "__main__":
    unittest.main()
