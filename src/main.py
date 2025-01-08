"""Main module to test the TextNode class"""
from textnode import TextNode, TextType
from htmlnode import text_node_to_html_node


def main():
    """Main function"""
    text_node = TextNode("This is a paragraph", TextType.NORMAL)
    html_node = text_node_to_html_node(text_node)
    print(html_node.to_html())

main()
