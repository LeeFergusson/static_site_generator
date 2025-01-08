"""A module to represent a text node"""
from enum import Enum

class TextType(Enum):
    """An enum class to represent the type of text node"""
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    """A class to represent a text node"""
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
