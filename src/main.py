from enum import Enum
from textnode import TextNode, TextType
import os
import shutil

def copy_recursive(src, dst):
    for name in os.listdir(src):
        item_src = os.path.join(src, name)
        item_dst = os.path.join(dst, name)
    
        if os.path.isfile(item_src):
            shutil.copy(item_src, item_dst)
        else:
            os.mkdir(item_dst)
            copy_recursive(item_src, item_dst)

def main():
    node =TextNode("some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
    
    this_dir = os.path.dirname(__file__)
    project_root = os.path.join(this_dir, "..")
    public_dir = os.path.join(project_root, "public")
    static_dir = os.path.join(project_root, "static")

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    os.mkdir(public_dir)

    copy_recursive(static_dir, public_dir)

main()
