from enum import Enum
from textnode import TextNode, TextType 

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props:
            props_str = ""

            for key, value in self.props.items():
                props_str += f' {key}="{value}"'
            return props_str
        else:
            return ""
    def __repr__(self):
        node = f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        return node

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("missing value!")
        
        elif self.tag == None:
            return self.value
        
        else:
            attrs = self.props_to_html() if self.props else ""
            return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"

    def __repr__(self):
        node = f"LeafNode({self.tag}, {self.value}, {self.props})"
        return node

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("missing tag!")
        
        elif self.children == None or self.children == []:
            raise ValueError("missing child!")
        
        else:
            attrs = self.props_to_html() if self.props else ""
            children_to_html = ""

            for child in self.children: 
                children_to_html = children_to_html + child.to_html()
            return f"<{self.tag}{attrs}>{children_to_html}</{self.tag}>"

def text_node_to_html_node(text_node):
    if TextType.TEXT == text_node.text_type:
        return LeafNode(None, text_node.text)
    
    elif TextType.BOLD == text_node.text_type:
        return LeafNode("b", text_node.text)
    
    elif TextType.ITALIC == text_node.text_type:
        return LeafNode("i", text_node.text)

    elif TextType.CODE == text_node.text_type:
        return LeafNode("code", text_node.text)

    elif TextType.LINK == text_node.text_type:
        return LeafNode("a", text_node.text, {"href": text_node.url})

    elif TextType.IMAGE == text_node.text_type:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    else:
        raise Exception("missing TextNode!")
