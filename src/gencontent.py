import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            split = line[2:]
            title = split.strip()
            return title
    else:
        raise Exception("No header")

def generate_page(from_path, template_path, dest_path, basepath=None):
    print(f"Generating from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as file:
        markdown_contents = file.read()
    
    with open(template_path, "r") as file:
        template_contents = file.read()
    
    html_node = markdown_to_html_node(markdown_contents)
    mkd_html = html_node.to_html()

    title = extract_title(markdown_contents)

    full_html = template_contents.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", mkd_html)
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath=None):
    cont_list = os.listdir(dir_path_content)
    

    for entry in cont_list:
        full_src_path = os.path.join(dir_path_content, entry)
        full_dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(full_src_path):
            if entry.endswith(".md"):
                entry_html = entry[:-3] + ".html"
                dest_html_path = os.path.join(dest_dir_path, entry_html)
                generate_page(full_src_path, template_path, dest_html_path, basepath)

        else:
            generate_pages_recursive(full_src_path, template_path, full_dest_path)
