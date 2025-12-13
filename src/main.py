from textnode import TextNode, TextType

def main():
    node = TextNode("Anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
    
main()