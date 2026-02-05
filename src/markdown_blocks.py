from enum import Enum



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
    
