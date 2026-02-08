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

def generate_page(from_path, template_path, dest_path):
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
    
    with open(dest_path, "w") as file:
        file.write(full_html)
