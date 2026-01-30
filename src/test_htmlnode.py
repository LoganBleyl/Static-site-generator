import unittest

from htmlnode import HTMLNode

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
  
if __name__ == "__main__":
    unittest.main()
