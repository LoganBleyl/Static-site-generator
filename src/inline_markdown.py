from textnode import TextNode, TextType

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

