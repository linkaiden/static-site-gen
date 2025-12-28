from pathlib import Path
from block_markdown import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_dir = Path(dir_path_content)
    dest_dir = Path(dest_dir_path)

    for item in content_dir.iterdir():
        if item.is_file():
            if item.suffix == ".md":
                dest_path = dest_dir / item.name
                dest_path = dest_path.with_suffix(".html")
                generate_page(item, template_path, dest_path, basepath)
            
        elif item.is_dir():
            new_dest_dir = dest_dir / item.name
            generate_pages_recursive(item, template_path, new_dest_dir, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    from_path, template_path, dest_path = Path(from_path), Path(template_path), Path(dest_path)
    print(f' * {from_path} {template_path} -> {dest_path}')
    
    markdown = from_path.read_text()
    template = template_path.read_text()
    
    html = markdown_to_html_node(markdown)
    title = extract_title(markdown)
    
    final_template = (
        template.replace("{{ Title }}", title)
                .replace("{{ Content }}", html.to_html())
                .replace('href="/', f'href="{basepath}')
                .replace('src="/', f'src="{basepath}')
    )

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    dest_path.write_text(final_template)
        
def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
        
    raise ValueError("Missing header.")