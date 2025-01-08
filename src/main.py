"""Main module to test the TextNode class"""
from textnode import TextNode, TextType

def main():
    """Main function to test the TextNode class"""
    node = TextNode(
        "This is a text node",
        TextType.NORMAL,
        "https://www.boot.dev"
    )
    print(node)

main()
