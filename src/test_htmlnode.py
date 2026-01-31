import unittest
from enum import Enum 
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_Empty(self):
        
        props ={}
        node = HTMLNode("a", "link text", None, props)

        result = node.props_to_html()

        expected = ""
        self.assertEqual(result, expected)

    def test_props_to_html_with_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("a", "link text", None, props)

        result = node.props_to_html()

        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(result, expected)

    def test_repr(self):
        
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = HTMLNode("a", "link text", None, props)

        result = node.__repr__()
        
        expected = "HTMLNode(a, link text, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(result, expected)
 
        
    # LeafNode tests

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        props = {"href": "https://www.google.com"}
        node = LeafNode("a", "Click me!", props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_tags(self):
        props = {"href": "https://www.google.com"}
        node = LeafNode(None, "Click me!", props)
        self.assertNotEqual(node.to_html(), '<href="https://www.google.com">Click me!</>')

    # ParentNode tests

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_children_props(self):
        props = {"href": "https://www.google.com"}
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props)
        self.assertEqual(parent_node.to_html(), '<div href="https://www.google.com"><span>child</span></div>')

    def test_to_html_with_children_tag(self):
        child_node = LeafNode(None, "child")
        parent_node = ParentNode("div", [child_node])
        self.assertNotEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_children_tag2(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_child(self):
        child_node = LeafNode("b", None)
        parent_node = ParentNode("div", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    # TextNode function tests

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_exc(self):
        node = TextNode(None, TextType.TEXT)
        html_node = text_node_to_html_node(node)
        with self.assertRaises(Exception):
            parent_node.to_html()

    def test_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")



if __name__ == "__main__":
    unittest.main()
