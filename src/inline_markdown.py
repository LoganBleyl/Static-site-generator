from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        split_nodes = []
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        
        elif node.text_type == TextType.TEXT:
            split_node = node.text.split(delimiter)
            if len(split_node) % 2 == 0:
                raise ValueError("delimiter not matched!")
            for i in range(len(split_node)):
                if split_node[i] == "":
                    continue 

                if i % 2 == 0:
                    text = split_node[i]
                    texttype = TextType.TEXT
                    new_node = TextNode(text, texttype)
                    split_nodes.append(new_node)
                else:
                    text = split_node[i]
                    new_node = TextNode(text, text_type)
                    split_nodes.append(new_node)
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images= extract_markdown_images(node.text)
            if len(images) ==0:
                new_nodes.append(node)
                continue
            remaining_text = node.text

            for alt, url in images:
                markdown = f"![{alt}]({url})"
                before, after = remaining_text.split(markdown, 1)
                if before != "":
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                remaining_text = after
            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images= extract_markdown_links(node.text)
            if len(images) ==0:
                new_nodes.append(node)
                continue
            remaining_text = node.text

            for alt, url in images:
                markdown = f"[{alt}]({url})"
                before, after = remaining_text.split(markdown, 1)
                if before != "":
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(alt, TextType.LINK, url))
                remaining_text = after
            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
