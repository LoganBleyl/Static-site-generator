import unittest
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )



    def test_markdown_to_blocks2(self):
        md = """
This is [link](www.boot.dev) paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is [link](www.boot.dev) paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

        # Blocktype Tests 
    
    def test_block_to_blocktype(self):
        md = "> This is a quote.\n> It can span multiple lines.\n> Every line starts with a greater-than symbol."
        block = block_to_block_type(md)
        block_type = BlockType.QUOTE
        self.assertEqual(block, block_type)

    def test_block_to_blocktype_unmatched_quote(self):
        md = "> This is a quote.\n It can span multiple lines.\n Every line starts with a greater-than symbol."
        block = block_to_block_type(md)
        block_type = BlockType.QUOTE
        self.assertNotEqual(block, block_type)

    def test_block_to_blocktype_ordered_list(self):
        md = "1. first line.\n2. second line.\n3. third line"
        block = block_to_block_type(md)
        block_type = BlockType.ORDERED_LIST
        self.assertEqual(block, block_type)

        if __name__ == "__main__":
            unittest.main()
