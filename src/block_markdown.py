from enum import Enum
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"
    
def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    btype = block_to_block_type(block)
    match btype:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return header_block_to_html_node(block)
        case BlockType.CODE:
            return code_block_to_html_node(block)
        case BlockType.QUOTE:
            return quote_block_to_html_node(block)
        case BlockType.ULIST:
            return ulist_block_to_html_node(block)
        case BlockType.OLIST:
            return olist_block_to_html_node(block)
        case _:
            raise ValueError("Invalid block type.")

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    return [text_node_to_html_node(tn) for tn in textnodes]

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode('p', children)

def header_block_to_html_node(block):
    level = 0
    while level < len(block) and block[level] == "#":
        level += 1
        
    if level + 1 >= len(block):
        raise ValueError("Invalid heading: No content following #s")
    
    text = block[level + 1:]
    children = text_to_children(text)
    
    return ParentNode(f"h{level}", children)
    
def code_block_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block.")
    
    text = block[4:-3]
    code_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(code_text_node)
    return ParentNode("pre", [ParentNode("code", [child])])

def quote_block_to_html_node(block):
    lines = block.split("\n")
    unquoted = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block.")
        unquoted.append(line.lstrip(">").strip())
    
    children = text_to_children(" ".join(unquoted))
    return ParentNode("blockquote", children)

def ulist_block_to_html_node(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        line = line[1:]
        line = line.lstrip()
        li_nodes.append(ParentNode("li", children=text_to_children(line)))
    
    return ParentNode("ul", children=li_nodes)

def olist_block_to_html_node(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        level = 0
        while level < len(line) and line[level] != ".":
            level += 1
            
        line = line[level+1:]
        line = line.lstrip()
        li_nodes.append(ParentNode("li", children=text_to_children(line)))
    
    return ParentNode("ol", children=li_nodes)
    
def block_to_block_type(block):
    lines = block.split("\n")
    
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and (lines[0].startswith("```") and lines[-1].startswith("```")):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}. '):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    
    return BlockType.PARAGRAPH
    
def markdown_to_blocks(md):
    split_md = md.split("\n\n")
    blocks = []
    
    for line in split_md:
        stripped = line.strip()
        if stripped:
            blocks.append(stripped)
    return blocks