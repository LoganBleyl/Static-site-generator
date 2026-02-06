from enum import Enum

from htmlnode import ParentNode, LeafNode, text_node_to_html_node, HTMLNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType


def markdown_to_blocks(markdown):
    blocks = []
    for part in markdown.split("\n\n"):
        part = part.strip()
        if part == "":
            continue
        blocks.append(part)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    if markdown.startswith("###### "):
        return BlockType.HEADING
    elif markdown.startswith("##### "):
        return BlockType.HEADING
    elif markdown.startswith("#### "):
        return BlockType.HEADING
    elif markdown.startswith("### "):
        return BlockType.HEADING
    elif markdown.startswith("## "):
        return BlockType.HEADING
    elif markdown.startswith("# "):
        return BlockType.HEADING

    elif markdown.startswith("```\n") and markdown.endswith("\n```") and len(markdown.split("\n")) > 1:
        return BlockType.CODE
    
    elif markdown.startswith(">"):
        for line in markdown.split("\n"):
            if not line.startswith(">"):
                break
        else:
            return BlockType.QUOTE
    
    elif markdown.startswith("- "):
        for line in markdown.split("\n"):
            if not line.startswith("- "):
                break
        else:
            return BlockType.UNORDERED_LIST
    
    line_num = 1

    if markdown.startswith(f"{line_num}. "):
        line_num = 1

        for line in markdown.split("\n"):
            if line.startswith(f"{line_num}. "):
                line_num += 1
            else:
                break
        else:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    md_block = markdown_to_blocks(markdown)
    nodes = []

    for block in md_block:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            lines = block.split("\n")
            paragraph = " ".join(lines)
            html_node = ParentNode("p", children=text_to_children(paragraph))
            nodes.append(html_node)

        elif block_type == BlockType.HEADING:
            level = heading_level(block)
            tag = f"h{level}"
            clean = block[level + 1:]

            html_node = ParentNode(tag, children=text_to_children(clean))
            nodes.append(html_node)

        elif block_type == BlockType.CODE:
            lines = block.split("\n")
            inner_lines = lines[1:-1]
            clean = "\n".join(inner_lines) + "\n"
            
            text_node = TextNode(clean, TextType.TEXT)
            html_node = text_node_to_html_node(text_node)
            code_node = ParentNode("code", children=[html_node])
            pre_node = ParentNode("pre", children=[code_node])
            nodes.append(pre_node)

        elif block_type == BlockType.QUOTE:
            new_lines = []
            lines = block.split("\n")
            for line in lines:
                new_line = line[1:].lstrip()
                new_lines.append(new_line)
            
            clean = " ".join(new_lines)
            html_node = ParentNode("blockquote", children=text_to_children(clean))
            nodes.append(html_node)

        elif block_type == BlockType.UNORDERED_LIST:
            new_lines = []
            lines = block.split("\n")
            for line in lines:
                inner_lines = line[2:]
                new_line = ParentNode("li", children=text_to_children(inner_lines))
                new_lines.append(new_line)
            html_node = ParentNode("ul", children=new_lines)
            nodes.append(html_node)

        elif block_type == BlockType.ORDERED_LIST:
            new_lines = []
            lines = block.split("\n")
            for line in lines:
                parts = line.split(". ", 1)
                item_text = parts[1]
                new_line = ParentNode("li", children=text_to_children(item_text))
                new_lines.append(new_line)
            html_node = ParentNode("ol", children=new_lines)
            nodes.append(html_node)

    return ParentNode(tag="div", children=nodes)


def text_to_children(text):
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

def heading_level(markdown):
    if markdown.startswith("###### "):
        return 6
        
    elif markdown.startswith("##### "):
        return 5

    elif markdown.startswith("#### "):
        return 4

    elif markdown.startswith("### "):
        return 3

    elif markdown.startswith("## "):
        return 2

    elif markdown.startswith("# "):
        return 1

