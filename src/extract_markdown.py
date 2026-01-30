import re


def extract_markdown_images(text):
    # ![alt text](url)
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    # [anchor text](url) but NOT images
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)