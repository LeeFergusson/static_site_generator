from textnode import TextNode, TextType

def main():
    node = TextNode("This is a text node", TextType.NORMAL_TEXT, "https://www.boot.dev")
    print(node)

main()
