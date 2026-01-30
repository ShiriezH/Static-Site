import re

from blocktype import BlockType


def block_to_block_type(block):
    # Heading: 1-6 #'s then a space
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    # Code block: starts with ``` and ends with ```
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")

    # Quote block: every line starts with >
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list: every line starts with "- "
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list: every line starts with "1. ", "2. ", "3. " etc (must increment)
    ordered = True
    for i, line in enumerate(lines):
        expected = f"{i+1}. "
        if not line.startswith(expected):
            ordered = False
            break
    if ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH