from enum import Enum
from textnode import TextNode, TextType

def main():
    node =TextNode("some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
main()

