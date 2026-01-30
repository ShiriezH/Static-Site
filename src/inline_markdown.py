from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        # If it's not plain text, keep it as-is
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # Split the text by the delimiter
        parts = old_node.text.split(delimiter)

        # If we get an even number of parts, delimiter was not properly closed
        # Example: "hello `world" -> ["hello ", "world"] (len=2, even) -> invalid
        if len(parts) % 2 == 0:
            raise Exception(f"Invalid markdown syntax: missing closing delimiter '{delimiter}'")

        # Even index = normal text, odd index = special text_type
        for i in range(len(parts)):
            if parts[i] == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(parts[i], text_type))

    return new_nodes