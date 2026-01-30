import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_strips_whitespace(self):
        md = "  # Heading  \n\n   Paragraph text   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["# Heading", "Paragraph text"])

    def test_markdown_to_blocks_removes_empty_blocks(self):
        md = "First block\n\n\n\nSecond block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block"])


if __name__ == "__main__":
    unittest.main()