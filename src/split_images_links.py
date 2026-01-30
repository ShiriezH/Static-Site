from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        # Only split TEXT nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        images = extract_markdown_images(text)

        # If no images, keep the node
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for alt, url in images:
            split_text = text.split(f"![{alt}]({url})", 1)

            # Add text before image
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))

            # Add image node
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            # Continue with the remaining text
            text = split_text[1]

        # Add leftover text after the last image
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        # Only split TEXT nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        links = extract_markdown_links(text)

        # If no links, keep the node
        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for anchor, url in links:
            split_text = text.split(f"[{anchor}]({url})", 1)

            # Add text before link
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))

            # Add link node
            new_nodes.append(TextNode(anchor, TextType.LINK, url))

            # Continue with remaining text
            text = split_text[1]

        # Add leftover text after last link
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes