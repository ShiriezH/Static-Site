from block_to_block_type import block_to_block_type
from blocktype import BlockType
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for tn in text_nodes:
        children.append(text_node_to_html_node(tn))
    return children


def heading_level(block):
    # block starts with 1-6 #'s then space
    count = 0
    for ch in block:
        if ch == "#":
            count += 1
        else:
            break
    return count


def strip_heading_markers(block):
    # remove leading "#... " from heading
    level = heading_level(block)
    return block[level + 1 :]


def strip_quote_markers(block):
    lines = block.split("\n")
    cleaned = []
    for line in lines:
        # remove leading ">"
        line = line[1:]
        # optional leading space
        if line.startswith(" "):
            line = line[1:]
        cleaned.append(line)
    return "\n".join(cleaned)


def strip_ul_markers(block):
    lines = block.split("\n")
    cleaned = []
    for line in lines:
        cleaned.append(line[2:])  # remove "- "
    return cleaned


def strip_ol_markers(block):
    lines = block.split("\n")
    cleaned = []
    for line in lines:
        # remove "1. " / "2. " etc
        split_line = line.split(". ", 1)
        cleaned.append(split_line[1])
    return cleaned


def code_block_content(block):
    # block is guaranteed to start with ```\n and end with ```
    lines = block.split("\n")
    # remove first line ``` and last line ```
    content_lines = lines[1:-1]
    return "\n".join(content_lines) + "\n"


def paragraph_text(block):
    # Paragraphs can span multiple lines, but become one <p> with spaces
    return " ".join(block.split("\n"))


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    block_nodes = []

    for block in blocks:
        btype = block_to_block_type(block)

        if btype == BlockType.PARAGRAPH:
            text = paragraph_text(block)
            children = text_to_children(text)
            block_nodes.append(ParentNode("p", children))

        elif btype == BlockType.HEADING:
            level = heading_level(block)
            text = strip_heading_markers(block)
            children = text_to_children(text)
            block_nodes.append(ParentNode(f"h{level}", children))

        elif btype == BlockType.CODE:
            content = code_block_content(block)
            # no inline parsing here
            code_leaf = LeafNode("code", content)
            block_nodes.append(ParentNode("pre", [code_leaf]))

        elif btype == BlockType.QUOTE:
            text = strip_quote_markers(block)
            children = text_to_children(text)
            block_nodes.append(ParentNode("blockquote", children))

        elif btype == BlockType.UNORDERED_LIST:
            items = strip_ul_markers(block)
            li_nodes = []
            for item in items:
                li_nodes.append(ParentNode("li", text_to_children(item)))
            block_nodes.append(ParentNode("ul", li_nodes))

        elif btype == BlockType.ORDERED_LIST:
            items = strip_ol_markers(block)
            li_nodes = []
            for item in items:
                li_nodes.append(ParentNode("li", text_to_children(item)))
            block_nodes.append(ParentNode("ol", li_nodes))

        else:
            raise Exception("Unknown block type")

    return ParentNode("div", block_nodes)

