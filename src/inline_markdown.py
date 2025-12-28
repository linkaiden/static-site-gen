from collections import Counter
from textnode import TextType, TextNode
import re

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    pattern = f'({re.escape(delimiter)})'
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        delimit_count = Counter(node.text)
        if (delimit_count[delimiter] % 2 ) > 0: 
            raise ValueError("Invalid text: Missing closing delimiter")
        
        delim_split = re.split(pattern, node.text)
        content = False
        
        for text in delim_split:
            if not text:
                continue
            if delimiter in text:
                content = not content
            if (delimiter not in text) and not content:
                new_nodes.append(TextNode(text, TextType.TEXT))
            if (delimiter not in text) and content:
                new_nodes.append(TextNode(text, text_type))
    
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        
        if not images:
            new_nodes.append(node)
            continue
        
        text = node.text
        for alt, url in images:
            img_md = f'![{alt}]({url})'
            if img_md not in text:
                raise ValueError(f'Invalid markdown image: {img_md!r} not found in {text!r}')
            before_img, text = text.split(img_md, 1)
            
            if before_img:
                new_nodes.append(TextNode(before_img, TextType.TEXT))
            
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
        
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
            
    return new_nodes
        
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        
        if not links:
            new_nodes.append(node)
            continue
        
        text = node.text
        for alt, url in links:
            link_md = f'[{alt}]({url})'
            if link_md not in text:
                raise ValueError(f'Invalid markdown link: {link_md!r} not found in {text!r}')
            
            before_link, text = text.split(link_md, 1)
            
            if before_link:
                new_nodes.append(TextNode(before_link, TextType.TEXT))
            
            new_nodes.append(TextNode(alt, TextType.LINK, url))
        
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
            
    return new_nodes

def extract_markdown_images(text):
    img_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(img_regex, text)

def extract_markdown_links(text):
    link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(link_regex, text)