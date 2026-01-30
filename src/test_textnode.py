import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_two(self):
        node3 = TextNode("Another Text Node", None, "www.Boot.dev")
        node4 = TextNode("Another Text Node", None, "www.Boot.dev")
        self.assertEqual(node3, node4)

    def test_three(self):
        node5 = TextNode("Hmmmmmm what's this", TextType.ITALIC, None)
        node6 = TextNode("Hmmmmmm what's this", TextType.ITALIC, "www.Boot.dev")
        self.assertNotEqual(node5, node6)


if __name__ == "__main__":
    unittest.main()
